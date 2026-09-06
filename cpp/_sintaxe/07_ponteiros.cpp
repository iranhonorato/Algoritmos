#include <iostream>


int main() {
    // Toda variavel ocupa um endereco na memoria
    int idade = 25;

    // & (operador "endereco de"): mostra ONDE a variavel mora
    std::cout << "valor:    " << idade  << std::endl;
    std::cout << "endereco: " << &idade << std::endl;   // algo como 0x7ffd1a2b


    // Ponteiro: variavel que guarda um endereco.
    // O tipo diz o que existe naquele endereco (int* = "ponteiro para int")
    int* p = &idade;

    // * (operador de desreferencia): acessa o valor guardado naquele endereco
    std::cout << p  << std::endl;       // o endereco
    std::cout << *p << std::endl;       // 25

    // Escrever atraves do ponteiro altera a variavel original
    *p = 30;
    std::cout << idade << std::endl;    // 30


    // nullptr: ponteiro que nao aponta para nada. Sempre teste antes de usar
    int* q = nullptr;
    if (q != nullptr) {
        std::cout << *q << std::endl;   // desreferenciar nullptr quebra o programa
    }


    // Referencia (&): um apelido para a variavel, dispensa o *
    int& apelido = idade;               // deve ser inicializada e nunca troca de dono
    apelido = 40;
    std::cout << idade << std::endl;    // 40


    // Arrays e ponteiros: o nome do array ja e o endereco do primeiro elemento
    int numeros[] = {10, 20, 30};
    int* inicio = numeros;              // mesma coisa que &numeros[0]

    std::cout << *inicio       << std::endl;    // 10
    std::cout << *(inicio + 1) << std::endl;    // 20 -> anda 1 int (4 bytes), nao 1 byte
    std::cout << inicio[2]     << std::endl;    // 30 -> [] e so um atalho para *(p + 2)

    // Percorrendo com aritmetica de ponteiros
    for (int* it = numeros; it != numeros + 3; it++) {
        std::cout << *it << " ";
    }
    std::cout << std::endl;


    // Ponteiro para constante: pode ler, nao pode escrever
    const int* somente_leitura = &idade;
    std::cout << *somente_leitura << std::endl;
    // *somente_leitura = 50;           // erro de compilacao

    // Na pratica, ponteiros e referencias servem para uma funcao alterar a
    // variavel de quem a chamou e para passar dados grandes sem copiar tudo.

    return 0;
}
