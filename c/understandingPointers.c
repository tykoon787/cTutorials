#include <stdio.h>

int main(void)
{
	int x =7;

	int *ptr = &x; // Points to the address of x
	printf("Address of x is: %p \n", ptr);

	/*To access the actual value pointed to */
	printf("x is %d \n", *ptr); 		
}
