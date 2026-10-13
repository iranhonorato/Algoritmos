# Aula completa: Linked List

## **Definição:**

Uma Linked List (lista ligada ou lista encadeada) é uma estrutura de dados linear formada por nós. Cada nó guarda um valor e uma referência para o próximo nó da sequência. Os nós não precisam ocupar posições vizinhas na memória: a ordem da lista é dada pelas referências, e não pela posição física dos elementos. Isso permite inserir e remover elementos em tempo constante quando já se tem o nó certo em mãos, ao custo de perder o acesso direto por índice.

## 1. A ideia geral

Imagine uma caça ao tesouro: cada pista contém uma informação e diz onde está a próxima pista. Você não consegue ir direto à quinta pista; precisa começar pela primeira e seguir as indicações uma a uma.

Uma **linked list** funciona assim:

    head → [1] → [2] → [3] → None

Compare com um array, em que os elementos ficam lado a lado e a posição de cada um é calculada pelo índice:

    array:        [ 1 | 2 | 3 ]        posições vizinhas, acesso direto por índice
    linked list:  [1] → [2] → [3]      nós espalhados, ligados por referências

O array chega a qualquer posição imediatamente, mas inserir no meio obriga a deslocar os elementos seguintes. A linked list faz o contrário: chegar a uma posição exige caminhar, mas inserir ou remover é só ajustar referências.

## 2. O nó: valor e referência

O bloco básico da lista é o **nó**. Ele guarda duas coisas:

- o **valor** armazenado;
- uma **referência** para o próximo nó.

Em Python:

    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

Montando a lista 1 → 2 → 3:

    head = ListNode(1, ListNode(2, ListNode(3)))

A referência é uma ligação, uma seta: o nó não contém o próximo nó dentro dele, apenas indica onde ele está.

    [val: 1 | next] → [val: 2 | next] → [val: 3 | next: None]

Dois nomes aparecem o tempo todo:

- **head**: a referência para o primeiro nó. É por ela que se entra na lista.
- **None**: o valor de `next` no último nó. Indica o fim da lista. Uma lista vazia é simplesmente `head = None`.

> A lista inteira é acessada a partir do head. Quem perde a referência do head perde a lista.

## 3. Percorrendo a lista

Para visitar os elementos, usamos uma variável auxiliar que começa no head e avança de nó em nó até chegar a None:

    node = head
    while node is not None:
        print(node.val)
        node = node.next

Usamos `node`, e não o próprio `head`, para não perder a referência do início da lista.

Quase toda operação em linked list é uma variação desse laço.

## 4. Operações básicas

### 4.1 Acessar o elemento da posição i

Não existe `lista[i]`. É preciso partir do head e avançar `i` vezes:

    node = head
    for _ in range(i):
        node = node.next

Custo: O(n) no pior caso.

### 4.2 Buscar um valor

Percorre-se a lista comparando o valor de cada nó. Custo: O(n).

### 4.3 Inserir

Inserir é criar um nó e ajustar referências. Nenhum outro elemento precisa ser deslocado.

**No início**, o novo nó aponta para o antigo head e passa a ser o head:

    head = ListNode(0, head)

    antes:   head → [1] → [2] → [3]
    depois:  head → [0] → [1] → [2] → [3]

**Depois de um nó conhecido** (`prev`), a ordem das atribuições importa:

    novo = ListNode(9)
    novo.next = prev.next    # 1º: o novo nó aponta para o resto da lista
    prev.next = novo         # 2º: o anterior passa a apontar para o novo

    antes:   [1] → [2] → [3]
    depois:  [1] → [9] → [2] → [3]      (prev é o nó 1)

Se a ordem for invertida, `prev.next` é sobrescrito antes de ser copiado e o resto da lista se perde.

**No fim**, é preciso caminhar até o último nó, o que custa O(n). Se a lista mantiver também uma referência **tail** para o último nó, inserir no fim passa a custar O(1).

### 4.4 Remover

Remover um nó é fazer o nó anterior "pular" o nó removido:

    prev.next = prev.next.next

    antes:   [1] → [2] → [3]
    depois:  [1] --------→ [3]      (o nó 2 ficou sem ninguém apontando para ele)

Em Python, não é preciso apagar o nó manualmente: quando nenhuma referência aponta mais para ele, a memória é liberada pelo coletor de lixo.

Note que a remoção precisa do nó **anterior**. Em uma lista simples, um nó não sabe quem vem antes dele.

## 5. Tipos de linked list

| Tipo | Cada nó guarda | Característica |
|---|---|---|
| Simples (singly) | valor + `next` | Só anda para frente |
| Dupla (doubly) | valor + `next` + `prev` | Anda nos dois sentidos; remove um nó sem precisar buscar o anterior |
| Circular | o último nó aponta para o primeiro | Não tem None no fim; exige cuidado para não percorrer para sempre |

A lista dupla gasta uma referência a mais por nó e exige atualizar duas ligações em cada inserção ou remoção.

    simples:   [1] → [2] → [3] → None
    dupla:     None ← [1] ⇄ [2] ⇄ [3] → None
    circular:  [1] → [2] → [3] → (volta ao 1)

## 6. Complexidade: linked list comparada a array

| Operação | Linked list simples | Array (list em Python) |
|---|---:|---:|
| Acessar a posição i | O(n) | O(1) |
| Buscar um valor | O(n) | O(n) |
| Inserir/remover no início | O(1) | O(n) |
| Inserir no fim | O(n), ou O(1) com tail | O(1) amortizado |
| Inserir/remover depois de um nó já conhecido | O(1) | O(n) |

Aqui, n é o número de elementos.

