# Rod Cutting (GFG)

> **Pattern:** unbounded knapsack (1D DP) · **Best:** O(n²) time, O(n) space · **Code:** [rod_cutting.py](rod_cutting.py)

## 1. Problem

`prices[i]` is the price of a piece of length `i + 1`. The rod has length `n = len(prices)`. Cut it into pieces (or leave it whole) to get the maximum total price.

```
prices = [1, 5, 8, 9, 10, 17, 17, 20]    # n = 8
answer = 22                               # pieces 2 + 6  ->  5 + 17
```

## 2. Draft: work small cases by hand

Sell pieces of a rod of length 8 and see what comes back:

```
l = 8                  -> 20
l = 7, l = 1           -> 17 + 1        = 18
l = 6, l = 1, l = 1    -> 17 + 1 + 1    = 19
l = 6, l = 2           -> 17 + 5        = 22   <- best
```

Every answer is a way to write 8 as a sum of piece lengths:

```
8 + 0
7 + 1
6 + 1 + 1        6 + 2
5 + 1 + 1 + 1    5 + 2 + 1    5 + 3
...
```

**Key observation:** every answer starts with a *first piece* of some length. What is left after it is the *same problem on a shorter rod*.

## 3. From observation to recurrence

First draft:

```
f(k) = prices[k] + f(n - k)
```

What is wrong with it:

- `k` is used both as the piece length and as the function argument.
- `prices[k]` is the price of length `k + 1`, not `k`.
- There is no `max`: we must try every first piece and keep the best.
- There is no base case, so the recursion never stops.

Fixed. Let `f(n)` be the best profit for a rod of length `n`. In code the first piece has length `i + 1`, so its price is `prices[i]` and the rest of the rod has length `n - (i + 1)`:

```
f(0) = 0
f(n) = max over i in 0..n-1 of ( prices[i] + f(n - (i + 1)) )
```

This is exactly the loop from the draft, `prices[k] + f(n-k-1)`, plus a `max` and a base case.

## 4. Four questions before coding

| Question | Answer |
|---|---|
| **State:** what does `f(n)` mean? | Best profit for a rod of length `n` |
| **Choice:** what do we decide at each step? | The length `i + 1` of the first piece |
| **Base case** | `f(0) = 0` (no rod, no profit) |
| **Overlap:** which calls repeat? | `f(2)` is reached from `6 + f(2)`, `5 + 1 + f(2)`, `4 + 2 + f(2)`, ... so memoize |

## 5. Why the first attempt (`cutRod_tle`) was slow

```python
def backtracking(array):
    n = len(array)
    ...
    memo[n] = array[-1]
    for i in range(n):
        curr = backtracking(array[:i]) + backtracking(array[:n-i])
        ...
```

It computes a correct recurrence: split the rod into two parts of lengths `i` and `n - i` and solve both. On random inputs it gives the same answers as the solutions below. The problem is cost, not logic:

1. **Slicing copies the list.** `array[:i]` does O(n) work before *every* call, even when the answer is already in `memo`. That pushes the total to about O(n³).
2. **Two recursive calls per choice, and every split is tried twice.** `(i, n - i)` and `(n - i, i)` are the same cut.
3. **It calls itself on the same length.** At `i = 0`, `array[:n]` has length `n` again. It only stops because `memo[n]` was filled before the loop, which is fragile.

**Lesson:** sell the first piece *whole*. Its price is a fixed number, so only the rest of the rod recurses. That gives one subproblem per choice, and the state is a plain integer instead of a list.

One measured run on random prices (recursion limit raised so the recursive versions finish at n = 1000):

| n | `cutRod_tle` | memoization | tabulation |
|---|---|---|---|
| 250 | 0.014 s | 0.003 s | 0.001 s |
| 500 | 0.088 s | 0.011 s | 0.006 s |
| 1000 | 0.558 s | 0.047 s | 0.025 s |

Doubling `n` makes `cutRod_tle` about 6× slower (a cubic trend) and memoization about 4× slower (quadratic).

## 6. Solutions

### 6.1 Plain recursion: O(2ⁿ)

```python
class Solution:
    def cutRod_recursion(self, prices: list[int]) -> int:
        def f(n: int) -> int:
            if n == 0:
                return 0
            best = 0
            for i in range(n):
                best = max(best, prices[i] + f(n - (i + 1)))
            return best

        return f(len(prices))
```

It makes 2ⁿ calls: 1,024 for n = 10 and 1,048,576 for n = 20.

### 6.2 Top-down (memoization): O(n²)

This is `cutRod` in [rod_cutting.py](rod_cutting.py).

