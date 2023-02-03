#include <stdio.h>
#include <stdlib.h>

typedef struct node_s
{
	int data;
	struct node_s *next;
} node_t;

node_t *front = NULL;
node_t *rear = NULL;

void enqueue(int x)
{
	node_t *newNode;
	newNode = (node_t *)malloc(sizeof(node_t));
	newNode->data = x;
	newNode->next = NULL;

	if (front == NULL && rear == NULL)
		front = rear = newNode;	
	else
	{
		rear->next = newNode;
		rear = newNode;
	}
}

void display()
{
	printf("====== Displaying data ====== \n");
	node_t *temp;
	if (front == NULL && rear == NULL)
		printf("Queue is empty\n");
	else
	{
		temp = front;
		while (temp != NULL)
		{
			printf("Element: [%d]\n",(*temp).data);
			temp = temp->next;
		}
	}
}

void dequeue()
{
	node_t *temp;
	temp = front;
	
	if (front == NULL && rear == NULL)
		printf("Queue is empty\n");
	else
	{
		printf("Deleted element: [%d]\n", (*front).data);
		front = front->next;
		free(temp);
	}
}

void peek()
{
	
	if (front == NULL && rear == NULL)
		printf("Queue is empty\n");
	else
		printf("First Element in the queue: [%d]\n", (*front).data);

}

int main(void)
{
	int x = 5, i = 0;
	int data[] = {10, 15, 20, 25, 30};
	while (x--)
	{
		enqueue(data[i]);
		i++;
	}

	display();

	dequeue();
	dequeue();

	peek();

	display();
	return (0);
}
