#include <stdio.h>

int main(void)
{
	int n = 5;
	int array[10];
	int i = 3;

	array[n] = i;

	/* Printing elements of the Array */
	int loop_counter = 0;

	for (; loop_counter < 10; loop_counter++)
	{
	printf("%d \n", array[loop_counter]);
	}


	return (0);

	/* Result */
	// Random numbers are generated
	// However, the value at array[n] which is array[5] is always
	// Constantly 3
}
