#include <stdlib.h>
#include <stdio.h>

int sum(int x,int y);

int average(int(*ptSum)(int,int), int a, int b);

int sum(int x, int y)
{
	return(x+y);
}

int average(int(*ptSum)(int, int), int a, int b)
{
	int value;
	
	value = ptSum(a,b);
	return (value/2);
}

int main(void)
{
	int (*ptSum)(int,int) = sum;
	int result = average(ptSum, 8, 2);
	printf("Average is :%d\n", result);
	return (0);
}
