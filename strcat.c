#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
	char *pathname;
	pathname = malloc(sizeof(char) * 100);
	pathname = "/bin/";

	char input[] = "ls";

	printf("%s", strcat(pathname, input));
	
	return (0);
}
