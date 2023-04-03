#include <stdio.h>
#include <stdlib.h>

/* Program implements the use of Pointer Functions */

int add(int x, int y);
int subtract(int x, int y);
int multiply(int x, int y);
int divide(int x, int y);

int add(int x, int y)
{
	printf("Adding %d and %d\n", x, y);
	return (x+y);
}

int subtract(int x, int y)
{
	printf("Subtracting %d from %d\n", x, y);
	if ((x > 0 && y > 00) && ( x > y))
	{
		return (x-y);
	}
	else if ((x > 0 && y > 0) && (y > x))
	{
		return (y-x);
	}
	else 
		return (x-y);
}

int multiply(int x, int y)
{
	printf("Mulitpylying %d and %d\n",x, y);
	return x * y;
}

int divide(int x, int y)
{
	printf("Dividing %d from %d\n", x, y);
	int value;
	if (x != 0 && y !=0)
		value = x / y;
	else 
		printf("Can't use zero \n");
	
	return (value);
}

int main (void)
{
	int choice, x, y;
	int (*ptOperator[])(int, int) = {add, subtract, multiply, divide};
	printf("-------------------------------------------------\n");
	printf("\n");
	printf("0 -> Add, 1 -> Subtract, 2 -> Multiply, 3 -> Divide");
	printf("\n");
	printf("\n");
	printf("-------------------------------------------------\n");
	printf("Enter Operation : ");
	scanf("%d", &choice);
	printf("Enter numbers x and y (Use space between numbers)\n");
	scanf("%d %d", &x, &y);
	printf("%d \n", ptOperator[choice](x , y));
}
