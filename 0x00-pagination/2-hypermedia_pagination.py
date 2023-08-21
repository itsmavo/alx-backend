#!/usr/bin/env python3
"""
Server class with methods to create simple pagination from csv data
"""
import csv
from typing import List
index_range = __import__('0-simple_helper_function').index_range

class Server:
    """ paginates db of popular baby names """
    Data_set = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """ Reads csv file and returns dataset """
        if self.__dataset is None:
            with open(self.Data_set) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
                self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def assert_positive_integer_type(value: int) -> None:
        """
        Args:
        value: val to be asserted
        """
        assert type(value) is int and value > 0

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Args:
        page: page num
        page_size: num of items per page
        Return:
        List[List]: page of dataset
        """
        self.assert_positive_integer_type(page)
        self.assert_positive_integer_type(page_size)
        dataset = self.dataset()
        start, end = index_range(page, page_size)
        try:
            data = dataset[start:end]
        except IndexError:
            data = []
        return data

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Args:
        page: page num
        page_size: items per page
        Returns:
        List[List]: page of the dataset
        """
        total_pages = len(self.dataset()) // page_size + 1
        data = self.get_page(page, page_size)
        info = {
            "page": page,
            "page_size": page_size if page_size <= len(data) else len(data),
            "total_pages": total_pages,
            "data": data,
            "prev_page": page - 1 if page > 1 else None,
            "next_page": page + 1 if page + 1 <= total_pages else None
        }
        return info

