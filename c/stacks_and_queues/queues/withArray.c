#include <stdio.h>
#include <stdlib.h>

#define N 5
int queue[N];
int front = -1;
int rear = -1;

void enqueue(int x)
{
	/* Check for overflow i.e., when rear is equal to the array size */
	if (rear == N -1)
		printf("Overflow\n");
	else if(front == 1 && rear == -1)
	{
		front = rear = 0;
		queue[rear] = x;
	}
	else
	{
		rear++;
		queue[rear] = x;
	}
}

void dequeue()
{
	if (front == -1 && rear == -1)
		printf("Underflow\n");
	/*
	* If front and rear are pointing to the same index, then it means that there is
	* only one data item left. 
	Since the intention is to dequeue the value, we can set front and rear to be 
	equal to -1 and the value will be discarded 
	*/
	else if (front == rear)
		front = rear = -1;	
	else
	{
		printf("Dequeued element: [%d]", queue[front]);
		front++;
	}
}

void peek()
{
	if (front == -1 && rear == -1)
		printf("List is Empty\n");
	else
		printf("First Element in Queue: [%d]\n", queue[front]);
}

void display()
{
	int i;
	if (front == -1 && rear == -1)
		printf("List is empty\n");
	else
	{
		for(i = front; i < rear + 1; i++)
			printf("Element: [%d]", queue[i]);
	}
}
