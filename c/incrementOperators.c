#include <stdio.h>

int main(){
	

	int w, x, y, z, result; 
	w = x = y = z = 1; 

	printf("Given w = %d, x = %d, y = %d, z = %d", w,x,y,z);
	putchar(10); 

	result = ++w; /*The operator will first add '1' to w then print the value of 'w'*/
	printf("++w evaluates to %d and w is now %d\n", result, w);

	result = x++; /*The operator will first assign the value of 'x' to 'result' then add 'x' by '1'*/
	printf("x++ evaluates to %d and x is now %d\n", result, x);

	result = --y; /*The operator will first subtract '1' from 'y' then print then store the value of 'y' to 'result'*/
	printf("--y evaluates to %d and y is now %d\n", result, y);

	result = z--; /*The operator will first assign the value of z to 'result' then subract '1' from z*/
	printf("z-- evaluates to %d and z is now %d\n", result, z);
	return 0; 
}
