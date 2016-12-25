# Heaps: Find the Running Median
# https://www.hackerrank.com/challenges/ctci-find-the-running-median
# Given an input stream of  integers, you must perform the following task for each  integer:
# 
# - Add the  integer to a running list of integers.
# - Find the median of the updated list (i.e., for the first element through the  element).
# - Print the list's updated median on a new line. The printed value must be a double-precision number scaled to decimal place (i.e.,  format).
# 
# Solution: use two heap, one min heap and one max heap, each containing greater or the lesser half of the data.
# The two heap are kept in balance so the medium must be one of them or their average.

from heaps import *

