def bubble_sort(items):
    '''Return array of items, sorted in ascending order

    Args:
        items (array): a list or array-like object containing numerical values

    Returns:
        array: items sorted in ascending order
    '''
    x = 0

    for i in range(len(items)-1):
        if items[i] > items[i+1]:
            items[i], items[i+1] = items[i+1], items[i]
            x += 1

    if x == 0:
        return items
    else:
        return bubble_sort(items)

def merge_sort(items):
    '''Return array of items, sorted in ascending order

    Args:
        items (array): a list or array-like object containing numerical values
    Returns:
        array: items sorted in ascending order
    '''

    def merge(items, left, right):
        if left < right:
            mid_point = (left + right) // 2
            merge(items, left, mid_point)
            merge(items, mid_point + 1, right)

            temp_list = []
            i = left
            j = mid_point + 1
            k = 0
            while i <= mid_point and j <= right:
                if items[i] <= items[j]:
                    temp_list.append(items[i])
                    k = k + 1
                    i = i + 1
                else:
                    temp_list.append(items[j])
                    k = k + 1
                    j = j + 1
            while i <= mid_point:
                temp_list.append(items[i])
                k = k + 1
                i = i + 1
            while j <= right:
                temp_list.append(items[j])
                k = k + 1
                j = j + 1
            a = 0
            b = left
            while a < k:
                items[b] = temp_list[a]
                b = b + 1
                a = a + 1

    merge(items, 0, len(items) - 1)

    return items

def quick_sort(items):
    '''Return array of items, sorted in ascending order

    Args:
        items (array): a list or array-like object containing numerical values
    Returns:
        array: items sorted in ascending order
    '''
    if len(items) == 0:
        return items
    partition = len(items) // 2
    left_side = [i for i in items if i < items[partition]]
    mid_point = [i for i in items if i == items[partition]]
    right_side = [i for i in items if i > items[partition]]

    return quick_sort(left_side) + mid_point + quick_sort(right_side)
