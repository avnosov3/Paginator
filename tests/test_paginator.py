import unittest

from tests.cases import (
    CASES_WHERE_TOTAL_PAGES_VALUE_IS_BIG,
    CASES_WHERE_TOTAL_PAGES_VALUE_IS_ELEVEN,
    CASES_WHERE_TOTAL_PAGES_VALUE_IS_FIVE,
    CASES_WHERE_TOTAL_PAGES_VALUE_IS_FOUR,
)

from src.paginator import Paginator


class TestPaginator(unittest.TestCase):
    def test_paginator_where_total_pages_value_is_four(self):
        total_pages = 4
        for current_page, boundaries, around, expected in CASES_WHERE_TOTAL_PAGES_VALUE_IS_FOUR:
            with self.subTest(
                total_pages=total_pages,
                current_page=current_page,
                boundaries=boundaries,
                around=around,
                expected=expected,
            ):
                self.assertEqual(
                    Paginator(total_pages, current_page, boundaries, around).calculating_list_of_pages(), expected
                )

    def test_paginator_where_total_pages_value_is_big(self):
        for total_pages, current_page, boundaries, around, expected in CASES_WHERE_TOTAL_PAGES_VALUE_IS_BIG:
            with self.subTest(
                total_pages=total_pages,
                current_page=current_page,
                boundaries=boundaries,
                around=around,
                expected=expected,
            ):
                self.assertEqual(
                    Paginator(total_pages, current_page, boundaries, around).calculating_list_of_pages(), expected
                )

    def test_paginator_where_total_pages_value_is_five(self):
        total_pages = 5
        for current_page, boundaries, around, expected in CASES_WHERE_TOTAL_PAGES_VALUE_IS_FIVE:
            with self.subTest(
                total_pages=total_pages,
                current_page=current_page,
                boundaries=boundaries,
                around=around,
                expected=expected,
            ):
                self.assertEqual(
                    Paginator(total_pages, current_page, boundaries, around).calculating_list_of_pages(), expected
                )

    def test_paginator_where_total_pages_value_is_eleven(self):
        total_pages = 11
        for current_page, boundaries, around, expected in CASES_WHERE_TOTAL_PAGES_VALUE_IS_ELEVEN:
            with self.subTest(
                total_pages=total_pages,
                current_page=current_page,
                boundaries=boundaries,
                around=around,
                excepted=expected,
            ):
                self.assertEqual(
                    Paginator(total_pages, current_page, boundaries, around).calculating_list_of_pages(), expected
                )

    def test_minmum_values(self):
        self.assertEqual(
            Paginator(total_pages=1, current_page=1, boundaries=0, around=0).calculating_list_of_pages(), [1]
        )

    def test_maximum_values(self):
        self.assertEqual(
            Paginator(total_pages=11, current_page=11, boundaries=11, around=2).calculating_list_of_pages(),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        )

    def test_total_pages(self):
        for unexcepted_value, exception, message_error in (
            ('1', TypeError, 'Type \"<class \'str\'>\" of total pages is not an integer'),
            (0, ValueError, 'Value "0" of total pages is less than 1'),
        ):
            with self.subTest(unexcepted_value=unexcepted_value, exception=exception, message_error=message_error):
                with self.assertRaises(exception) as context:
                    Paginator(
                        total_pages=unexcepted_value, current_page=2, boundaries=8, around=2
                    ).calculating_list_of_pages()
                self.assertEqual(str(context.exception), message_error)

    def test_current_page_errors(self):
        for unexcepted_value, exception, message_error in (
            ('1', TypeError, 'Type \"<class \'str\'>\" of current page is not an integer'),
            (0, ValueError, 'Value "0" of current page is less than 1'),
            (12, ValueError, 'Value "12" of current  page is bigger than total pages "11"'),
        ):
            with self.subTest(unexcepted_value=unexcepted_value, exception=exception, message_error=message_error):
                with self.assertRaises(exception) as context:
                    Paginator(
                        total_pages=11, current_page=unexcepted_value, boundaries=8, around=2
                    ).calculating_list_of_pages()
                self.assertEqual(str(context.exception), message_error)

    def test_boundary_errors(self):
        for unexcepted_value, exception, message_error in (
            ('1', TypeError, 'Type \"<class \'str\'>\" of boundaries is not an integer'),
            (-1, ValueError, 'Value "-1" of boundaries is less than 0'),
        ):
            with self.subTest(unexcepted_value=unexcepted_value, exception=exception, message_error=message_error):
                with self.assertRaises(exception) as context:
                    Paginator(
                        total_pages=11, current_page=1, boundaries=unexcepted_value, around=2
                    ).calculating_list_of_pages()
                self.assertEqual(str(context.exception), message_error)

    def test_around_errors(self):
        for unexcepted_value, exception, message_error in (
            ('1', TypeError, 'Type \"<class \'str\'>\" of around is not an integer'),
            (-1, ValueError, 'Value "-1" of around is less than 0'),
        ):
            with self.subTest(unexcepted_value=unexcepted_value, exception=exception, message_error=message_error):
                with self.assertRaises(exception) as context:
                    Paginator(
                        total_pages=11, current_page=1, boundaries=2, around=unexcepted_value
                    ).calculating_list_of_pages()
                self.assertEqual(str(context.exception), message_error)


if __name__ == '__main__':
    unittest.main()
