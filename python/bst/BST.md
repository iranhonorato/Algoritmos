# Aula completa: Binary Search Tree (BST)

## **Definição:**

Uma Binary Search Tree (árvore binária de busca) é uma estrutura de dados hierárquica em que cada nó guarda um valor e tem no máximo dois filhos, um à esquerda e um à direita. Ela obedece a uma regra de ordenação: todos os valores da subárvore esquerda de um nó são menores que o valor dele, e todos os da subárvore direita são maiores. Essa regra permite descartar metade da árvore a cada comparação, o que torna busca, inserção e remoção proporcionais à altura da árvore.

## 1. A ideia geral

Imagine procurar uma palavra em um dicionário de papel. Você abre no meio, vê se a palavra procurada vem antes ou depois, e descarta a metade que não interessa. Repetindo isso, chega à palavra em poucas etapas.

Uma **BST** organiza os dados para que essa mesma decisão — "é menor ou é maior?" — possa ser tomada em cada nó:

            5
          /   \
         3     7
        / \   / \
       1   4 6   8

Para procurar o 6: ele é maior que 5, então vamos para a direita; é menor que 7, então vamos para a esquerda; encontramos o 6. Foram três comparações em uma árvore de sete elementos.

Diferentemente de um array ordenado, a BST mantém os dados ordenados e ainda aceita inserções e remoções sem deslocar elementos.

## 2. Vocabulário de árvores

| Termo | Significado |
|---|---|
| Nó | Elemento da árvore; guarda um valor e as referências para os filhos |
| Raiz (root) | O nó do topo; é por ele que se entra na árvore |
| Filho / pai | Um nó ligado diretamente abaixo / acima de outro |
| Folha | Nó sem filhos |
| Subárvore | Um nó junto com todos os seus descendentes |
| Altura (h) | Número de ligações no caminho mais longo da raiz até uma folha |

Na árvore acima, 5 é a raiz; 1, 4, 6 e 8 são folhas; a subárvore esquerda de 5 é formada por 3, 1 e 4; e a altura é 2.

Em Python, o nó é parecido com o de uma linked list, mas com duas referências em vez de uma:

    class Tree:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    root = Tree(5,
                Tree(3, Tree(1), Tree(4)),
                Tree(7, Tree(6), Tree(8)))

Um filho ausente é representado por None. Uma árvore vazia é `root = None`.

## 3. A propriedade que define uma BST

Para **todo** nó da árvore:

- todos os valores da subárvore **esquerda** são **menores** que o valor do nó;
- todos os valores da subárvore **direita** são **maiores** que o valor do nó.

A regra vale para a subárvore inteira, e não apenas para os filhos diretos. Esta árvore **não** é uma BST:

            5
          /   \
         3     7
        / \
       1   6

O 6 é maior que seu pai, 3, e está à direita dele, o que parece correto. Mas ele está na subárvore esquerda do 5 e é maior que 5. Uma busca pelo 6 iria para a direita do 5 e nunca o encontraria.

> Árvore binária é qualquer árvore com no máximo dois filhos por nó. BST é a árvore binária que, além disso, respeita a regra de ordenação.

## 4. Buscar um valor

A cada nó, comparamos o valor procurado com o valor do nó e escolhemos um lado. O outro lado inteiro é descartado.

1. Começar na raiz.
2. Se o nó for None, o valor não está na árvore.
3. Se o valor for igual ao do nó, encontramos.
4. Se for menor, continuar pela esquerda; se for maior, pela direita.

Em Python:

    def search(node, val):
        while node is not None and node.val != val:
            node = node.left if val < node.val else node.right
        return node

Buscando o 4 na árvore da seção 1:

    4 < 5  → esquerda
    4 > 3  → direita
    4 == 4 → encontrado

O número de comparações é, no máximo, a altura da árvore mais um.

## 5. Inserir um valor

A inserção é uma busca que não encontra o valor: descemos comparando até chegar a uma posição vazia (None) e colocamos o novo nó ali. Todo nó novo entra como **folha**.

    def insert(node, val):
        if node is None:
            return Tree(val)
        if val < node.val:
            node.left = insert(node.left, val)
        elif val > node.val:
            node.right = insert(node.right, val)
        return node

Inserindo o 2:

    2 < 5 → esquerda;  2 < 3 → esquerda;  2 > 1 → direita, que está vazia

            5
          /   \
         3     7
        / \   / \
       1   4 6   8
        \
         2

A função devolve o nó para que o pai consiga ligar o filho recém-criado: `node.left = insert(node.left, val)`.

## 6. Remover um valor

A remoção tem três casos, conforme o número de filhos do nó removido.

