#include <stdio.h>

int sum(int, int);

/* Initialize the function pointer to pint to the address of the function */
int (*sum_ptr)(int,int) = &sum;
