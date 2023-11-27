#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *fast, *slow;

	if (list == NULL)
		return (0);

	fast = slow = list;

	while (slow != NULL && (*slow).next != NULL)
	{
		fast = (*fast).next;
		slow = (*slow).next->next;

		if (fast == slow)
			return (1);
	}
	return (0);
}