**Caso 1: o nó é uma folha.** Basta desligá-lo do pai.

**Caso 2: o nó tem um filho.** O filho sobe e ocupa o lugar do nó removido.

    remover 1 (que tem só o filho 2):

         3              3
        / \            / \
       1   4    →     2   4
        \
         2

**Caso 3: o nó tem dois filhos.** Não dá para simplesmente retirá-lo, pois sobrariam duas subárvores soltas. A solução é:

1. Encontrar o **sucessor**: o menor valor da subárvore direita (descer à direita uma vez e depois sempre à esquerda).
2. Copiar o valor do sucessor para o nó que seria removido.
3. Remover o sucessor de sua posição original. Ele não tem filho esquerdo, então cai no caso 1 ou 2.

Exemplo:

    remover 5 (dois filhos): o sucessor é o 6

            5                  6
          /   \              /   \
         3     7      →     3     7
        / \   / \          / \     \
       1   4 6   8        1   4     8

O sucessor funciona porque é maior que tudo à esquerda e menor que todo o restante à direita, então a propriedade da BST continua valendo. Também se pode usar o **predecessor**, o maior valor da subárvore esquerda.

## 7. Travessias: como percorrer a árvore

Percorrer é visitar todos os nós. A diferença entre as travessias em profundidade é o momento em que o nó é visitado em relação aos filhos.

| Travessia | Ordem | Resultado na árvore da seção 1 |
|---|---|---|
| Pre-order | nó, esquerda, direita | 5, 3, 1, 4, 7, 6, 8 |
| In-order | esquerda, nó, direita | 1, 3, 4, 5, 6, 7, 8 |
| Post-order | esquerda, direita, nó | 1, 4, 3, 6, 8, 7, 5 |
| Em largura (BFS) | nível por nível | 5, 3, 7, 1, 4, 6, 8 |

A **in-order** é a mais importante em uma BST: ela visita os valores em **ordem crescente**.

    def in_order(node):
        if node is None:
            return
        in_order(node.left)
        print(node.val)
        in_order(node.right)

Para as outras duas, basta mudar a posição do `print`. A travessia em largura usa uma fila em vez de recursão.

Todas visitam cada nó uma vez e custam O(n).

## 8. Mínimo, máximo e consultas por ordem

A ordenação da árvore dá algumas consultas quase de graça:

- **Mínimo:** partir da raiz e descer sempre para a esquerda.
- **Máximo:** partir da raiz e descer sempre para a direita.
- **Valores em um intervalo:** fazer uma travessia in-order ignorando as subárvores que estão fora do intervalo.

Código do mínimo:

    def minimum(node):
        while node.left is not None:
            node = node.left
        return node

## 9. Complexidade: tudo depende da altura

Busca, inserção e remoção descem por um único caminho da raiz em direção às folhas. O custo é, portanto, proporcional à altura h da árvore.

| Operação | Árvore balanceada | Pior caso (degenerada) |
|---|---:|---:|
| Buscar | O(log n) | O(n) |
| Inserir | O(log n) | O(n) |
| Remover | O(log n) | O(n) |
| Mínimo / máximo | O(log n) | O(n) |
| Percorrer tudo | O(n) | O(n) |

Aqui, n é o número de nós.

### Por que O(log n) na árvore balanceada?

Em uma árvore balanceada, cada nível tem cerca do dobro de nós do nível anterior. Com isso, n nós cabem em aproximadamente log₂ n níveis. Um milhão de valores ocupam cerca de 20 níveis, então uma busca faz cerca de 20 comparações.

### Por que o pior caso é O(n)?

A forma da árvore depende da **ordem de inserção**. Inserindo 1, 2, 3, 4, 5 nessa ordem, cada valor é maior que todos os anteriores e vai sempre para a direita:

    1
     \
      2
       \
        3
         \
          4
           \
            5

A árvore virou, na prática, uma linked list. A altura é n − 1 e a busca não descarta nada a cada passo. Essa árvore é chamada de **degenerada**.

### E a memória?

A estrutura ocupa O(n). As versões recursivas das operações usam ainda O(h) de pilha de chamadas.

## 10. Árvores balanceadas

Para evitar o pior caso, existem BSTs **auto-balanceadas**, como a **AVL** e a **rubro-negra** (red-black). Elas reorganizam os nós por meio de rotações durante as inserções e remoções, mantendo a altura em O(log n). Com isso, as operações são O(log n) também no pior caso.

Uma BST simples, sem balanceamento, só garante O(log n) se os dados chegarem em ordem razoavelmente aleatória.

## 11. BST, hash table e array ordenado comparados