### Por que inserir é O(1) se chegar ao nó é O(n)?

São duas etapas diferentes. **Chegar** à posição custa O(n), porque exige caminhar. **Inserir ou remover**, uma vez no lugar, custa O(1), porque só ajusta referências. O ganho real aparece quando o algoritmo já está no nó certo, por exemplo durante um percurso, ou quando trabalha sempre nas pontas.

### E a memória?

Cada nó guarda uma referência além do valor, então a lista ligada usa mais memória por elemento do que um array. Além disso, como os nós ficam espalhados, percorrê-la costuma ser mais lento na prática do que percorrer um array do mesmo tamanho.

## 7. Técnicas comuns em problemas

### Nó sentinela (dummy)

Inserir ou remover o primeiro nó é um caso especial, porque ele não tem anterior. Um nó falso colocado antes do head elimina esse caso: todo nó real passa a ter um anterior.

    def remove(head, val):
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next is not None:
            if prev.next.val == val:
                prev.next = prev.next.next
                break
            prev = prev.next
        return dummy.next

O retorno é `dummy.next`, e não `head`, porque o head original pode ter sido justamente o nó removido.

### Dois ponteiros (rápido e lento)

Dois ponteiros percorrem a lista em velocidades diferentes. Com o lento andando um nó e o rápido andando dois, quando o rápido chega ao fim o lento está no meio:

    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

A mesma ideia detecta ciclos: se a lista tiver um ciclo, o ponteiro rápido acaba alcançando o lento.

### Inversão de referências

Inverter uma lista é percorrê-la fazendo cada nó apontar para o anterior, em vez do próximo. Como isso apaga a ligação com o resto da lista, é preciso guardar o próximo nó em uma variável **antes** de alterar `next`.

    antes:   None    [1] → [2] → [3] → None
    depois:  None ← [1] ← [2] ← [3]

### Recursão

Uma lista ligada é naturalmente recursiva: ela é ou vazia (None), ou um nó seguido de outra lista. Por isso muitos problemas têm soluções recursivas curtas, com `node is None` como caso base. O custo é a pilha de chamadas, que cresce O(n).

## 8. Linked list em Python

A **list** do Python **não** é uma linked list. Ela é um array dinâmico: tem acesso por índice em O(1) e inserção no início em O(n).

Python não tem uma classe de linked list simples pronta. Em problemas de entrevista, ela é montada com uma classe de nó como a `ListNode` acima.

Quando o objetivo é inserir e remover nas duas pontas em O(1), a coleção indicada é **collections.deque**:

    from collections import deque

    fila = deque([1, 2, 3])
    fila.appendleft(0)   # insere no início em O(1)
    fila.append(4)       # insere no fim em O(1)
    fila.popleft()       # remove do início em O(1)

## 9. Cuidados importantes

### Verificar None antes de acessar atributos

Acessar `node.next` ou `node.val` quando `node` é None gera `AttributeError`. A ordem dos testes importa, porque o `and` e o `or` param no primeiro resultado decisivo:

    if node is None or node.next is None:    # correto: testa node primeiro
    if node.next is None or node is None:    # erro se node for None

### Não perder referências

Ao alterar um `next`, a ligação antiga deixa de existir. Se ela era o único caminho até o resto da lista, esse resto se perde. Guarde em uma variável o que for necessário antes de sobrescrever.

### Casos de borda

Sempre teste mentalmente: lista vazia, lista com um único nó, e operação no primeiro e no último nó.

## 10. Dúvidas comuns respondidas

### O nó guarda o próximo nó dentro dele?

Não. Ele guarda uma referência, isto é, uma indicação de onde o próximo nó está. Os nós são objetos separados na memória.

### O que é o head? É um nó especial?

É apenas uma variável que referencia o primeiro nó. O primeiro nó é um nó comum.

### Se eu fizer node = node.next, estou alterando a lista?

Não. Isso só muda para onde a variável `node` aponta. A lista só é alterada quando se atribui a um atributo, como em `node.next = outro`.

### Duas variáveis podem apontar para o mesmo nó?

Sim. Depois de `a = head`, tanto `a` quanto `head` referenciam o mesmo objeto. Alterar `a.val` altera o nó visto por `head`.

### Por que não usar sempre um array?

Na maioria dos casos, o array é mesmo a melhor escolha. A linked list compensa quando há muitas inserções e remoções nas pontas ou em posições já alcançadas, e quando não se precisa de acesso por índice. Ela também é a base de outras estruturas, como filas, pilhas e o encadeamento de uma hash table.

### Como sei o tamanho da lista?

Percorrendo e contando, o que custa O(n), a menos que a implementação mantenha um contador atualizado a cada inserção e remoção.

### Dá para fazer busca binária em uma linked list?

Não de forma eficiente. A busca binária depende de saltar direto ao elemento do meio, e na linked list chegar ao meio já custa O(n).

## 11. Resumo final

1. Uma linked list é uma sequência de nós; cada nó guarda um valor e uma referência para o próximo.
2. O head referencia o primeiro nó; o último nó aponta para None.
3. Os nós não ficam em posições vizinhas da memória; a ordem vem das referências.
4. Não há acesso por índice: chegar à posição i custa O(n).
5. Inserir e remover custam O(1) quando já se tem o nó anterior, pois basta ajustar referências.
6. A lista dupla guarda também o nó anterior; a circular liga o último ao primeiro.
7. Nó sentinela, dois ponteiros e inversão de referências resolvem grande parte dos problemas.
8. Em Python, list é um array dinâmico; para inserções rápidas nas duas pontas, use collections.deque.
9. Verifique None antes de acessar atributos e guarde as referências antes de sobrescrevê-las.
