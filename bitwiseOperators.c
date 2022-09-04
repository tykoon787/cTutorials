#include <stdio.h>

int main(){
	int x, y, z; 

	x = 1 & 1; 
	y = 1 & 2; // Will be converted to the binary equivalent
	z = ~5; // This will convert the result its binary equivalent
	printf("Result of x is: %d\n",x);
	printf("Result of y is: %d\n",y);

	printf ("Result of z using NOT operator: %d\n",z);
	/*The above function will print the result in its decimal form because 
	 * we are using the '%d' identifier.
	 *
	 * The result if negative (-6) becuase the value of decimal 5 in base 2 (binary) 
	 * is 1010
	 *
	 * Since int represents a 32 bit digit, the value of 5 to base 2 in its binary 
	 * form is 0000 0000 0000 0000 0000 0000 0000 1010 whose result when negated is 
	 *         1111 1111 1111 1111 1111 1111 1111 0101
	 *
	 * All the ones represent the negative in decimal form (%d) 
	 * */

	unsigned int a; 
	a = ~5; 
	/*
	 *When we declare that the variable is unsigned, we will get a different number. 
	 *The unsigned integer data type (32-bit) has the max number of 4294967295
	 *
	 *
	 * */
	printf("Result of a when using unsigned declaration is: %u\n",a); // We use the %u format specifier
	printf("Result of a is: %u\n",a); // We use the %u format specifier

}
