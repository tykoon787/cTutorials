#include <stdio.h>
#include <stdlib.h>

int main(void)
{

	FILE *fp;

	fp = fopen("OduorFile.txt", "w");

	if (fp == NULL)
	{
		printf("Failed to open file\n");
		exit(1);
	}

	fputc('B',fp); // Puts a signle character
	fputs("aby Panda\n", fp); // Puts a whole string
	fprintf(fp, "%d %s", 33, "White Kittens\n"); // Puts according to format specifiers
	fclose(fp);
	return (0);
}
