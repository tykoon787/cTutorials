#include <stdio.h>
#include <stdlib.h>

#define N 5
int stack[N];
int top = -1;

/* Insert data in stack */
void push()
{
	/* Data to be inserted by user */
	int input;
	printf("Enter Data: ");
	scanf("%d", &input);

	/* Check if Stack is full */
	if (top == N-1)
		printf("Stack if Full. Overflow detected\n");
	else
	{
		top++; // Remember that top is at -1, so we have to move it 0 first
		stack[top] = input; //Insert the data
	}
}

/* Remove the top most element of the stack */
void pop()
{
	int item;
	/* Check if the stack is empty */
	if (top == -1)
		printf("Underflow\n");
	else
	{
		printf("Popped item: [%d]\n",item = stack[top]);
		top--; // If the stack was loaded, then the top would be pointing to 
			// the last data insterted. 
	}
}

/* Checking the top most element of the stack */
void peek()
{
	if (top == -1)
		printf("Stack is Empty\n");
	else
	{
		printf("Top element is: [%d]\n", stack[top]);
	}
}

/* Checking the contents of the stack */
void display()
{
	int i;
	if (top == -1)
		printf("Stack is empty\n");
	for (i = top; i >= 0; i-- )
	{
		printf("Item: [%d]\n", stack[i]);
	}

}

/* Implementation */
int main(void)
{
	/* User to enter value 5 times */
	int x = 5;
	printf("Enter 5 numbers\n");
	while (x--) 
		push();

	/* Initially display with the values eneterd by the user */
	display();

	/* Peek the most top element */
	peek();

	/* Delete all items in the stack */
	x = 5;
	while (x--)
		pop();

	/* Dislay the Stack once again */
	display();
	return (0);
}
