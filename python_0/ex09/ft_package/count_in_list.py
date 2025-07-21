def count_in_list(lst: list, item: any) -> int:
    """
    Counts the occurrences of an item in a list.

    Args:
        lst (list): The list to search within.
        item (any): The item to count.

    Returns:
        int: The number of times 'item' appears in 'lst'.
    """
    return lst.count(item)
