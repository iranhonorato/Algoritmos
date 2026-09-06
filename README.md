# Algoritmos

Repositório pessoal de estudo de **estruturas de dados e algoritmos**. A ideia é treinar os
mesmos tipos de problema em linguagens diferentes, comparando como cada uma resolve a mesma
coisa — Python quando o foco é a lógica, C++ quando o foco é o que acontece embaixo (ponteiros,
memória, containers da STL).

Não é uma biblioteca nem um projeto com build: é um caderno de exercícios versionado. Cada
arquivo é autocontido e roda sozinho.

## Organização

O repositório é dividido em dois eixos: **linguagem** no primeiro nível, **tipo de estrutura ou
técnica** no segundo.

```
.
├── cpp/
│   ├── _sintaxe/        # notas de linguagem (não são problemas)
│   ├── backtracking/
│   ├── bst/
│   ├── grafos/
│   ├── linked list/
│   ├── slide window/
│   └── two pointers/
└── python/
    ├── backtracking/
    ├── bst/
    ├── grafos/
    ├── hash table/
    ├── linked list/
    ├── slide window/
    └── two pointers/
```

Os tópicos se espelham entre as linguagens de propósito: um problema resolvido em
`python/two pointers/` tem um lugar óbvio em `cpp/two pointers/` quando for a vez de refazê-lo
em C++. Quando um tópico ainda não existe do outro lado (hoje `hash table` só existe em Python),
é só criar a pasta na hora de escrever o primeiro exercício.

## Convenção de nomes

| Padrão | Significado |
| --- | --- |
| `00_intro.*` | Ponto de partida do tópico: definição da estrutura (`ListNode`, `Tree`, …) e operações básicas. |
| `<número>_<nome_do_problema>.*` | Solução de um problema. O número é o id do problema no LeetCode e o nome vai em `snake_case`. Ex.: `128_longest_consecutive_sequence.py`. |
| `_sintaxe/` | Pasta com `_` na frente para ficar no topo da listagem. Contém notas de linguagem numeradas na ordem de leitura (`01_print.cpp` → `09_stl.cpp`), não problemas. |

Problemas que não vêm do LeetCode ficam só com o nome descritivo, sem número
(ex.: `reverse_node_kth_group.py`).

As soluções em Python seguem o formato do próprio LeetCode — uma `class Solution` com o método
do enunciado — para poder colar direto na plataforma. Quando existe mais de uma abordagem para o
mesmo problema, cada uma vira um método com sufixo próprio (`reverseList_recursion`,
`reverseList_iterative`).

## Estado atual

| Tópico | Python | C++ |
| --- | --- | --- |
| linked list | intro + 3 problemas | — |
| hash table | 2 problemas | — |
| bst | intro | — |
| backtracking | — | — |
| grafos | — | — |
| slide window | — | — |
| two pointers | — | — |
| sintaxe da linguagem | — | 9 notas (`_sintaxe/`) |

## Como rodar

Python (sem dependências além da stdlib):

```bash
python3 "python/hash table/01_two_sum.py"
```

C++ (compila e executa um arquivo por vez):

```bash
g++ -std=c++17 -O2 -o /tmp/algo "cpp/_sintaxe/09_stl.cpp" && /tmp/algo
```

## Adicionando um problema novo

1. Escolha a pasta pelo par linguagem + tipo (`python/two pointers/`, `cpp/bst/`, …).
2. Nomeie o arquivo com o número e o nome do problema em `snake_case`.
3. Se for o primeiro problema daquele tópico na linguagem, comece pelo `00_intro` com a
   definição da estrutura — os arquivos de solução repetem essa definição para continuarem
   autocontidos.

## Nota sobre pastas vazias

O Git não versiona diretórios vazios, então os tópicos ainda sem nenhum arquivo não aparecem em
um clone novo. Eles são recriados naturalmente quando o primeiro exercício do tópico é
adicionado — ou, se quiser preservá-los desde já, basta colocar um `.gitkeep` dentro de cada um.
