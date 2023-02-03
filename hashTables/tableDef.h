#ifndef tabledef_h
#define tabledef_h

#include "hash.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * createItem- Function that creates items by allocating memory to the key and value 
 * @key: Key
 * @value: Value
 * Return: On success (ht_item)
*/
ht_item_t *createItem(char *key, char *value)
{
    ht_item_t *item = (ht_item_t *)malloc(sizeof(ht_item_t));
    item->key = (char *)malloc(strlen(key) + 1); 
    item->value = (char *)malloc(strlen(value) + 1);
    strcpy(item->key, key);
    strcpy(item->value, value);
    return (item);
}

/**
 * createTable- Function that creates a hash table
 * @size: Size of the Hash Table
 * Return: On success (Hash table)
*/
hashTable_t *createTable(int size)
{
    int i;
    hashTable_t *table = (hashTable_t*)malloc(sizeof(hashTable_t));
    table->size = size;
    table->count = 0;
    table->items = (ht_item_t**) calloc(table->size, siezeof(ht_item_t*));
    
    /* Load table with initial values of NULL */
    for (i = 0; i < table->size; i++)
        table->items[i] = NULL;
    
    return (table);
}

/**
 * freeItem- Function that free heap allocated memory for a hash Table Item
 * @item: Hash Table Item
 * Return: Nothing
*/
void freeItem(ht_item_t *item)
{
    free (item->key);
    free (item->value);
    free (item); 
}

/**
 * freeTable- Function that frees the table by first freeing individual items from the table
 * @table: Hash Table containing items to be freed
 * Return: Nothing
*/
void freeTable(hashTable_t *table)
{
    int i;
    for (i = 0; i < table->size; i++) 
    {
        ht_item_t *item = table->items[i];
        if (item != NULL)
            freeItem(item);
    }
    free(table->items);
    free (table);
}

/**
 * printTable- Function that prints the index, key and value of a table
 * @table: A Hash Table
 * Return: Nothing
*/
void printTable(hashTable_t *table)
{
    int i;
    printf("\n === HASH TABLE ==== \n");

    for (i = 0; i < table->size; i++)
    {
        if (table->items[i])
            printf("Index: %d Key: %s Value: %s ", i, table->items[i]->key, table->items[i]->value);
    }

    printf("\n ------------------ \n");

}
#endif /* tabledef_h */
