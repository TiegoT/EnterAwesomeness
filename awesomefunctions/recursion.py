def sum_array(array):
    """Return sum of all items in array

    Args:
        items (array): a list or array-like object containing numerical values

    Returns: int value with sum of all items in array
    """
    if len(array) == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):
    """Return nth term in fibonacci sequence

    Args:
        n (int): number to perform fibonacci operation off of

    Returns:
        n (int): fibonacci number corresponding to n
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def factorial(n):
    ''''Return word in reverse

    Args:
        n (int): number to perform factorial operation off of

    Returns:
        n (int): factorial number corresponding to n
    '''
    return 1 if(n <= 1) else n * factorial(n - 1)


def reverse(word):
    '''Return word in reverse

    Args:
        word (string): one word string
        s
    Returns:
        string: word returns in reverse order
    '''
    if len(word) == 0:
        return word
    else:
        return reverse(word[1:]) + word[0]
