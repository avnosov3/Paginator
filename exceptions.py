class UnorderedObjectListWarning(RuntimeWarning):
    pass


class InvalidPage(Exception):
    pass


class CurrentPageNotAnInteger(InvalidPage):
    pass


class BoundaryNotAnInteger(InvalidPage):
    pass


class AroundNotAnInteger(InvalidPage):
    pass


class EmptyPage(InvalidPage):
    pass
