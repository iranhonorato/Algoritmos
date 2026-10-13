# Aula completa: Hash Table, HashMap e HashSet

## **Definição:** 

Uma Hash Table é uma estrutura de dados que utiliza uma função Hash para converter uma chave (que pode ser um identificador ou o próprio elemento) em um endereço de memória. Isso permite armazenar e recuperar dados de forma dispersa com acesso direto em tempo constante, seja associando essa chave a um valor externo (como nos dicionários) ou usando o próprio elemento como chave (como nos conjuntos).

## 1. A ideia geral

Imagine que você guarda nomes e idades:

- Ana → 25
- Bia → 30
- Caio → 19

Você quer encontrar rapidamente a idade de alguém pelo nome. Uma solução simples seria olhar os nomes um por um até encontrar o procurado. Isso funciona, mas pode exigir muitas comparações.

Uma **Hash Table** (tabela hash) usa a chave — neste exemplo, o nome — para calcular uma posição inicial em uma tabela. Assim, em vez de começar examinando todos os dados, ela vai diretamente a uma região onde espera encontrar a entrada.

A ideia é:

    chave → função hash → código hash → índice → posição candidata na tabela

Essa posição é candidata porque pode haver colisões. A tabela ainda precisa confirmar que encontrou a chave certa.

> A tabela hash não necessariamente calcula um endereço físico de memória. Ela calcula um índice interno, como a posição 6 de um array.

## 2. Do início ao fim: como a chave leva à posição

Vamos dividir o processo em etapas.

### Etapa 1: temos uma chave

A chave é a informação usada para localizar uma entrada. Pode ser um número, uma string, uma tupla ou outro objeto que possa ser usado como chave.

Exemplo: a chave é 17.

### Etapa 2: a função hash calcula um código hash

Uma **função hash** transforma a chave em um número inteiro chamado **código hash**.

    chave 17 → função hash → código hash

O código hash não é, por si só, o endereço da entrada. Ele é um resultado intermediário.

### Etapa 3: o código hash é convertido em um índice válido

Se a tabela tem m posições, os índices precisam estar entre 0 e m − 1. Uma técnica didática comum é usar o resto da divisão:

    índice = código hash mod m

Por exemplo, se o código hash fosse 123456 e a tabela tivesse 10 posições:

    123456 mod 10 = 6

O índice calculado seria 6.

O módulo é uma forma de obter o índice, mas não é a única. Implementações podem usar outras formas de reduzir o código hash a um índice válido, como máscaras de bits ou métodos baseados em multiplicação.

Alguns materiais usam “função hash” para se referir ao processo completo, da chave até o índice. Outros explicam separadamente o código hash e sua conversão em índice.

### Etapa 4: a tabela consulta a posição candidata

A tabela acessa o slot, também chamado de **bucket**, correspondente ao índice calculado. Se encontrar ali a chave procurada, termina. Se encontrar outra chave ou uma colisão, aplica uma estratégia de resolução.

## 3. O que é uma colisão?

Uma **colisão** acontece quando duas chaves diferentes acabam direcionadas ao mesmo índice da tabela.

Isso é inevitável em geral: o conjunto de chaves possíveis costuma ser muito maior que o número de posições disponíveis. Várias chaves precisam compartilhar as posições da tabela.

Considere, para simplificar, uma tabela com 7 posições e a regra:

    índice = chave mod 7

Então:

    10 mod 7 = 3
    17 mod 7 = 3
    24 mod 7 = 3

As três chaves chegam ao índice 3.

Uma colisão também pode ocorrer entre códigos hash diferentes: basta que, ao serem convertidos em índices, ambos resultem no mesmo índice.

**Ter o mesmo hash não significa que duas chaves são iguais.** O hash ajuda a direcionar a busca; a comparação de igualdade confirma qual chave foi encontrada.

## 4. Como resolver colisões?

Há diferentes estratégias. Duas importantes são o encadeamento e o endereçamento aberto.

### 4.1 Encadeamento (chaining)

