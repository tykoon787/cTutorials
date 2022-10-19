#include "task3_main.h"
#include <stdio.h>
#include <stdarg.h>

void print_all(const char * const format, ...)
{
	int len = 0, size = 0; 
	char *temp; 

	while(format[size] != '\0')
	{
		len++;
		size++;
	}
	size = 0; 

	va_list args; 

	va_start(args, format);

	while(len--)
	{
		switch(format[size])
		{
			case 'c': 
			putchar(va_arg(args, int));	
			putchar('\n');
			break;
			
			case 'i':
			printf("%d\n", va_arg(args, int));
			break;

			case 'f':
			printf("%f\n", va_arg(args, double));
			break;

			case 's':
			temp = va_arg(args, char *);
			if (temp != NULL)
				printf("%s\n", temp);
			else
				printf("(nil)");
			break;
		}	
	size++;
	}
	putchar('\n');
}

int main(void)
{
	print_all("ceis", 'B', 3, "stSchool", "Baby Panda");
	return (0);
}
