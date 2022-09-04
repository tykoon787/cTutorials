#include <stdio.h>

int main(){
	
	int num1, num2; 
	num1 = 12; 
	num2 = 12345; 

	printf("%d\n", num1);
	printf("%d\n", num2);
	printf("%5d\n", num1);
	printf("%05d\n", num1); //This will insert 0s before to fill in the spaces

	putchar(10);
	printf("Using the Precision specifier \n");

	double num3, num4; 
	num3 = 123.333444;
	num4 = 45.5544444; 

	printf("Rounding off to 4dp: %5.4f\n", num3); // This will display 4 decimal places
	printf("Rounding off to 2dp: %-10.2f\n", num4); // The '-' means that it will be justified to the left
	printf("Rounding off to 2dp without -: %10.2f\n", num4);
	return 0;
}
