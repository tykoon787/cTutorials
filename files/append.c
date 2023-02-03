#include <stdio.h>
#include <stdlib.h>

int main(void)
{
	FILE *fp;
	char str[50], str1[50];

	fp = fopen("OduorFile.txt", "a");
	if (fp == NULL)
	{
		printf("Error while opening file\n");
		exit(1);
	}
	printf("Enter Content: ");
	scanf("%s", str);

	fprintf(fp, "\n%s", str);
	printf("Successfully Appended\n");
	fclose(fp);

	
	putchar('\n');
	printf("++++++++++++Reading File +++++++++++++\n");
	fp = fopen("OduorFile.txt", "r");
	while (!feof(fp))
	{
		fgets(str1,50, fp);
		printf("%s", str1);
	}
	putchar('\n');
	fclose(fp);

	return (0);
}
