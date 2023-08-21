#!/usr/bin/env python3
"""
Server Class paginates db of popular baby names
"""

import csv
import math
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Args:
    page : page num to be return
    page_size: num of items per page
    Return:
    tuple(start_index, end_index)
    """
    start, end = 0, 0
    for i in range(page):
        start = end
        end += page_size
    return (start, end)

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
            """
            Args:
            page: required page num. +ve int
            page_size : num of records per page. +ve int.
            Return:
            list of lists containing required from dataset
            """
            assert type(page) is int and page > 0
            assert type(page_size) is int and page_size > 0

            dataset = self.dataset()
            data_length = len(dataset)

            try:
                index = index_range(page, page_size)
                return dataset[index[0]:index[1]]
            except IndexError:
                return []
