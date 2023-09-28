import unittest

from src.exceptions import AroundNotAnInteger, BoundaryNotAnInteger, CurrentPageNotAnInteger, EmptyPage
from src.paginator import Paginator


class TestPaginator(unittest.TestCase):
    def setUp(self):
        self.total_pages = 11
        self.paginator = Paginator(total_pages=self.total_pages)

    def test_base_cases(self):
        for current_page, boundaries, around, excepted in (
            (5, 1, 0, [1, '...', 5, '...', 11]),
            (5, 2, 0, [1, 2, '...', 5, '...', 10, 11]),
            (5, 1, 1, [1, '...', 4, 5, 6, '...', 11]),
            (5, 1, 1, [1, '...', 4, 5, 6, '...', 11]),
            (5, 2, 1, [1, 2, '...', 4, 5, 6, '...', 10, 11]),
            (5, 2, 2, [1, 2, 3, 4, 5, 6, 7, '...', 10, 11]),
            (5, 2, 3, [1, 2, 3, 4, 5, 6, 7, 8, '...', 10, 11]),
            (5, 3, 3, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
            (5, 4, 0, [1, 2, 3, 4, 5, '...', 8, 9, 10, 11]),
            (5, 4, 1, [1, 2, 3, 4, 5, 6, '...', 8, 9, 10, 11]),
            (5, 0, 0, ['...', 5, '...']),
            (5, 0, 3, ['...', 2, 3, 4, 5, 6, 7, 8, '...']),
            (5, 0, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, '...']),
            (5, 0, 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, '...']),
        ):
            self.assertEqual(self.paginator.make_result(current_page, boundaries, around), excepted)

    def test_with_different_current_page(self):
        for current_page, boundaries, around, excepted in (
            (6, 1, 1, [1, '...', 5, 6, 7, '...', 11]),
            (4, 2, 1, [1, 2, 3, 4, 5, '...', 10, 11]),
            (10, 2, 1, [1, 2, '...', 9, 10, 11]),
            (9, 1, 1, [1, '...', 8, 9, 10, 11]),
            (2, 2, 1, [1, 2, 3, '...', 10, 11]),
            (3, 1, 1, [1, 2, 3, 4, '...', 11]),
        ):
            self.assertEqual(self.paginator.make_result(current_page, boundaries, around), excepted)

    def test_minmum_values(self):
        paginator = Paginator(total_pages=1)
        self.assertEqual(paginator.make_result(current_page=1, boundaries=0, around=0), [1])

    def test_maximum_values(self):
        self.assertEqual(
            self.paginator.make_result(current_page=self.total_pages, boundaries=self.total_pages, around=2),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        )

    def test_current_page_errors(self):
        for unexcepted_value, exception, message_error in (
            ('1', CurrentPageNotAnInteger, 'That current page type \"<class \'str\'>\" is not an integer'),
            (0, EmptyPage, 'That current page "0" is less than 1'),
            (12, EmptyPage, 'That current page "12" is greater than total_pages "11"'),
        ):
            with self.assertRaises(exception) as context:
                self.paginator.make_result(current_page=unexcepted_value, boundaries=self.total_pages, around=2)
            self.assertEqual(str(context.exception), message_error)

    def test_boundary_errors(self):
        for unexcepted_value, exception, message_error in (
            ('1', BoundaryNotAnInteger, 'That boundary type \"<class \'str\'>\" is not an integer'),
            (-1, EmptyPage, 'That boundary value "-1" is less than 0'),
            (12, EmptyPage, 'That boundary values "12" is greater than total_pages "11"'),
        ):
            with self.assertRaises(exception) as context:
                self.paginator.make_result(current_page=5, boundaries=unexcepted_value, around=2)
            self.assertEqual(str(context.exception), message_error)

    def test_around_errors(self):
        for unexcepted_value, exception, message_error in (
            ('1', AroundNotAnInteger, 'That around type \"<class \'str\'>\" is not an integer'),
            (-1, EmptyPage, 'That around value "-1" is less than 0'),
            (12, EmptyPage, 'That around values "12" is greater than total_pages "11"'),
        ):
            with self.assertRaises(exception) as context:
                self.paginator.make_result(current_page=5, boundaries=2, around=unexcepted_value)
            self.assertEqual(str(context.exception), message_error)


if __name__ == '__main__':
    unittest.main()
