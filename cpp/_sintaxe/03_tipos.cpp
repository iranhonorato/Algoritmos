#include <iostream>
#include <string>    // Necessário para utilizar std::string


int main() {

    // Inteiros
    short int pequeno = 100;         // 2 bytes (16 bits): -2**16 a 2**16 - 1 
    int usual = 25;                  // 4 bytes (32 bits): -2**32 a 2**32 - 1 
    long long int grande = 1e12;     // 8 bytes (64 bits): -2**64 a 2**64 - 1  


    // Pontos flutuantes, decimais
    float preco = 4.90f;            // Precisão simples - 4 bytes - (Necessita de 'f' no final)
    double pi = 3.1415926535;       // Precisão dupla - 8 bytes 



    // Caracteres e texto
    char letra = 'A';               // Caractere único (1 byte, entre aspas simples)
    std::string nome = "Iran";      // Texto/Cadeia de caracteres (entre aspas duplas)




    // Boleanos
    bool flag = true;
    
    return 0;
}