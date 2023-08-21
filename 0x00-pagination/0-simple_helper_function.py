#!/usr/bin/env python3
"""
index_range helper function
"""
from typing import Tuple

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
