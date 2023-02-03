#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	FILE *fp;

	fp = fopen("OduorFile.txt", "r+");
	if (fp == NULL)
	{
		printf("Error\n");
		exit(1);
	}
	fputs("Not Baby Panda Ha", fp);
	return (0);
}
