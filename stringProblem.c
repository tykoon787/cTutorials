#include <stdio.h>
/* REPEAT */
/* 	OUTPUT 'What is the best subject you take?' */
/* 	INPUT user inputs the best subject they take */
/* 	STORE the user's input in the answer variable */
/* 	IF answer = 'Computer Science' THEN */
/* 		OUTPUT 'Of course it is!' */
/* 	ELSE */
/* 		OUTPUT 'Try again!' */
/* UNTIL answer = 'Computer Science' */


int main(void)
{
	printf("What is the best subject you take?\n");
	char ans[] = {};

	scanf("%s", ans);
	int i = 0;
	while(ans[i] != '\0')
	{
		putchar(ans[i]);
		i++;
	}
	return (0);
}
