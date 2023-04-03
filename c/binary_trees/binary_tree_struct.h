#ifndef TREE_H
#define TREE_H

typedef struct tree {
    int data;
    struct node *left;
    struct node *right;
} tree;

#endif /* TREE_H */