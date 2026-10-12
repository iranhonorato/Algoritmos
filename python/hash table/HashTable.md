# Hash Table

Uma **hash table** é uma estrutura de dados que guarda entradas em um array e usa a **chave** de cada entrada para calcular em qual posição desse array ela deve ficar. Como a posição é calculada (e não procurada), buscar, inserir e remover custam **O(1) em média**.

Ela é o mecanismo por trás de duas coleções muito usadas:

- **HashMap** (`dict` em Python): associa uma chave a um valor e permite encontrar o valor usando a chave.
- **HashSet** (`set` em Python): armazena elementos únicos e permite verificar rapidamente se um elemento está presente.

---

## 1. Da chave até a posição

```
chave  →  função hash  →  código hash  →  índice  →  slot (bucket) do array
"bia"                      123456         123456 mod 10 = 6      tabela[6]
```

1. A **função hash** transforma a chave em um número inteiro, o **código hash**.
2. O código hash é reduzido a um **índice válido** entre `0` e `m − 1`, em que `m` é o número de posições da tabela.
3. A tabela vai direto a esse índice para ler ou gravar a entrada.

Dois pontos que costumam confundir:

- O código hash **não é um endereço de memória**. Ele é só uma etapa intermediária para chegar a um índice do array interno.
- A redução para índice **nem sempre é `mod`**. O resto da divisão é o método mais comum, mas também existem a máscara de bits (quando `m` é potência de 2, basta pegar os bits finais do código) e o método da multiplicação. Alguns materiais chamam de "função hash" o caminho inteiro, da chave até o índice.

---

## 2. Colisões

Existem muito mais chaves possíveis do que posições na tabela, então chaves diferentes inevitavelmente acabam no mesmo índice. Isso é uma **colisão**, e é uma situação normal, não um erro.

Com `índice = chave mod 7`:

```
10 mod 7 = 3
17 mod 7 = 3
24 mod 7 = 3      → as três chaves disputam o índice 3
```

Uma colisão pode acontecer mesmo entre chaves com códigos hash diferentes: basta que os dois códigos sejam reduzidos ao mesmo índice.

### 2.1 Encadeamento (chaining)

Cada slot do array guarda uma **referência** (um ponteiro, uma "seta") para o primeiro nó de uma lista ligada. O slot não contém a lista inteira, só indica onde ela começa.

```
índice 0 → vazio
índice 1 → vazio
índice 2 → vazio
índice 3 → [chave: 10 | valor: "maçã" | próx] → [chave: 17 | valor: "banana" | próx] → fim
índice 4 → vazio
```

Cada nó guarda **a chave e o valor juntos**, além da ligação para o próximo nó. A seta entre os nós significa apenas "o próximo nó é este"; ela não significa que "maçã aponta para banana".

Busca pela chave `17`:

1. Calcula o índice: `17 mod 7 = 3`.
2. Vai ao slot 3 e segue a referência até o primeiro nó.
3. Compara a chave do nó com `17`. Não é (`10`), avança.
4. Encontra `17` e devolve o valor guardado **naquele mesmo nó**: `"banana"`.

A lista não precisa ser uma lista ligada: algumas implementações usam um array dinâmico ou até uma árvore em cada slot. O que importa é o slot conseguir guardar várias entradas.

### 2.2 Endereçamento aberto (open addressing)

Não há listas: todas as entradas ficam **dentro do próprio array**. Se o índice calculado já está ocupado por outra chave, a tabela segue uma regra (uma sequência de sondagem) para tentar outras posições, até achar a chave ou um slot livre.

```
inserir 10 → índice 3 livre      → grava em 3
inserir 17 → índice 3 ocupado    → tenta 4, livre → grava em 4
buscar 17  → olha 3 (é 10, não)  → olha 4 (é 17, achou)
```

O `dict` e o `set` do CPython usam endereçamento aberto.

### 2.3 Hash aponta, igualdade confirma

Nas duas estratégias, o hash só diz **onde começar a procurar**. Quem confirma que a entrada é a certa é a **comparação de igualdade** entre as chaves. Ter o mesmo hash não prova que duas chaves são iguais.

---

## 3. Complexidade

| Operação | Caso médio | Pior caso |
|----------|-----------|-----------|
| Buscar   | O(1)      | O(n)      |
| Inserir  | O(1) amortizado | O(n) |
| Remover  | O(1)      | O(n)      |

- **Caso médio O(1):** vale quando a função hash espalha bem as chaves e a tabela não está cheia demais, de modo que cada slot tem poucas entradas para comparar.
- **Pior caso O(n):** acontece se muitas chaves colidirem, porque a busca precisa comparar várias entradas uma a uma.
- A análise assume que calcular o hash e comparar chaves custa O(1). Para chaves grandes, como strings longas, esse custo depende do tamanho da chave.

### Fator de carga e redimensionamento

```
α = n / m        n = número de entradas, m = número de posições
```

Quanto maior o fator de carga `α`, mais colisões. Por isso, ao passar de um limite, a tabela **cresce** e redistribui todas as entradas no array maior (*rehash*). Esse redimensionamento custa O(n), mas acontece raramente, e diluído ao longo de muitas inserções o custo por inserção fica **O(1) amortizado**.

---

## 4. HashMap e HashSet

