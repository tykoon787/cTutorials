#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
	int age;
	struct node *next;
}node;

int main(void)
{

	/* Declare the Node */
	node *nodeA, *nodeB, *nodeC;

	/* Assign some space to the node */
	nodeA = (node*)malloc(sizeof(node));
	nodeB = (node*)malloc(sizeof(node));
	nodeC = (node*)malloc(sizeof(node));

	/* Assign a value to the node */
	nodeA->age = 67;
	nodeB->age = 47;
	nodeC->age = 35;

	/* Assign the address */
	nodeA->next = nodeB; 
	nodeB->next = nodeC;
	nodeC->next = NULL;

	/* Create a head */
	node *head;
	head = nodeA;
	
	/* Traversing the List */
	/* Create a temporary Pointer */
	node *temp;
	temp = head;
	
	while (temp->next != NULL)
	{
		printf("%d\n", temp->age);
		temp = temp->next;
	}
	printf("%d\n", temp->age);

	return (0);
}
