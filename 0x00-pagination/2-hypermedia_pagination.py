#!/usr/bin/env python3
"""
    Replicate code from the previous task.

    Implement a get_hyper method that takes the same arguments (and defaults)d
    as get_page and returns a dictionary containing the following
    key-value pairs:

    page_size: the length of the returned dataset page
    page: the current page number
    data: the dataset page (equivalent to return from previous task)
    next_page: number of the next page, None if no next page
    prev_page: number of the previous page, None if no previous page
    total_pages: the total number of pages in the dataset as an integer
    Make sure to reuse get_page in your implementation.
    You can use the math module if necessary
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple:
    """
    Calculate the start and end index for a given page and page size.

    Args:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    Tuple: A tuple containing the start index and end index.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()

        try:
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get pagination details including the page size, current page,
            dataset, next and previous pages, and tota pages
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(self.dataset / page_size)

        start, end = index_range(page, page_size)

        # Estimating next and previous pages
        if (page < total_pages):
            next_page = page + 1
        else:
            next_page = None

        if (page == 1):
            prev_page = None
        else:
            prev_page = page - 1

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page
            'prev_page': prev_page
            'total_pages': total_pages
        }
