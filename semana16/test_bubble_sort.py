from bubble_sort import my_bubble
from random import randint
from pytest import raises

def test_my_bubble_works_with_short_lists():
    #arrange
    element_list = [64, 34, 25, 12, 22, 11, 90]
    #act
    result = my_bubble(element_list)
    #assert
    assert result == [11, 12, 22, 25, 34, 64, 90]

def test_my_bubble_works_with_long_lists():
    #arrange
    element_list = [item for item in range(150)]
    #act
    result = my_bubble(element_list)
    element_list.sort()
    #assert
    assert result == element_list

def test_my_bubble_works_with_empty_lists():
    #arrange
    element_list = []
    #act
    result = my_bubble(element_list)
    #assert
    assert result == []

def test_my_bubble_fails_with_non_list_elements_type_error():
    #arrange
    element_list = 90
    #act & assert
    with raises(TypeError):
        my_bubble(element_list)
    


