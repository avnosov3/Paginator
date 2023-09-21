from src import constants
from src.exceptions import AroundNotAnInteger, BoundaryNotAnInteger, CurrentPageNotAnInteger, EmptyPage


class Paginator:
    def __init__(self, total_pages, hidden_pages='...'):
        self.total_pages = total_pages
        self.hidden_pages = hidden_pages

    def validate(self, current_page, boundaries, around):
        for exception, message, value in (
            (CurrentPageNotAnInteger, constants.CURRENT_PAGE_INVALID_TYPE_ERROR_MESSAGE, current_page),
            (BoundaryNotAnInteger, constants.BOUNDARY_INVALID_TYPE_ERROR_MESSAGE, boundaries),
            (AroundNotAnInteger, constants.AROUND_INVALID_TYPE_ERROR_MESSAGE, around),
        ):
            if not isinstance(value, int):
                raise exception(message.format(type(value)))
        if current_page < 1:
            raise EmptyPage(constants.MIN_CURRENT_PAGE_ERROR_MESSAGE.format(str(current_page)))
        for message, value in (
            (constants.MIN_BOUNDARY_ERROR_MESSAGE, boundaries),
            (constants.MIN_AROUND_ERROR_MESSAGE, around),
        ):
            if value < 0:
                raise EmptyPage(message.format(str(value)))
        for message, value in (
            (constants.CURRENT_PAGE_IS_GREATER_TOTAL_PAGES, current_page),
            (constants.BOUNDARY_IS_GREATER_TOTAL_PAGES, boundaries),
            (constants.AROUND_IS_GREATER_TOTAL_PAGES, around),
        ):
            if value > self.total_pages:
                raise EmptyPage(message.format(value, self.total_pages))
        return current_page

    @property
    def page_range(self):
        return range(1, self.total_pages + 1)

    def create_footer(self, current_page, boundaries, around):
        current_page = self.validate(current_page, boundaries, around)

        if self.total_pages <= (around + boundaries) * 2:
            yield from self.page_range
            return

        if current_page >= (1 + around + boundaries) + 1:
            yield from range(1, boundaries + 1)
            yield self.hidden_pages
            yield from range(current_page - around, current_page + 1)
        else:
            yield from range(1, current_page + 1)

        if current_page <= (self.total_pages - around - boundaries) - 1:
            yield from range(current_page + 1, current_page + around + 1)
            yield self.hidden_pages
            yield from range(self.total_pages - boundaries + 1, self.total_pages + 1)
        else:
            yield from range(current_page + 1, self.total_pages + 1)

    def make_result(self, current_page, boundaries, around):
        return list(self.create_footer(current_page, boundaries, around))


if __name__ == '__main__':
    paginator = Paginator(total_pages=int(input()))
    print(*paginator.make_result(*map(int, input().split())))
