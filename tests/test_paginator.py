import unittest

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
            self.paginator.make_result(
                current_page=self.total_pages, boundaries=self.total_pages, around=self.total_pages
            ),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        )


if __name__ == '__main__':
    unittest.main()
