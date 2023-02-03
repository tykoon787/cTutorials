#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	FILE *fp;
	int count = 0;

	fp = fopen("OduorFile.txt", "r");
	if (fp == NULL)
	{
		printf("Error Reading File\n");
		exit(1);
	}


	printf("========Print using fgetc()============\n");
	while (!feof(fp))
	{
		printf("%c", fgetc(fp));
	}
	fclose(fp);	


	printf("========Print using fgets()============\n");
	fp = fopen("OduorFile.txt", "r");
	char str[30];
	while (!feof(fp))
	{
	fgets(str, 50, fp);
	printf("%s\n", str);
	}

	fclose(fp);
	return (0);
}
