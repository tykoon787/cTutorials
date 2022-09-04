#include <stdio.h>

int main(){

	int c = ' '; 

	printf("Enter any character: (You can exter 'x' to exit) \n");
	
	while (c != 'x'){
		c = getc(stdin);
		putchar(c);
	       	putchar(10);	
	}
	printf("You have exited the program \n");
	return 0; 
}
