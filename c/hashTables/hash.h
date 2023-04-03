#ifndef HASH_H
#define HASH_H

/**
 * ht_item_s- Structure defining a hash table item
 * @key: Key
 * @value: Value retrieved from the HT
*/
typedef struct ht_item_s
{
	char *key;
	char *value;
} ht_item_t;

/**
 * hashTable_s - Structure defining a hash Table
 * @size: Returns the size of the hashTable
 * @count: Returns the number of elements in the hashTable
*/
typedef struct hashTable_s
{
	ht_item_t **items;
	int size;
	int count;
} hashTable_t;

#endif /* HASH_H */