# Cracking the Coding Interview

def verifica_palindromo(s:str) -> bool:
    s_clean = "".join([c.lower() for c in s if c.isalpha()])

    memo = {}

    for i in range(len(s_clean)):
        if s_clean[i] not in memo:
            memo[s_clean] = 1 

        else:
            memo.pop(s_clean[i])

    return len(s_clean) <= 1




