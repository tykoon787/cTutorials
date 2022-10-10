#include <stdio.h>

int main (int argc, char **argv)
{
	int tens = 0;
	int ones = 0; 


	for (; tens <= 9; tens++)
	{
		for (ones = tens + 1; ones <=9; ones++)
		{
			putchar(tens + '0');
			putchar(ones + '0');
			putchar('\t');
		}
	}
	return (0);
}