No encadeamento, cada posição da tabela guarda uma referência — pense em uma seta ou ponteiro — para uma coleção de entradas que chegaram àquela posição. Na explicação clássica, essa coleção é uma lista ligada.

Para um mapa, cada nó guarda a chave e o valor juntos, além da ligação para o próximo nó:

    array[3]
       |
       v
    [chave: 10 | valor: "maçã" | próximo]
       |
       v
    [chave: 17 | valor: "banana" | próximo: fim]

A seta entre os nós significa “o próximo nó da lista está aqui”. Ela não significa que “maçã aponta para banana”. Cada nó tem seu próprio par chave–valor.

A posição do array não guarda a lista inteira dentro dela. Ela guarda uma referência ao primeiro nó da lista.

Uma busca pela chave 17 funciona assim:

1. Calcular o índice: 17 mod 7 = 3.
2. Acessar a posição 3.
3. Seguir sua referência até o primeiro nó.
4. Comparar a chave do primeiro nó, 10, com 17. Não são iguais.
5. Seguir para o próximo nó.
6. Comparar a chave seguinte, 17, com a chave procurada. São iguais.
7. Devolver o valor desse mesmo nó: "banana".

A lista ligada é uma estratégia clássica; outras implementações podem usar outras coleções em cada posição.

### 4.2 Endereçamento aberto (open addressing)

No endereçamento aberto, todas as entradas ficam nos próprios slots do array. Se o índice calculado estiver ocupado por outra chave, a tabela segue uma sequência de posições candidatas, chamada **sequência de sondagem**, até encontrar a chave ou uma posição livre.

Exemplo simplificado com sondagem linear:

    inserir 10 → índice 3 livre       → grava em 3
    inserir 17 → índice 3 ocupado     → tenta 4, livre → grava em 4
    buscar 17  → olha 3: encontra 10  → tenta 4: encontra 17

O exemplo mostra apenas a ideia. As regras exatas de sondagem variam entre implementações.

O dict e o set do CPython resolvem colisões por endereçamento aberto. Portanto, em Python, não imagine necessariamente uma lista ligada em cada posição.

## 5. HashMap: associação entre chave e valor

Um **HashMap** é uma coleção que associa cada chave a um valor.

    chave → valor
    "ana" → 25
    "bia" → 30

Com ele, podemos perguntar:

> Qual valor está associado à chave "bia"?

A tabela usa a chave para localizar a entrada. Quando encontra a chave, obtém o valor que está associado a ela.

Operações comuns de um mapa são:

- inserir uma associação;
- consultar o valor pela chave;
- verificar se uma chave existe;
- atualizar o valor associado;
- remover uma associação.

Em Python, a coleção correspondente é o **dict**. O nome da classe nativa é dict; “hash map” é uma descrição da estrutura e do comportamento.

No Python:

    idades = {"ana": 25, "bia": 30}

    idades["caio"] = 19       # insere uma nova chave e valor
    idades["bia"] = 31        # atualiza o valor associado a "bia"
    idade = idades["bia"]     # obtém 31
    existe = "ana" in idades  # True: verifica as chaves
    del idades["ana"]         # remove a associação

Cada chave é única. Se atribuirmos um novo valor à chave "bia", o valor anterior é substituído; não surge uma segunda entrada com a mesma chave.

## 6. HashSet: conjunto de elementos únicos

Um **HashSet** é uma coleção que guarda elementos sem associar a cada um um valor separado. Seu uso comum é verificar rapidamente se um elemento está presente, mantendo os elementos únicos.

    {"ana", "bia", "caio"}

No conjunto, o próprio elemento faz o papel da chave usada na busca. Não há um valor associado separado, como há em um HashMap.

Em Python, a coleção correspondente é **set**:

    vistos = {"ana", "bia"}

    vistos.add("caio")        # adiciona
    vistos.add("ana")         # não cria uma segunda "ana"
    existe = "bia" in vistos  # True
    vistos.remove("bia")      # remove

É útil pensar no set como uma tabela que usa o próprio elemento para calcular onde procurar. Algumas implementações constroem um HashSet internamente sobre um HashMap, usando um valor interno sem significado para quem usa o conjunto.

