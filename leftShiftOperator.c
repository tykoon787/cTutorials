#include <stdio.h> 

int main(){
	
	int x = 5; 
	unsigned int z; 
	z = x << 2; // Z is equal to the value of x (5) shifted by 2 bits 

	printf("5 when left shifted by 2 bits is: %d\n", z);
	int i; 
	unsigned int a = 5;
	for (i = 0; i < 20; i++){
		printf("5 When left shifted by %02d is %08x | %u\n", i, a << i, a << i);
	}
		
	

	return 0; 
} 
