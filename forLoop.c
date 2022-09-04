#include <stdio.h>

int main(){

	int i; 	
	for (i=0; i < 15; i++){
		printf("The value of i is %d\n",i);
	}
	printf("The value of i is now %d\n",i);
	printf("End of Loop\n");

	putchar(10);


	int j,k; 
	for (i=0, j=10; i!=j; i++, j--){ /*Notice the use of comma to separate expressions*/
		printf("%d + %d = %d\n", i,j,i+j);
	}
	printf("At this point, the value of i and j are equal\n");
	printf("End of Loop \n");
	return 0; 
}
