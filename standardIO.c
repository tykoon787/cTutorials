# include <stdio.h>

int main(){

	int ch; 

	printf("Enter one character: ");
	ch = getc(stdin); 
	printf("The character you printed is: %c\n", ch);

	printf("Using the getchar(void) Function To read input \n");

	int ch1, ch2; 
	printf("Enter two characters following each other \n");
	ch1 = getc(stdin);
	ch2 = getchar();

	printf("The first character you entered is: %c \n", ch1);
	printf("The second character you enterred is: %c \n", ch2);

	return 0;
}
