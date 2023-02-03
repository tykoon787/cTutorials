#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	char *str = "Baby Panda Bamboo";
	int position = 0;

	char **tokens = malloc(sizeof(char) * 1024);
	char *token;

	token = strtok(str, " ");
	
	while(token != NULL)
	{
		tokens[position] = token;
		token = strtok(NULL, " ");
		position++;
	}
	tokens[position] = NULL;

	printf("Tokens Received : [%s]\n", *tokens);

	return (0);
}
