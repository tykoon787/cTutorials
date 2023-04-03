#ifndef OPS_H
#define OPS_H

#include "tableDef.h" 
#include "hash.h"

/**
 * ht_insert- Function that inserts data
 * @table: A Hash Table
 * @key: Key
 * @value: Value to be passed
 * Return: Nothing
*/
void ht_insert(hashTable_t *table, char *key, char *value)
{
    /* Create the Item */
    ht_item_t *item = createItem(key, value);

    /* Compute the Index*/
    int index = hash_function(key);

    ht_item_t *current_item = table->items[index];

    if (current_item == NULL)
    {
        /* Key doesn't Exist */
        if (table->count == table->size)
        {
            /* Hash Table is Full */
            printf("Insert Error: Hash Table is full\n");
            freeItem(item);
            return;
        }

        /* Insert Directly */
        table->items[index] = item;
        table->count++;
    }
    else
    {
		if (strcmp(current_item->key, key) == 0)		
		{
			/* Update The value */
			strcpy(table->items[index] -> value, value);
			return;
		}
		else
		{
			/* Scenario 2: Hanlding collision */
			handle_collision(table, item);
		}
    }
}

void handle_collision(hashTable_t *table, ht_item_t *item)
{
	return;
}

/**
 * hash_function- This is a hash function
 * @key: 
*/
void hash_function(char *key)
{
	return;
}

/**
 * ht_search- Function that searches for a Key in the Hashtable
 * @key: Key to be searched
 * Return: On Success (value) else NULL
*/
char *ht_search(hashTable_t *table, char *key)
{
	int index = hash_function(key);
	ht_item_t *item = table->items[index];

	if (item != NULL)
	{
		if (strcmp(item->key, key) == 0)
			return item->value;
	}

	return NULL;
}

/**
 * print_search- Function that prints the Item that matches the key
 * @key: Key
 * Return: Nothing
*/
void print_search(hashTable_t *table, char *key)
{
	char *val;

	if (val = ht_search(table, key) == NULL)
	{
		printf("Key: %s does not exist\n");
		return;
	}
	else
		printf("Key: %s, Value: %s\n", key, val);
}

#endif /* OPS_H */
