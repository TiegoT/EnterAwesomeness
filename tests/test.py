from awesomefunctions import myFunction


def test_sum_array():
    """
    make sure sum_array works correctly
    """
    assert myFunction.sum_array([8, 3, 2, 7, 4]) == 24, 'incorrect'
    assert myFunction.sum_array([10, 1, 12, 9, 2]) == 34, 'incorrect'
    assert myFunction.sum_array([1, 2, 3, 4, 5]) == 15, 'incorrect'

def test_fibonacci():
    """
    make sure fibonacci works correctly
    """
    assert myFunction.fibonacci(29) == 514229, 'incorrect'
    assert myFunction.fibonacci(9) == 34, 'incorrect'
    assert myFunction.fibonacci(6) == 8, 'incorrect'

def test_factorial():
    """
    make sure factorial works correctly
    """
    assert myFunction.factorial(15) == 1307674368000, 'incorrect'
    assert myFunction.factorial(10) == 3628800, 'incorrect'
    assert myFunction.factorial(5) == 120, 'incorrect'

def test_reverse():
    """
    make sure reverse works correctly
    """
    assert myFunction.reverse('Vice') == 'eciV', 'incorrect'
    assert myFunction.reverse('reverse_me') == 'em_esrever', 'incorrect'
    assert myFunction.reverse('DoEs_tHis_WoRk?') == '?kRoW_siHt_sEoD', 'incorrect'

def test_bubble_sort():
    """
    make sure bubble_sort works correctly
    """
    assert myFunction.bubble_sort([1, 5, 2, 8, 3]) == [1, 2, 3, 5, 8], 'incorrect'
    assert myFunction.bubble_sort([3, 45, 1, 2, 34]) == [1, 2, 3, 34, 45], 'incorrect'
    assert myFunction.bubble_sort([10, 1, 12, 9, 2]) == [1, 2, 9, 10, 12], 'incorrect'

def test_merge_sort():
    """
    make sure merge_sort works correctly
    """
    assert myFunction.merge_sort([1, 5, 2, 8, 3]) == [1, 2, 3, 5, 8], 'incorrect'
    assert myFunction.merge_sort([3, 45, 1, 2, 34]) == [1, 2, 3, 34, 45], 'incorrect'
    assert myFunction.merge_sort([10, 1, 12, 9, 2]) == [1, 2, 9, 10, 12], 'incorrect'

def test_quick_sort():
    """
    make sure quick_sort works correctly
    """
    assert myFunction.quick_sort([1, 5, 2, 8, 3]) == [1, 2, 3, 5, 8], 'incorrect'
    assert myFunction.quick_sort([3, 45, 1, 2, 34]) == [1, 2, 3, 34, 45], 'incorrect'
    assert myFunction.quick_sort([10, 1, 12, 9, 2]) == [1, 2, 9, 10, 12], 'incorrect'