| Característica | BST balanceada | Hash table | Array ordenado |
|---|---|---|---|
| Buscar | O(log n) | O(1) em média | O(log n) com busca binária |
| Inserir / remover | O(log n) | O(1) em média | O(n) |
| Mantém os dados ordenados | Sim | Não | Sim |
| Mínimo / máximo | O(log n) | O(n) | O(1) |
| Busca por intervalo | Eficiente | Precisa percorrer tudo | Eficiente |

A hash table é mais rápida para perguntar "este valor existe?". A BST compensa quando a **ordem** importa: percorrer em ordem, achar o menor valor maior que x, ou listar tudo entre a e b.

## 12. BST em Python

Python não tem uma BST na biblioteca padrão. Em problemas de entrevista, a árvore é montada com uma classe de nó como a `Tree` acima.

Para manter dados ordenados no dia a dia, as alternativas são:

- o módulo **bisect**, que faz busca binária em uma list ordenada (a busca é O(log n), mas a inserção é O(n) por deslocar elementos);
- a biblioteca externa **sortedcontainers** (`SortedList`, `SortedDict`).

Exemplo com bisect:

    import bisect

    valores = [1, 3, 4, 7]
    bisect.insort(valores, 5)            # [1, 3, 4, 5, 7]
    i = bisect.bisect_left(valores, 4)   # 2: posição do 4

## 13. Dúvidas comuns respondidas

### Basta cada nó ser maior que o filho esquerdo e menor que o direito?

Não. A regra vale para todas as subárvores, não só para os filhos diretos. Para validar uma BST, cada nó precisa estar dentro de um intervalo herdado dos seus ancestrais:

    def is_bst(node, low=float("-inf"), high=float("inf")):
        if node is None:
            return True
        if not (low < node.val < high):
            return False
        return (is_bst(node.left, low, node.val) and
                is_bst(node.right, node.val, high))

Outra forma é verificar se a travessia in-order produz valores estritamente crescentes.

### A BST aceita valores repetidos?

Depende da convenção. Na definição mais comum, não: os valores são únicos. Quando repetições são permitidas, define-se que elas vão sempre para o mesmo lado, ou guarda-se um contador em cada nó.

### Os mesmos valores sempre formam a mesma árvore?

Não. A forma depende da ordem de inserção. Inserir 5, 3, 7 gera uma árvore balanceada; inserir 3, 5, 7 gera uma árvore inclinada para a direita. As duas são BSTs válidas com os mesmos valores.

### A raiz precisa ser o valor do meio?

Não. A raiz é simplesmente o primeiro valor inserido (em uma BST sem balanceamento). A árvore só fica equilibrada se a raiz estiver perto da mediana.

### Qual a diferença entre BST e heap?

As duas são árvores binárias, mas com regras diferentes. Na BST, a ordem é entre esquerda e direita, e ela permite buscar qualquer valor. No heap, a ordem é só entre pai e filhos (o pai é menor, ou maior, que ambos), e ele serve para obter rapidamente o mínimo ou o máximo, não para buscar valores arbitrários.

### Devo usar recursão ou laço?

As duas formas funcionam. A recursão combina com a estrutura da árvore, pois cada subárvore é também uma árvore, e costuma dar código mais curto. O laço evita o uso da pilha de chamadas, o que importa em árvores muito altas: Python limita a profundidade da recursão a cerca de 1000 chamadas por padrão.

### Por que usar BST se a hash table busca em O(1)?

Porque a hash table não mantém ordem. Se o problema pede o menor elemento, o próximo valor maior que x ou os elementos de um intervalo, a hash table precisa examinar tudo, enquanto a BST responde seguindo um caminho.

## 14. Resumo final

1. Uma BST é uma árvore binária em que, para todo nó, a subárvore esquerda tem valores menores e a direita tem valores maiores.
2. A regra vale para subárvores inteiras, não apenas para os filhos diretos.
3. A busca compara o valor com o nó e descarta um dos lados a cada passo.
4. A inserção desce como uma busca e coloca o novo nó como folha.
5. A remoção tem três casos; com dois filhos, o nó recebe o valor do seu sucessor.
6. A travessia in-order visita os valores em ordem crescente.
7. Busca, inserção e remoção custam O(h), em que h é a altura da árvore.
8. Em uma árvore balanceada, h é O(log n); em uma árvore degenerada, h é O(n).
9. A forma da árvore depende da ordem de inserção; árvores AVL e rubro-negras se reequilibram para garantir O(log n).
10. A hash table é melhor para testar pertencimento; a BST é melhor quando a ordem dos dados importa.
