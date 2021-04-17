#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Each number to be sorted is a node in a pile of linked lists.
typedef struct node
{
    // The number itself
    int number;
    // A pointer to the next number in its pile
    struct node *next;
    // A pointer to the top number of the pile to the left of it
    struct node *pile;
}
node;

int length;

// A patience sort algorithm for finding the longest decreasing/increasing subsequence in O(nlogn)
void patience_sort(int sequence[], bool increasing);

int main(void)
{
    // Gets the list length from the user
    scanf("%i", &length);

    // Will store the list of numbers
    int dataset[length];

    // Opens dataset and reads it into file
    FILE *file = fopen("C:/input.txt", "r");

    // Scans file and adds it to array dataset
    for (int i = 0; fscanf(file, "%i", &dataset[i]) > 0; i++) {}

    fclose(file);

    // Prints empty line between input and output
    printf("\n");

    // Finds and prints the longest increasing subsequence
    patience_sort(dataset, true);
    // Finds and prints the longest decreasing subsequence
    patience_sort(dataset, false);

    return 0;
}


void patience_sort(int sequence[], bool order)
{
    // Table of pointers to linked lists, where each list is essentially a "pile" of numbers.
    node *table[length];

    // The number of linked lists (or piles) that have been created. Indexed at zero.
    int counter = 0;

    // The first number in the sequence is a corner case and can't be in the iteration
    node *first = malloc(sizeof(node));

    // If memory is successfully allocated
    if (first != NULL)
    {
        // It's number is the first number of the sequence
        first->number = sequence[0];
        // It's next and pile pointers are NULL for now
        first->next = NULL;
        first->pile = NULL;
        // Add it to the first linked list (or pile)
        table[0] = first;
    }

    // Iterate through the sequence
    for (int i = 1; i < length; i ++)
    {
        // Each number is part of a node
        node *n = malloc(sizeof(node));

        // If memory is successfully allocated
        if (n != NULL)
        {
            // It's number is the current sequence number
            n->number = (int)sequence[i];
            // It's next and pile pointers are NULL for now
            n->pile = NULL;
            n->next = NULL;
        }

        // Keeps track if it's added to a linked list (pile) or not
        bool added = false;

        // Iterates through the linked lists (piles) that we created
        for (int j = 0; j <= counter; j++)
        {
            // If we're finding the increasing subsequence
            if (order == true)
            {
                // If the number is less than the top number in a pile
                if (n->number < table[j]->number)
                {
                    // Add it to the pile
                    n->next = table[j];
                    table[j] = n;

                    // The first pile's pile pointers should remain NULL
                    if (j > 0)
                    {
                        // If it's not the first pile, it should point to
                        // the top number on the pile to the left of it
                        n->pile = table[j - 1];
                    }

                    // It has been added to a pile
                    added = true;

                    // We don't need to keep iterating
                    break;
                }
            }

            // If we're finding the decreasing subsequence
            else
            {
                // If the number is greater than the top number in a pile
                if (n->number > table[j]->number)
                {
                    // Add it to the pile
                    n->next = table[j];
                    table[j] = n;

                    // The first pile's pile pointers should remain NULL
                    if (j > 0)
                    {
                        // If it's not the first pile, it should point to
                        // the top number on the pile to the left of it
                        n->pile = table[j - 1];
                    }

                    // It has been added to a pile
                    added = true;

                    // We don't need to keep iterating
                    break;
                }
            }
        }

        // If there wasn't a pile we could add it to
        if (added == false)
        {
            // Create a new pile and add the node to it
            counter++;
            table[counter] = n;
            n->pile = table[counter - 1];
        }
    }

    // The length of our final result is equal to the number
    // of piles we have + 1 (since counter is indexed at zero)
    int results[counter + 1];

    // Iterable for for loop below. We count down since
    // the pointers will be in backwards order. That way,
    // when we go through results upwards, it'll be in forwards order.
    int m = counter;

    // Traverses through linked list created from pile pointers
    for (node *tmp = table[counter]; tmp != NULL; tmp = tmp->pile)
    {
        results[m] = tmp->number;
        m--;
    }

    // Iterates through all piles and results array, freeing the piles.
    for (int i = 0; i <= counter; i++)
    {
        printf("%i ", results[i]);
        // Frees all memory allocated in the pile
        while (table[i] != NULL)
        {
            node *tmp = table[i]->next;
            free(table[i]);
            table[i] = tmp;
        }
    }

    printf("\n");
    return;
}