```python
class Solution:
    def cutRod_memo(self, prices: list[int]) -> int:
        memo = {}

        def f(n: int) -> int:
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            best = 0
            for i in range(n):
                best = max(best, prices[i] + f(n - (i + 1)))
            memo[n] = best
            return best

        return f(len(prices))
```

> **Watch out:** the recursion goes `n` levels deep. Python's default recursion limit is 1000, so this raises `RecursionError` at n = 1000. Use tabulation for submissions.

### 6.3 Bottom-up (tabulation): O(n²), no recursion

```python
class Solution:
    def cutRod(self, prices: list[int]) -> int:
        n = len(prices)
        dp = [0] * (n + 1)              # dp[m] = best profit for a rod of length m
        for m in range(1, n + 1):
            for i in range(m):          # first piece has length i + 1
                dp[m] = max(dp[m], prices[i] + dp[m - (i + 1)])
        return dp[n]
```

The table is filled from short rods to long ones, so `dp[m - (i + 1)]` is always ready when `dp[m]` needs it.

### 6.4 Which pieces to cut

The value alone does not say how to cut. For each length, also store the first piece of its best cut, then follow those choices back from `n`:

```python
class Solution:
    def cutRod_pieces(self, prices: list[int]) -> tuple[int, list[int]]:
        n = len(prices)
        dp = [0] * (n + 1)
        first_cut = [0] * (n + 1)       # first_cut[m] = first piece of the best cut for length m
        for m in range(1, n + 1):
            for i in range(m):
                candidate = prices[i] + dp[m - (i + 1)]
                if candidate > dp[m]:
                    dp[m] = candidate
                    first_cut[m] = i + 1

        pieces = []
        m = n
        while m > 0:
            pieces.append(first_cut[m])
            m -= first_cut[m]
        return dp[n], pieces
```

For the example it returns `(22, [2, 6])`.

## 7. Trace for `prices = [1, 5, 8, 9, 10, 17, 17, 20]`

The full table:

| m | dp[m] | pieces |
|---|---|---|
| 0 | 0 | none |
| 1 | 1 | 1 |
| 2 | 5 | 2 |
| 3 | 8 | 3 |
| 4 | 10 | 2 + 2 |
| 5 | 13 | 2 + 3 |
| 6 | 17 | 6 |
| 7 | 18 | 1 + 6 (2 + 2 + 3 also gives 18) |
| 8 | **22** | 2 + 6 |

Inside the last step, `dp[8]` tries every first piece and keeps the max:

| first piece | `prices[i]` | + best of the rest | total |
|---|---|---|---|
| 1 | 1 | `dp[7]` = 18 | 19 |
| 2 | 5 | `dp[6]` = 17 | **22** |
| 3 | 8 | `dp[5]` = 13 | 21 |
| 4 | 9 | `dp[4]` = 10 | 19 |
| 5 | 10 | `dp[3]` = 8 | 18 |
| 6 | 17 | `dp[2]` = 5 | **22** |
| 7 | 17 | `dp[1]` = 1 | 18 |
| 8 | 20 | `dp[0]` = 0 | 20 |

`2 + 6` and `6 + 2` are the same cut found from both ends.

## 8. Complexity

| Approach | Time | Space | Note |
|---|---|---|---|
| Plain recursion | O(2ⁿ) | O(n) stack | Too slow past n ≈ 25 |
| Memoization | O(n²) | O(n) memo + O(n) stack | `RecursionError` at n = 1000 by default |
| Tabulation | O(n²) | O(n) | Safe for any n |

## 9. The pattern: unbounded knapsack

Rod cutting is unbounded knapsack in disguise:

| Unbounded knapsack | Rod cutting |
|---|---|
| Item | A piece of length `i + 1` |
| Weight | `i + 1` |
| Value | `prices[i]` |
| Capacity `W` | Rod length `n` |
| Each item can be taken any number of times | Several pieces can have the same length |

```
knapsack:  dp[w] = max over items with weight <= w  of ( value     + dp[w - weight] )
rod:       dp[m] = max over i < m                   of ( prices[i] + dp[m - (i + 1)] )
```

**Why one dimension is enough:** after cutting a piece of length `k`, the rest of the rod may use length `k` again. So the state only needs to know how much rod is left. In 0/1 knapsack each item can be used once, so the state must also track which items remain: `dp[item][w]`.

Try this recurrence first whenever a problem says "pick options, repeats allowed, to fill a capacity".

## 10. Thinking checklist

1. Work small examples by hand and list every combination.
2. Find the pattern "one choice + the same problem, smaller".
3. Make one side of the choice a fixed value, so only the other side recurses.
4. Write the recurrence, then check indexing, `max`/`min`, and the base case.
5. Look for repeated subproblems in your own list of combinations, then memoize.
6. Convert to a bottom-up table if the recursion can go around 1000 levels deep in Python.
