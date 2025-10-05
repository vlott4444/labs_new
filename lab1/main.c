#include <stdio.h>
#include "vector.h"

int main() {
    Vector a = vect_input();
    Vector b = vect_input();
    vect_multiply(&a, &b);
    summ(&a, &b);
    return 0;
}