| | HashMap (`dict`) | HashSet (`set`) |
|---|---|---|
| O que guarda | pares chave → valor | elementos únicos |
| Pergunta típica | "qual valor está associado a esta chave?" | "este elemento está no conjunto?" |
| O que passa pela função hash | a chave | o próprio elemento |
| Duplicatas | chave repetida **substitui** o valor antigo | elemento repetido é ignorado |

O mecanismo interno (hash, índice, colisões) é o mesmo. No set, o elemento faz o papel da chave e não existe valor associado. Muitas implementações constroem o HashSet em cima de um HashMap, usando cada elemento como chave e um valor interno sem significado.

```python
# HashMap
idades = {"ana": 25, "bia": 30}
idades["caio"] = 19        # insere
idades["bia"] = 31         # atualiza: a chave "bia" continua única
idades["bia"]              # 31
idades.get("duda", 0)      # 0 (chave ausente, sem erro)
"ana" in idades            # True  → procura nas CHAVES
del idades["ana"]          # remove

# HashSet
vistos = {"ana", "bia"}
vistos.add("ana")          # nada muda: já existe
"bia" in vistos            # True
vistos.remove("bia")       # remove
```

---

## 5. Em Python: `in` em dict vs. em lista

```python
for x in array:
    if x in colecao:
        ...
```

| `colecao` é... | Custo de cada `in` | Custo do loop (n elementos) |
|---|---|---|
| `dict` ou `set` | O(1) em média | O(n) |
| `list` de tamanho m | O(m) | O(n · m), ou O(n²) se m = n |

- No `dict`/`set`, o `in` calcula o hash de `x`, vai à posição candidata e compara poucas entradas.
- Na `list` não há hash: Python compara elemento por elemento até achar ou chegar ao fim.

Esse é o motivo de tantos problemas trocarem uma busca em lista por um `set` ou `dict`: um loop O(n²) vira O(n), ao custo de O(n) de memória extra.

Atenção: `x in dicionario` procura **somente nas chaves**. Para procurar entre os valores é preciso `x in dicionario.values()`, que percorre tudo e custa O(n).

---

## 6. Regras para as chaves

- **Chaves iguais precisam ter o mesmo hash.** Caso contrário, a tabela procuraria a mesma chave em lugares diferentes. O inverso não é exigido: chaves diferentes podem ter o mesmo hash (colisão).
- **Uma chave não pode mudar depois de inserida.** Se mudasse, seu hash mudaria e a tabela continuaria procurando no índice antigo. Por isso, Python só aceita como chave (ou elemento de set) objetos *hashable*, em geral imutáveis:

```python
d = {(1, 2): "ok"}     # tupla: pode
d = {[1, 2]: "erro"}   # TypeError: unhashable type: 'list'
```

---

## 7. Dúvidas frequentes

**O código hash aponta para onde?**
Para lugar nenhum diretamente. Ele é um número que ainda precisa ser reduzido a um índice do array interno. É esse índice que indica o slot a consultar.

**A hash table é um array?**
Ela é organizada sobre um array de slots. No encadeamento, cada slot guarda uma referência para uma lista de entradas; no endereçamento aberto, as entradas ficam nos próprios slots.

**A chave é armazenada ou só serve para calcular a posição?**
É armazenada, junto com o valor. Sem a chave guardada, a tabela não teria como distinguir duas entradas que colidiram no mesmo índice.

**Com colisão, como a tabela sabe qual valor é de qual chave?**
Cada entrada guarda seu próprio par chave–valor. A busca compara a chave procurada com a chave de cada entrada e devolve o valor da entrada que bater.

**O set "mapeia um valor para ele mesmo"?**
É melhor pensar que o set guarda só elementos, e que o elemento faz o papel da chave. Não há valor associado.

**Hash table, HashMap e HashSet são a mesma coisa?**
Não. Hash table é a estrutura (o mecanismo de array + hash + tratamento de colisão). HashMap e HashSet são coleções implementadas com ela. Na prática os nomes se misturam, e muita gente diz "hash table" querendo dizer o próprio mapa.

**`chave in dicionario` percorre o dicionário inteiro?**
Não. Calcula o hash da chave, vai à posição candidata e, se houver colisão, examina algumas posições vizinhas. Devolve `True` ao encontrar a chave e `False` ao concluir que ela não está lá.

**Se é O(1), por que se fala em O(n)?**
O(1) é o caso médio, que depende de boa distribuição dos hashes. O(n) é o pior caso teórico, com muitas colisões. Com as funções hash padrão de Python, ele é raro na prática.

**O dict mantém ordem?**
Desde o Python 3.7, o `dict` preserva a ordem de inserção. O `set` não garante ordem nenhuma. Nenhum dos dois fica ordenado pelo valor das chaves.

**Quando não usar hash table?**
Quando é preciso manter os dados ordenados, buscar por intervalo (todas as chaves entre `a` e `b`) ou achar o mínimo/máximo com frequência. Nesses casos, árvores de busca balanceadas ou heaps são mais adequados.

---

## 8. Resumo

1. A chave passa pela função hash e vira um índice do array interno.
2. Chaves diferentes podem cair no mesmo índice: isso é uma colisão.
3. Colisões são resolvidas com encadeamento (lista por slot) ou endereçamento aberto (outra posição do array).
4. O hash indica onde procurar; a comparação de igualdade confirma a entrada.
5. Busca, inserção e remoção custam O(1) em média e O(n) no pior caso.
6. HashMap associa chave a valor; HashSet guarda elementos únicos.
