#include <stdio.h>

/* Global Variables */
int sum;

/* Function Prototypes */	
int greatestCommonDivisor(int, int);
int leastCommonMultiple(int, int);

/* Function Definitions */
int greatestCommonDivisor(int a, int b)
{
	while (a && b)
		if (a > b)
			a %= b;
		else
			b %= a;
	return (a + b);
}


int leastCommonMultiple(int a, int b)
{
	return (a / greatestCommonDivisor(a, b)) * b;
}

/* Entry Point */
int main(void)
{
	int x, y; 
	printf("Enter two values to find their GCD and LCM : ");
	scanf("%d%d", &x, &y);
	printf("GCD : %d \nLCM : %d", greatestCommonDivisor(x,y), leastCommonMultiple(x,y));
	sum = greatestCommonDivisor(x,y) + leastCommonMultiple(x,y);
	printf("\nSum of GCD and LCM : %d \n", sum);
	return (0);
}
