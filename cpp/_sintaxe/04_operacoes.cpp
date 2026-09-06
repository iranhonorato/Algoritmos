#include <iostream>
#include <string>
#include <cmath>


int main() {
    int a = 10, b = 15;
    
    // Soma 
    int soma = a + b; 

    // Subtração 
    int subtracao = a - b;

    // Divisao interia
    int divisao = b / a;

    // Resto
    int resto = b % a;
    
    // Divisao real
    float div_real = (float) b / a;

    // Exponencial
    int exponencial = std::pow(2,10);

    // Comparacao
    bool igual = (a == b);
    bool menor = (a < b);

    // logicos 
    bool condicao1 = (a > 5 && b < 20);
    bool condicao2 = (a > 0 || b == 15);
    bool negacao = !condicao1;

}   