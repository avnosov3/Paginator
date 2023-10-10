## Important Information (about how the exercise was accomplished, not how the code works)
I would like to draw your attention to the fact that I used an off-the-shelf [solution](https://github.com/django/django/blob/main/django/core/paginator.py) from the Django framework as the base for this exercise. I found this way to be the most efficient, as I knew how it worked and understood how it could be adapted to the current exercise.



## Project Description
Footer with pagination to browse through the several pages of a given website.

Variables:

- current_page

- total_pages

- boundaries: how many pages we want to link in the beginning, or end (meaning, how many pages starting at page 1 and how many leading up to the last page, inclusive)

- around: how many pages we want to link before and after the current page, exclusive.

For pages with no direct link we should use one set of three points (...) per set of pages hidden.

## Stack
* python 3.10
* pre-commit 3.4.0
* poetry 1.5.1


## Project launch
1. Run that command
```
python -m src.paginator
```
2. Input values in command line like in an example
```
INPUT
11 4 0 1 [total_pages, current_page, boundaries, around]
OUTPUT
... 3 4 5 ...

P.S. Don't input these brackets with words [words]
```
3. Run tests
```
python -m unittest tests.test_paginator
```
