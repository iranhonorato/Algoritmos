#include <iostream>


int main() {
    std::string nome; // declaracao da variável tipada (veremos isso em 03_tipos)
    std::cin >> nome; // input na variável

    std::cout << "Olá " << nome << ", " << "tudo bem?" << std::endl;

    return 0;
}