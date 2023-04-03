#include <stdio.h>
#include <stdlib.h>

/* Add Node at the Beginning */

typedef struct node_t
{
	int data;
	struct node_t *next;
} node_t;

size_t print_all(const node_t *h)
{
	int count = 0;
	const node_t *temp = h;
	while (temp != NULL)
	{
		printf("Data : [%d]\n", temp->data);
		count++;
		temp = temp->next;
	}
	return (count);
}

int main(void)
{

	/* Create a list of nodes to store data */
	node_t *nodeA, *nodeB, *nodeC, *nodeD, *head;	

	/* Create a new node */
	node_t *new_node = malloc(sizeof(node_t));

	/* Assign Space to nodes */
	nodeA = malloc(sizeof(node_t));
	nodeB = malloc(sizeof(node_t));
	nodeC = malloc(sizeof(node_t));
	nodeD = malloc(sizeof(node_t));

	/* Assign Values to the nodes */
	head = nodeA;
	nodeA->data = 20;
	nodeA->next = nodeB;
	nodeB->data = 30;
	nodeB->next = nodeC;
	nodeC->data = 40;
	nodeC->next = nodeD;
	nodeD->data = 50;
	nodeD->next = NULL;
	new_node->data = 100;

	/* Insertion at the beginning */
	new_node->next = head; 
	head = new_node;

	
	print_all(head);

	return (0);
}
