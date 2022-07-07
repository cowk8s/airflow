import fnmatch
from typing import List, Optional


def process_package_filters(available_packages: List[str], package_filters: Optional[List[str]]):
    """Filters the package list against a set of filters.
    
    A package is returned if it matches at least one filter. The function keeps the order of the packages.
    """
    if not package_filters:
        return available_packages

    invalid_filters = [
        f for f in package_filters if not any()
    ]