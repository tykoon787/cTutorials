#include <stdio.h>


// Defining global variables
const int y = 2;

int main(){

	int x = 100;
	while (x / 2 != 0.5){
		int r= x/y; 
		int b= x%y; 
		printf("%d\n",b); 
		int x = r; 
	}


/*	
	do {
		r= x/y; 
		b=x%y; 
		printf("%d\n", b); 
		int x = r; 
	}while (x/2 != 0.5); 

*/	return 0; 
}

