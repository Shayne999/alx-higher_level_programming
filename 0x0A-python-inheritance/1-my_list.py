#!/usr/bin/python3
"""Defines MyList, an inherited list class."""


class MyList(list):
    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
