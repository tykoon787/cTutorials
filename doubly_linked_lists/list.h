#ifndef LIST_H
#define LIST_H

#include <stdio.h>
#include <stdlib.h>

typedef struct node_s  
{
	int data;
	struct node_s *next;
	struct node_s *prev;
} node_t;

#endif /* LIST_H */
