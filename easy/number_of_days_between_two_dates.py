https://leetcode.com/problems/number-of-days-between-two-dates


import math
import datetime
from datetime import date

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        arr1 = list(map(int, date1.split("-")))
        arr2 = list(map(int, date2.split("-")))
        
        dt1 = date(arr1[0], arr1[1], arr1[2])
        dt2 = date(arr2[0], arr2[1], arr2[2])
         
        return abs((dt2-dt1).days) 
