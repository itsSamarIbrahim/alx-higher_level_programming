#include "lists.h"
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
