#include <stdio.h>

int main(int argc, char **argv)
{

	int arr[3] = {2, 3, 4};
	int *p = arr;
	int i = 0;

	for (; i < 3; i++)
	{
		printf("%d\n", *(arr+i));
	}

	int var[] = {20, 30, 40, 50, 60};
	int j = 0;

	int *ptr[5];
	
	for (; j < 5; j++)
	{
		ptr[j] = &var[j];
	}

	for (j = 0; j < 5; j++)
	{
		printf("Value of var[%d] is : %d\n", j, *ptr[j]);
	}


	return (0);
}
