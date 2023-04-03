#include <stdio.h>

int main(void)
{

	int tens = 0;
	int ones = 0;

	for (; tens <= 9; tens++)
	{
		for (ones = tens + 1; ones <=9; ones++)
		{	
		if (tens != ones)
		{
		putchar(tens + '0');	
		putchar(ones + '0');
		putchar('\t');
		}
		}
	}

	return (0);
}

