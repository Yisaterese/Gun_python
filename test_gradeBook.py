import pytest

from gradeBook import GradeBook


@pytest.fixture
def gradeBook():
    return GradeBook()


def test_search_Course_name(gradeBook):
    name = gradeBook.set_name("Dayo")
    assert gradeBook.get_name() is name

def test_minimum_grade(gradeBook):
    added_numbers = gradeBook.add(2, 3, 4, 1, 4, 57, 5)
    assert gradeBook.get_minimum(added_numbers) == 1


def test_maximum_grade(gradeBook):
    assert gradeBook.get_maximum([2, 4, 3, 6, 5, 1]) == 6


def test_average_of_elements(gradeBook):
    average_of_values =  gradeBook.get_maximum([2, 4, 3, 6, 5, 1])
    assert gradeBook.get_average is 21.00
