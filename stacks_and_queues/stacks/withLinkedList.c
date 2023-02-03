
#include <stdio.h>
#include <stdlib.h>

typedef struct node_s
{
	int data;
	struct node_s *next;
} node_t;

node_t *top = NULL;

/* Creating a newNode to push to the stack with data x */
void push(int x)
{
	node_t *newNode;
	newNode = (node_t *)malloc(sizeof(node_t));
	newNode->data = x;
	newNode->next = top; // NULL
	top = newNode;
}

/* Displays the top most element of a stack */
void peek()
{
	if (top == NULL)
		printf("Stack is Empty\n");
	else
		printf("Top element is: [%d]\n", (*top).data);
}

/* Deletes from the top */
void pop()
{
	node_t *temp; // Will be used to free the memory
	temp = top;
	if (top == NULL)
		printf("Stack is Empty\n");
	else
	{
		printf("Popped element is: [%d]\n", (*temp).data);
		top = top->next;
		free(temp);
	}
}

/* Display the stack */
void display()
{
	node_t *temp;
	temp = top;
	if (top == NULL)
		printf("Stack is Empty\n");
	else
	{
		while(temp != NULL)
		{
			printf("Data: [%d]\n", temp->data);
			temp = temp->next;
		}
	}
}

/* Implementation */
int main(void)
{
	int x = 5, i = 0;
	int data[] = {10, 15, 20, 25, 30};
	while (x--)
	{
		push(data[i]);
		i++;
	}

	printf("======Displaying Stack ======\n");
	display();

	printf("\nDeleting two items\n");
	pop(); pop();

	printf("======Displaying Stack ======\n");
	display();

	return (0);
}
