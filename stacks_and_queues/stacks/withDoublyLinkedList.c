#include <stdio.h>
#include <stdlib.h>

typedef struct node_s
{
	int data;
	struct node_s *next;
	struct node_s *prev;
} node_t;

node_t *top = NULL;

void push(int d)
{
	/* Check d */
	if (d < 0)
		printf("Positive Numbers only\n");
	/* Create a node */
	node_t *newNode, *head = NULL;
	newNode = (node_t *)malloc(sizeof(node_t));
	newNode->data = d;
	newNode->next = NULL;
	newNode->prev = NULL;

	/* If head is null, list is empty, else, push */
	if (head == NULL)
		head = top = newNode;
	else
	{
		top->next = newNode;
		newNode->prev = top->next;
		top = newNode;
	}
}

void pop()
{
	node_t *temp;
	temp = top;
	if (top == NULL)
		printf("Stack is empty, nothin to delete\n");
	else
	{
		printf("Popped [%d]\n", (*temp).data);
		top->prev->next = NULL;
		top = top->prev;
		free(temp);
	}
}