## 7. HashMap e HashSet comparados

| Característica | HashMap (dict em Python) | HashSet (set em Python) |
|---|---|---|
| O que guarda | Pares chave–valor | Elementos únicos |
| O que é usado no hash | A chave | O próprio elemento |
| Pergunta típica | “Qual valor corresponde a esta chave?” | “Este elemento está no conjunto?” |
| Repetição | Uma chave repetida atualiza/substitui seu valor | Um elemento repetido não cria uma cópia |
| Exemplo | "bia" → 30 | {"ana", "bia"} |

O mecanismo de hashing pode ser parecido, mas a finalidade das coleções é diferente.

## 8. Como funciona a expressão x in dicionario?

Em Python:

    x in dicionario

pergunta se **x está entre as chaves** do dicionário. Não procura nos valores.

    idades = {"ana": 25, "bia": 30}

    "bia" in idades          # True
    30 in idades              # False: 30 é um valor, não uma chave
    30 in idades.values()     # True: aqui a busca é entre os valores

A consulta por chave ocorre conceitualmente assim:

1. Python obtém o objeto x.
2. Calcula o hash de x.
3. Usa o hash para localizar uma posição candidata.
4. Confere a igualdade entre x e a chave armazenada.
5. Se houver colisão, tenta outras posições de acordo com a estratégia da tabela.
6. Retorna True se encontrar uma chave igual; retorna False se concluir que ela não está no dicionário.

A expressão não é “lida da direita para a esquerda”. Ela significa “x está em dicionario?”. O operador in é o teste de pertencimento; o dicionário realiza a busca.

## 9. Complexidade: o que significa O(1) em média?

A tabela hash é conhecida por buscas rápidas, mas dizer simplesmente “tudo custa O(1)” esconde as condições.

| Operação | Caso médio | Pior caso |
|---|---:|---:|
| Buscar | O(1) | O(n) |
| Inserir | O(1) amortizado, em implementações que redimensionam | O(n) |
| Remover | O(1) | O(n) |

Aqui, n é o número de entradas armazenadas.

### Por que o caso médio é O(1)?

Se os hashes distribuírem bem as chaves e a tabela não estiver cheia demais, a tabela vai a uma posição candidata e verifica poucas entradas. O número de verificações não cresce proporcionalmente a n; por isso, dizemos que a operação é O(1) em média.

Essa análise também supõe que calcular o hash e comparar as chaves custam O(1). Se a chave for uma string longa, calcular o hash ou comparar a string pode depender do tamanho dela.

### Por que o pior caso pode ser O(n)?

Se muitas chaves acabarem na mesma região ou sequência de sondagem, a tabela pode precisar verificar muitas entradas. No limite, uma operação examina uma quantidade proporcional ao número de entradas: O(n).

### O que significa O(1) amortizado para inserção?

Algumas inserções podem ser caras. Quando a tabela fica cheia demais, ela cresce e redistribui as entradas; esse processo, chamado **redimensionamento** ou **rehash**, pode custar O(n) naquele momento.

Mas o redimensionamento não acontece em toda inserção. Ao analisar uma sequência longa de inserções, o custo dessas operações caras fica distribuído entre muitas inserções baratas. Por isso, o custo médio por inserção pode ser O(1) amortizado.

## 10. Fator de carga e tamanho da tabela

O **fator de carga**, frequentemente representado por α, compara o número de entradas com o número de posições:

    α = n / m

- n é o número de entradas.
- m é o número de posições da tabela.

Uma tabela que fica muito cheia tende a ter mais colisões. Muitas implementações acompanham o fator de carga e redimensionam a tabela quando necessário.

## 11. O custo de percorrer um array ou uma lista procurando algo

Em uma lista, não há cálculo de hash para descobrir a posição. Python compara os elementos um por um até encontrar o valor ou chegar ao fim.

    x in minha_lista

Se a lista tem m elementos, a consulta custa O(m) no pior caso.

Em um dict ou set, a consulta é O(1) em média, pelas condições já explicadas.

Se percorremos n elementos e fazemos um teste de pertencimento para cada um:

