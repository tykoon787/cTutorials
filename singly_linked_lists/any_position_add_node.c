#include <stdio.h>
#include <stdlib.h>

typedef struct node_t
{
	int data;
	struct node_t *next;
} node_t;

int main(void)
{

	/* Create a list of nodes to store data */
	node_t *nodeA, *nodeB, *nodeC, *nodeD,*nodeE, *nodeF, *head, *temp;	
	int len = 0, n = 0, pos;

	/* Create a new node */
	node_t *new_node = malloc(sizeof(node_t));

	/* Assign Space to nodes */
	nodeA = malloc(sizeof(node_t));
	nodeB = malloc(sizeof(node_t));
	nodeC = malloc(sizeof(node_t));
	nodeD = malloc(sizeof(node_t));
	nodeE = malloc(sizeof(node_t));
	nodeF = malloc(sizeof(node_t));

	/* Assign Values to the nodes */
	head = nodeA;
	nodeA->data = 20;
	nodeA->next = nodeB;
	nodeB->data = 30;
	nodeB->next = nodeC;
	nodeC->data = 40;
	nodeC->next = nodeD;
	nodeD->data = 50;
	nodeD->next = nodeE; 
	nodeE->data = 60;
	nodeE->next = nodeF;
	nodeF->data = 80;
	nodeF->next = NULL;

	/* Value to be inserted */
	new_node->data = 70;

	/* Getting Length of List */
	temp = head;
	while (temp != NULL)
	{
		len++;
		temp = temp->next;
	}
	printf("Length : [%d]\n",len);
	/* Insert at any position (n)*/	
	printf("Enter Position to insert: \n");
	scanf("%d",&pos);
	temp = head;
	if (pos > len)
	{
		printf("Error! Cannot insert at position :\"%d\"\n", pos);
		return(1);
	}
	else
	{
		while(n < pos)	
		{
			temp = temp->next;
			n++;
		}
		new_node->next = temp->next;
		temp->next = new_node;
	}

	/* Print out the list */
	temp = head;
	len = 0;
	while (temp != NULL)
	{
		printf("Data: [%d]\n", temp->data);
		len++;
		temp = temp->next;
	}
	printf("New Length : %d\n", len);
		

	return (0);
}
