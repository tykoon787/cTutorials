#include "main.h"
#include <stdio.h>
#include <stdlib.h>

/* Working with Singly Linked Lists */

/* 1. Create a struct node*/
typedef struct node_t
{
	int data;
	struct node_t *next;

} node_t;

int main(void)
{
	node_t *head_node, *middle_node, *last_node, *temp;

	head_node = malloc(sizeof(node_t));
	middle_node = malloc(sizeof(node_t));
	last_node = malloc(sizeof(node_t));

	head_node->data = 10;
	middle_node->data = 20;
	last_node->data = 30;

	head_node->next = middle_node;
	middle_node->next = last_node;
	last_node = NULL;

	
	temp = head_node;
	while(temp != NULL)
	{
		printf("Data: [%d]\n", temp->data);
		temp = temp->next;
	}

	return (0);
}
