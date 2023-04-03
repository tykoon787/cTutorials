#include <stdio.h>
#include <stdlib.h>

typedef struct node_s
{
	int data;
	struct node_s *next;
	struct node_s *prev;
}node_t;

node_t *head = NULL, *newNode, *temp;

void *create(int x)
{
	printf("Creating a node\n");
	newNode = (node_t *)malloc(sizeof(node_t));
	newNode->data = x;
	newNode->next = NULL;
	newNode->prev = NULL;

	if (head == NULL)
		head = temp = newNode;
	else
	{
		newNode->prev = temp;
		temp->next = newNode;
		temp = newNode;
	}
	return head;
}

void display(node_t *h)
{
	if (h == NULL)
		printf("List Empty List\n");
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

	int data[5] = {10, 15, 20, 25, 30};
	int count = 5, i = 0;
	while (count--)
	{
		head = create(data[i]);
		i++;
	}
	display(head);
	return (0);
}
