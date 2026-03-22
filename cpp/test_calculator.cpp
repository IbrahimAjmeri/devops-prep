#include <iostream>
#include <cassert>

int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);

int main() {
    assert(add(2, 3) == 5);
    assert(subtract(10, 4) == 6);
    assert(multiply(3, 3) == 9);
    
    std::cout << "All C++ tests passed!" << std::endl;
    return 0;
}