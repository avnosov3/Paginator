class Paginator:
    default_error_messages = {
        'invalid_type_of_total_pages': 'Type "{type}" of total pages is not an integer',
        'invalid_type_of_current_page': 'Type "{type}" of current page is not an integer',
        'invalid_type_of_boundaries': 'Type "{type}" of boundaries is not an integer',
        'invalid_type_of_around': 'Type "{type}" of around is not an integer',
        'invalid_value_of_total_pages': 'Value "{value}" of total pages is less than 1',
        'invalid_value_of_current_page': 'Value "{value}" of current page is less than 1',
        'invalid_value_of_boundaries': 'Value "{value}" of boundaries is less than 0',
        'invalid_value_of_around': 'Value "{value}" of around is less than 0',
        'big_value_of_current_page': 'Value "{value}" of current  page is bigger than total pages "{total_pages}"',
    }

    def __init__(self, total_pages, current_page, boundaries, around, hidden_pages='...'):
        self.total_pages = total_pages
        self.current_page = current_page
        self.boundaries = boundaries
        self.around = around
        self.hidden_pages = hidden_pages

    def validate(self):
        for message, value in (
            (self.default_error_messages['invalid_type_of_total_pages'], self.total_pages),
            (self.default_error_messages['invalid_type_of_current_page'], self.current_page),
            (self.default_error_messages['invalid_type_of_boundaries'], self.boundaries),
            (self.default_error_messages['invalid_type_of_around'], self.around),
        ):
            if not isinstance(value, int):
                raise TypeError(message.format(type=type(value)))
        for message, value in (
            (self.default_error_messages['invalid_value_of_total_pages'], self.total_pages),
            (self.default_error_messages['invalid_value_of_current_page'], self.current_page),
        ):
            if value < 1:
                raise ValueError(message.format(value=value))
        for message, value in (
            (self.default_error_messages['invalid_value_of_boundaries'], self.boundaries),
            (self.default_error_messages['invalid_value_of_around'], self.around),
        ):
            if value < 0:
                raise ValueError(message.format(value=value))
        if self.current_page > self.total_pages:
            raise ValueError(
                self.default_error_messages['big_value_of_current_page'].format(
                    value=self.current_page, total_pages=self.total_pages
                )
            )

    def create_footer(self):
        self.validate()

        last_page = self.total_pages + 1

        if self.boundaries * 2 >= self.total_pages:
            yield from range(1, last_page)
            return

        if self.boundaries > self.around + self.current_page:
            yield from range(1, self.boundaries + 1)
            yield self.hidden_pages
            yield from range(self.total_pages - self.boundaries + 1, last_page)
            return

        if self.current_page >= (self.around + self.boundaries + 1) + 1:
            right_boundary_position = self.total_pages - self.boundaries + 1
            if self.current_page - right_boundary_position >= self.around:
                yield from range(1, self.boundaries + 1)
                yield self.hidden_pages
                yield from range(right_boundary_position, last_page)
                return
            yield from range(1, self.boundaries + 1)
            yield self.hidden_pages
            yield from range(self.current_page - self.around, self.current_page + 1)
        else:
            yield from range(1, self.current_page + 1)

        if self.current_page <= (self.total_pages - self.around - self.boundaries) - 1:
            yield from range(self.current_page + 1, self.current_page + self.around + 1)
            yield self.hidden_pages
            yield from range(self.total_pages - self.boundaries + 1, last_page)
        else:
            yield from range(self.current_page + 1, last_page)

    def calculating_list_of_pages(self):
        return list(self.create_footer())


if __name__ == '__main__':
    print(*Paginator(*map(int, input().split())).calculating_list_of_pages())
