#include <iostream>
#include <string>


int main() {
    int i = 0;

    // while
    while (i < 5) {
        std::cout << i << " ";
        i++;                  
    }
    std::cout << std::endl;


    // do-while: executa ANTES de testar, entao roda pelo menos uma vez
    int senha;
    do {
        std::cout << "Digite a senha: ";
        std::cin >> senha;
    } while (senha != 1234);           


    // for 
    for (int j = 0; j < 5; j++) {       // 'j' so existe dentro do for
        std::cout << j << " ";
    }
    std::cout << std::endl;

    // o passo nao precisa ser +1 
    for (int j = 10; j > 0; j -= 2) {
        std::cout << j << " ";
    }
    std::cout << std::endl;


    // for baseado em intervalo (C++11): percorre os elementos, sem indice
    int numeros[] = {3, 7, 2, 9};
    for (int n : numeros) {             // use 'int& n' para alterar o original
        std::cout << n << " ";
    }
    std::cout << std::endl;

    std::string nome = "Iran";
    for (char c : nome) {
        std::cout << c << ".";
    }
    std::cout << std::endl;


    // break encerra o loop; continue pula para a proxima iteracao
    for (int j = 1; j <= 10; j++) {
        if (j % 2 != 0) continue;       // ignora os impares
        if (j > 6) break;               // para quando passar de 6
        std::cout << j << " ";          // imprime: 2 4 6
    }
    std::cout << std::endl;


    // Loops aninhados: o interno completa todas as voltas a cada volta do externo
    for (int linha = 1; linha <= 3; linha++) {
        for (int coluna = 1; coluna <= 3; coluna++) {
            std::cout << linha * coluna << "\t";
        }
        std::cout << std::endl;         // um break aqui sairia so do for interno
    }

    return 0;
}
