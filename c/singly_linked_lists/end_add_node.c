#include <stdio.h>
#include <stdlib.h>

/* Add Node at the End */

typedef struct node_t
{
	int data;
	struct node_t *next;
} node_t;

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
	nodeD->next = new_node;
	new_node->data = 100;
	new_node->next = NULL;

	/* Insertion at the end */
	
	node_t *temporary = head;
	while (temporary->next != NULL)
	{
		printf("Data [%d]\n", temporary->data);
		temporary = temporary->next;
	}
	printf("Data [%d]\n", temporary->data);
	temporary->next = new_node;

	return (0);
}
