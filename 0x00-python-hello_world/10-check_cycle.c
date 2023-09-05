#include <list.h>

/**
 * check_cycle- checks whether a linked list has a cycle
 * @list: linked list to check
 *
 * Return: 1 if the list has a cycle, 0 if it does not.
 */
int check_cycle(listnt_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list

		if (!list)
			return (0);
	while (slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
