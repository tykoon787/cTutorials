#include <stdio.h>
#include <stdarg.h>
#include <string.h>

int sum(int x, ...);
void get_len(char *placeholder, ...);

int main(void)
{
	printf("Sum of number is : %d \n",	sum(4, 4, 3, 2, 1));
	get_len("Baby Panda\n");
	return (0);
}

int sum (int x, ...)
{
	int total = 0; 
	va_list args;

	va_start(args, x);

	for (int i = 0; i < x; i++)
	{
		total = total + va_arg(args, int);
	}

	va_end(args);

	return (total);
}

void get_len(char *placeholder, ...)
{
	int len = 0; 

	while(*placeholder)
	{
		len++;
		placeholder++;
	}

	char store;
	va_list args; 

	va_start (args, placeholder);

	for (int i = 0; i < len; i++)
	{
		store = va_arg(args, int);
		printf("%c\n", store);
	}

	va_end(args);
}
