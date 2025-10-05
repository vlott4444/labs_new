#ifndef VECTOR_H
#define VECTOR_H

typedef struct{
    int x;
    int y;
    int z;
} Vector;

void vect_print(Vector *vect);
void vect_multiply(Vector *vect1, Vector *vect2);
void summ(Vector *vect1, Vector *vect2);
Vector vect_input();

#endif
