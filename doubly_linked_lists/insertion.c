#include "list.h"

node_t *head = NULL, *tail, *newNode, *temp;

void *create(int x)
{
	printf("Creating node with data: [%d]\n", x);
	newNode = (node_t *)malloc(sizeof(node_t));
	newNode->data = x;
	newNode->prev = NULL;
	newNode->prev = NULL;
	if (head == NULL)
		head = tail = newNode;
	else
	{
		newNode->prev = tail;
		tail->next = newNode;
		tail = newNode;
	}
	return (head);
}

void insertAtBeginning(node_t *h)
{
	if (h == NULL)
		printf("Empty List cannot be inserted\n");
	else
	{
		newNode->next = head;
		head->prev = newNode;
		head = newNode;
	}
}

void display(node_t *h)
{
	printf("\n === Displaying data === \n");
	if (h == NULL)
		printf("Nothing to display\n");
	else
	{
		temp = head;
		while (temp != NULL)
		{
			printf("Data: [%d]\n", (*temp).data);
			temp = temp->next;
		}
	}
}

int main(void)
{
	int data[5] = {20, 25, 30, 35, 40};
	int i = 0, counter = 5;
	while (counter--)
		head = create(data[i++]);
	display(head);
	return (0);
}
