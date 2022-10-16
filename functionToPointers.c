#include <stdlib.h>
#include <stdio.h>


#define MAX_NAME_SIZE 1000

typedef struct
{
	unsigned int id;
	char name[MAX_NAME_SIZE];
	unsigned int passing_year;
} Student;

#define MAX_STD_SIZE 30
Student std_db[MAX_NAME_SIZE];
memset(std_db, 0, sizeof(std_db));