| Coleção consultada | Custo de cada teste | Custo de n testes |
|---|---:|---:|
| dict ou set | O(1) em média | O(n) em média |
| lista com m elementos | O(m) | O(n · m) |
| lista com n elementos | O(n) | O(n²) |

Exemplo:

    for x in elementos:
        if x in dicionario:
            ...

Se elementos tem n itens e cada consulta ao dicionário custa O(1) em média, o loop custa O(n) em média.

Se, em vez disso, x for procurado em uma lista de tamanho n, cada teste pode custar O(n), e o loop inteiro pode custar O(n²).

Por isso, em problemas de pertencimento repetido, trocar uma lista por um set pode reduzir o tempo de O(n²) para O(n), com o custo de usar memória adicional.

## 12. Regras importantes para chaves e elementos

### Objetos iguais precisam ter hashes iguais

Se duas chaves são consideradas iguais, seus hashes precisam ser iguais. Caso contrário, a tabela poderia procurar a mesma chave em posições diferentes.

O inverso não é necessário: duas chaves diferentes podem ter o mesmo hash. Isso é uma colisão, e a tabela a resolve comparando as chaves.

### A chave não deve mudar de uma forma que altere seu hash

Depois de inserir uma chave, ela deve continuar com o mesmo comportamento de hash e igualdade. Se seu hash mudar, a tabela pode procurar no lugar calculado anteriormente e não encontrá-la.

Por isso, em Python, listas não podem ser usadas como chaves de dict nem como elementos de set: listas são mutáveis e não são hashable.

    coordenadas = {(1, 2): "ponto"}  # funciona: a tupla pode ser hashable
    # {[1, 2]: "ponto"}              # erro: listas não são hashable

Uma tupla também só é hashable se todos os seus componentes forem hashable.

## 13. Dúvidas comuns respondidas

### O código hash aponta para um endereço de memória?

Não necessariamente. Ele ajuda a calcular um índice da tabela. O índice identifica a posição interna onde a busca começa.

### A tabela hash é simplesmente um array?

Uma forma comum de implementá-la usa um array de slots, mas a estrutura também inclui a função de hash e a estratégia para resolver colisões. No encadeamento, um slot pode apontar para uma coleção; no endereçamento aberto, as entradas ocupam posições do próprio array.

### Com colisão, como sei qual valor pertence a cada chave?

Cada entrada do mapa guarda a própria chave e o próprio valor. A tabela compara a chave procurada com a chave de cada entrada candidata e retorna o valor do par cuja chave for igual.

### Hash table, HashMap e HashSet são sinônimos?

Não exatamente. **Hash table** é a estrutura de hashing usada para organizar e localizar entradas. **HashMap** associa chaves a valores. **HashSet** guarda elementos únicos. Em alguns livros e linguagens, “hash table” também é usado como nome para um mapa implementado com hashing.

### O set mapeia um elemento para ele mesmo?

É mais claro dizer que o set guarda elementos únicos e usa cada elemento como chave de busca. O set não apresenta um valor separado associado ao elemento.

### O dict procura entre as chaves ou entre os valores?

A expressão x in d procura entre as chaves. Para procurar entre os valores, pode-se usar x in d.values(), mas essa busca percorre os valores e custa O(n).

## 14. Resumo final

1. Uma hash table usa uma chave para calcular um índice candidato em uma tabela.
2. O código hash é um intermediário; não é um endereço físico de memória.
3. A posição inicial é calculada, mas colisões podem exigir verificações adicionais.
4. Encadeamento mantém uma coleção de entradas por posição; endereçamento aberto procura outros slots no próprio array.
5. Cada entrada de um mapa guarda chave e valor juntos. A comparação de igualdade confirma a chave.
6. HashMap associa chave a valor; em Python, use dict.
7. HashSet guarda elementos únicos; em Python, use set.
8. Busca e remoção costumam custar O(1) em média; inserção costuma ter O(1) amortizado quando há redimensionamento.
9. No pior caso, colisões podem fazer uma operação custar O(n).
10. Em Python, x in d verifica as chaves; x in lista percorre os elementos um a um.

