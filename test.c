#include <stdio.h>

typedef struct point point;
struct point {
   int    x;
   int    y;
};
point p = {1, 2};

int main(void)
{
	printf("p.y : %d p.x : %d \n", p.y, p.x);
	return (0);
}
