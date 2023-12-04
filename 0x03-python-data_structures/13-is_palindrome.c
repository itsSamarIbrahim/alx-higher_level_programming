#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a double pointer to the first value in the list
 * Return: 1 if it is a palindrome (ON SUCCESS),
 *		0 if it is not a palindrome (ON FAILURE)
 */
int is_palindrome(listint_t **head)
{
	listint_t *iteration;
	int buffer[10000], i, x = 0;

	if (head == NULL)
		return (0);

	iteration = *head;
	while (iteration != 0)
	{
		buffer[x++] = iteration->n;
		iteration = iteration->next;
	}
	for (i = 0; i < (x / 2); i++)
	{
		if (buffer[i] != buffer[x - i - 1])
			return (0);
	}
	return (1);
}
