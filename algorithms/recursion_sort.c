#include <stdio.h>
#include <stdlib.h>

void draw(int n);

int main(void)
{
	int height = 10;
	draw(height);
   
	return (0);
}

/**
 * draw - A Function to draw the pyramid recursively
 * @n: Height of the pyramid
 * Return: Nothing
*/
void draw(int n)
{
	int i;
	if (n <= 0)
		return;
	draw(n - 1);
	/* First print n hashes*/
	for (i = 0; i < n; i ++)
	{
			printf("#");
	}
	printf("\n");
}