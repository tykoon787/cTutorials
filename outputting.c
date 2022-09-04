#include <stdio.h>

int main(){

	int ch; 
	ch = 65;

	printf("The character that has the numberic value of 65 is \n");
	putc(ch, stdout);
	putchar(10); // Output a new line

	putchar(66);
	putchar(10);
	return 0;
}
