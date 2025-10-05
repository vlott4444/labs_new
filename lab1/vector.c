#include <stdio.h>
#include "vector.h"


void vect_print(Vector *vect){
    printf("[%d , %d, %d]\n\n", vect->x, vect->y, vect->z);
}

void vect_multiply(Vector *vect1, Vector *vect2) {
    printf("матрица для подсчета векторного произведения: \n");
    printf("   | %3s %3s %3s |\n", "i", "j", "k");
    printf("   | %3d %3d %3d |\n", vect1->x, vect1->y, vect1->z);
    printf("det| %3d %3d %3d | = ", vect2->x, vect2->y, vect2->z);

    int x_comp = vect1->y * vect2->z - vect1->z * vect2->y;
    int y_comp = vect1->z * vect2->x - vect1->x * vect2->z;
    int z_comp = vect1->x * vect2->y - vect1->y * vect2->x;
    Vector comp = {x_comp, y_comp, z_comp};

    printf("i*(%d) + j*(%d) + k*(%d)\n", x_comp, y_comp, z_comp);
    printf("произведение векторов: ");
    vect_print(&comp);
}

void summ(Vector *vect1, Vector *vect2){
    int x_comp = vect1->x + vect2->x;
    int y_comp = vect1->y + vect2->y;
    int z_comp = vect1->z + vect2->z;
    Vector comp = {x_comp, y_comp, z_comp};
    printf("сумма векторов : ");

    vect_print(&comp);
}


Vector vect_input(){
    Vector v;
    printf("Введите вектор (x y z): ");
    scanf("%d %d %d", &v.x, &v.y, &v.z);
    return v;
}
