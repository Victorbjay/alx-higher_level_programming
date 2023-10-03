#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to start of list
 * @number: integer to add to the list
 *
 * Return: pointer to the new node
 * or NULL if it fails.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *curr, *new;

	curr = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	/* insert to empty list */
	if ((*head) == NULL)
	{
		*head = new;
		new->next = NULL;
	}
	else
	{
		while (curr->next != NULL)
		{
			/* insert at begining */
			if (curr->next->n > number)
			{
				new->next = curr->next;
				curr = new;
				break;
			}
			curr = curr->next;
		}

	}
	return (new);

}
