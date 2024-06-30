#include "lists.h"
/**
 * check_cycle - will check for loop in LL
 * @list: head of linked list *
 * Description - check for loops in LL
 * Return: 1 if successfully cycled or  0 if failed
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (!list)
	{
		return (0);
	}
	slow = list;
	fast = list->next;
	while (fast && slow && fast->next)
	{
		if (slow == fast)
		{
			return (1);
		}
		slow = slow->next;
		fast = fast->next->next;
	}
	return (0);
}
