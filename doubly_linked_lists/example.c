#include "list.h"

void *createNode(int x)
{
	node_t *newNode;
	newNode = (node_t*)malloc(sizeof(node_t));
	newNode->data = x;
	newNode->prev = NULL;
	newNode->next = NULL;
	return (newNode);
}

void print_list(node_t *h)
{
	node_t *temp;
	temp = h;

	if (h == NULL)
	{
		printf("List is Empty\n");
	}
	else
	{
		printf("Element -> [%d]", (*temp).data);
		

	}
}

int main(void)
{
	node_t *head, *firstNode, *secondNode, *thirdNode, *fourthNode;

	head = firstNode;
	/* First Node */
	firstNode = (node_t*)malloc(sizeof(node_t));
	firstNode->data = 20;
	firstNode->prev = NULL;
	firstNode->next = secondNode;

	/* Second Node */
	secondNode = (node_t*)malloc(sizeof(node_t));
	secondNode->data = 25;
	secondNode->prev = firstNode;
	secondNode->next = NULL;

	/* Third Node */
	thirdNode = (node_t*)malloc(sizeof(node_t));
	thirdNode->data = 30;
	thirdNode->prev = secondNode;
	thirdNode->next = fourthNode;

	/* Fourth Node */
	fourthNode = (node_t*)malloc(sizeof(node_t));
	fourthNode->data = 35;
	fourthNode->prev = thirdNode;
	fourthNode->next = NULL;


	/* 	
	// Loop to create x number of nodes
	int no_of_nodes = 3; // Number of nodes to be created
	int data[5] = {5, 4, 7, 19, 10}; // Data to be inserted to the nodes
	int idx = 0; // Index to loop through the data
	while (no_of_nodes--)
	{
		createNode(data[idx]);	
	}
	printf("No of nodes created: [%d]", idx - 1);
	*/
	return 0;
}

