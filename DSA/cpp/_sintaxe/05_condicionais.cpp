#include <iostream>


int main() {
    int nota = 75;

    if (nota >= 90) {
        std::cout << "A\n";
    } else if (nota >= 70) {     
        std::cout << "B\n";
    } else {
        std::cout << "C\n";
    }
}
