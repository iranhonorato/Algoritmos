#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <unordered_map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>      // sort, find, reverse, max_element...
#include <numeric>        // accumulate


int main() {
    // A STL e a biblioteca padrao do C++ e tem tres partes que se encaixam:
    //   1. CONTAINERS  - estruturas prontas (vector, map, set, queue...)
    //   2. ITERADORES  - "ponteiros" que percorrem qualquer container
    //   3. ALGORITMOS  - funcoes (sort, find...) que trabalham sobre iteradores
    // Todos sao templates: o <int> dentro dos sinais de menor/maior diz qual
    // tipo o container vai guardar.


    // ================= vector: o array que cresce =================
    // Faz sozinho o malloc/realloc/free do arquivo anterior.
    std::vector<int> numeros = {5, 3, 8};

    numeros.push_back(1);               // adiciona no fim
    numeros.pop_back();                 // remove do fim
    numeros.push_back(1);

    std::cout << numeros[0]      << std::endl;   // acesso direto, sem checagem
    std::cout << numeros.at(1)   << std::endl;   // .at() avisa se o indice for invalido
    std::cout << numeros.size()  << std::endl;   // quantos elementos
    std::cout << numeros.empty() << std::endl;   // 1 se estiver vazio

    for (int n : numeros) {
        std::cout << n << " ";
    }
    std::cout << std::endl;


    // ================= algoritmos =================
    std::sort(numeros.begin(), numeros.end());              // ordena no lugar
    std::sort(numeros.begin(), numeros.end(), std::greater<int>());  // decrescente
    std::reverse(numeros.begin(), numeros.end());           // volta a ser crescente

    // begin() aponta para o primeiro elemento, end() para DEPOIS do ultimo
    auto it = std::find(numeros.begin(), numeros.end(), 8);
    if (it != numeros.end()) {                              // end() = "nao achei"
        std::cout << "achei o 8 na posicao " << (it - numeros.begin()) << std::endl;
    }

    std::cout << *std::max_element(numeros.begin(), numeros.end()) << std::endl;
    std::cout << std::accumulate(numeros.begin(), numeros.end(), 0) << std::endl;  // soma
    std::cout << std::count(numeros.begin(), numeros.end(), 3) << std::endl;

    // Em vetor JA ORDENADO, busca binaria em O(log n)
    std::cout << std::binary_search(numeros.begin(), numeros.end(), 5) << std::endl;


    // ================= map: o dicionario =================
    // Guarda pares chave -> valor, sempre ORDENADOS pela chave. O(log n)
    std::map<std::string, int> idades;

    idades["Iran"] = 25;                // insere
    idades["Ana"]  = 30;
    idades["Iran"] = 26;                // chave repetida sobrescreve

    std::cout << idades["Ana"] << std::endl;
    std::cout << idades.size() << std::endl;

    // Cuidado: idades["Ze"] CRIA a chave com valor 0 so de consultar.
    // Para so verificar, use count() (ou contains(), C++20):
    if (idades.count("Ana")) {
        std::cout << "Ana existe" << std::endl;
    }

    idades.erase("Ana");

    // Percorrendo: cada elemento e um std::pair (.first = chave, .second = valor)
    for (const auto& [nome, idade] : idades) {      // structured binding (C++17)
        std::cout << nome << " tem " << idade << " anos" << std::endl;
    }

    // unordered_map: mesma interface, tabela hash, O(1) em media, SEM ordem.
    // Use este quando a ordem nao importa (quase sempre mais rapido).
    std::unordered_map<std::string, int> estoque;
    estoque["caneta"] = 12;
    std::cout << estoque["caneta"] << std::endl;


    // ================= set: conjunto de unicos =================
    // Ordenado e sem repeticao. Existe tambem o unordered_set (hash).
    std::set<int> unicos = {4, 1, 4, 7, 1};

    unicos.insert(2);
    unicos.erase(7);

    std::cout << unicos.count(4) << std::endl;      // 1 = existe, 0 = nao existe
    for (int u : unicos) {
        std::cout << u << " ";                      // sai ordenado: 1 2 4
    }
    std::cout << std::endl;


    // ================= stack: pilha (LIFO) =================
    // Ultimo a entrar e o primeiro a sair
    std::stack<int> pilha;
    pilha.push(1);
    pilha.push(2);
    std::cout << pilha.top() << std::endl;          // 2 (so espia)
    pilha.pop();                                    // remove, mas nao devolve
    std::cout << pilha.top() << std::endl;          // 1


    // ================= queue: fila (FIFO) =================
    // Primeiro a entrar e o primeiro a sair
    std::queue<std::string> fila;
    fila.push("primeiro");
    fila.push("segundo");
    std::cout << fila.front() << std::endl;         // primeiro
    std::cout << fila.back()  << std::endl;         // segundo
    fila.pop();
    std::cout << fila.front() << std::endl;         // segundo


    // ================= priority_queue: heap =================
    // A fila sai ordenada por prioridade, nao por chegada.
    // Por padrao e um MAX-heap: o maior sempre no topo. push/pop em O(log n)
    std::priority_queue<int> heap;
    heap.push(3);
    heap.push(10);
    heap.push(7);

    while (!heap.empty()) {
        std::cout << heap.top() << " ";             // 10 7 3
        heap.pop();
    }
    std::cout << std::endl;

    // MIN-heap (menor no topo): troque o comparador
    std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
    min_heap.push(3);
    min_heap.push(10);
    min_heap.push(7);
    std::cout << min_heap.top() << std::endl;       // 3


    // ================= resumo de custo =================
    // vector          - acesso O(1), push_back O(1) amortizado, busca O(n)
    // map / set       - insere, busca e remove em O(log n), sempre ordenados
    // unordered_*     - O(1) em media, sem ordem nenhuma
    // stack / queue   - insere e remove em O(1) na ponta certa
    // priority_queue  - topo em O(1), inserir e remover em O(log n)

    return 0;
}
