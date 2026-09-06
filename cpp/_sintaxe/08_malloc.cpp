#include <iostream>
#include <cstdlib>    // malloc, calloc, realloc, free
#include <memory>     // std::unique_ptr


int main() {
    // Ate aqui as variaveis viviam na STACK: o compilador sabe o tamanho delas
    // e libera tudo sozinho no fim do bloco.
    // A HEAP e a memoria que voce pede em tempo de execucao (o tamanho pode vir
    // de uma variavel) e que voce mesmo precisa devolver depois.


    // ---------- malloc / free (herdado do C) ----------

    // malloc recebe o tamanho em BYTES e devolve void*, por isso o cast
    int* n = (int*) std::malloc(sizeof(int));

    if (n == nullptr) {                 // devolve nullptr se faltar memoria
        std::cout << "falha na alocacao" << std::endl;
        return 1;
    }

    *n = 42;                            // malloc NAO inicializa: antes disso era lixo
    std::cout << *n << std::endl;

    std::free(n);                       // devolve a memoria ao sistema
    n = nullptr;                        // usar 'n' depois do free seria ponteiro pendurado


    // Vetor dinamico: aqui esta a graca, o tamanho nao precisa ser constante
    int tamanho = 5;
    int* vetor = (int*) std::malloc(tamanho * sizeof(int));

    for (int i = 0; i < tamanho; i++) {
        vetor[i] = i * 10;              // vetor[i] e o mesmo que *(vetor + i)
    }
    for (int i = 0; i < tamanho; i++) {
        std::cout << vetor[i] << " ";
    }
    std::cout << std::endl;


    // calloc: mesma ideia (quantidade, tamanho de cada), mas ja zera tudo
    int* zerado = (int*) std::calloc(tamanho, sizeof(int));
    std::cout << zerado[0] << std::endl;        // 0, garantido
    std::free(zerado);


    // realloc: redimensiona o bloco. Pode MOVER os dados de lugar, entao guarde
    // o retorno num ponteiro novo: se falhar, o bloco antigo continua valido
    int* maior = (int*) std::realloc(vetor, 10 * sizeof(int));
    if (maior != nullptr) {
        vetor = maior;
    }
    std::cout << vetor[0] << std::endl;         // os 5 primeiros valores continuam la

    std::free(vetor);
    vetor = nullptr;


    // ---------- new / delete (o jeito C++) ----------

    // Nao precisa de sizeof nem de cast, e ainda chama o construtor do tipo
    int* x = new int(7);                // aloca e inicializa com 7
    std::cout << *x << std::endl;
    delete x;                           // par obrigatorio do new

    int* lista = new int[tamanho]{};    // as chaves vazias zeram os elementos
    lista[0] = 1;
    delete[] lista;                     // new[] casa com delete[], new casa com delete

    // Nunca misture as duas famílias: free() em memoria de new, ou delete em
    // memoria de malloc, e comportamento indefinido.


    // ---------- os tres erros classicos ----------
    // 1. vazamento (leak):    alocar e nunca liberar
    // 2. dangling pointer:    usar o ponteiro depois do free/delete
    // 3. double free:         liberar o mesmo bloco duas vezes


    // ---------- na pratica ----------
    // Em C++ moderno raramente se escreve malloc/delete na mao: o ponteiro
    // inteligente libera sozinho ao sair do escopo, e std::vector faz o
    // trabalho de malloc + realloc + free por voce.
    std::unique_ptr<int> seguro = std::make_unique<int>(99);
    std::cout << *seguro << std::endl;  // nao existe delete aqui, e esta certo

    return 0;
}
