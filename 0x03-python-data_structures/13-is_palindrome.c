#include "lists.h"
int is_palindrome(listint_t **head)
{
	listint *end;

	if (head == NULL || *head == NULL || end == NULL)
		return (1);
	if (is_palindrome(head, end->next) && *head->n == end->n)
	{
		*head = *head->next;
		return (1);
	}
	return (0);
}
