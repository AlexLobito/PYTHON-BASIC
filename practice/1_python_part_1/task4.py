"""
Write function which receives list of integers. Calculate power of each integer and
subtract difference between original previous value and it's power. For first value subtract nothing.
Restriction:
Examples:
    >>> calculate_power_with_difference([1, 2, 3])
    [1, 4, 7]  # because [1^2, 2^2 - (1^2 - 1), 3^2 - (2^2 - 2)]
"""
from typing import List


def calculate_power_with_difference(ints: List[int]) -> List[int]:
    ListResult=[]
    
    lastsquareelem=0
    for elem in ints :
        elem2List=elem**2 - (lastsquareelem**2 - lastsquareelem)
        lastsquareelem=elem
        ListResult.append(elem2List)
        print(elem2List)
        
    return ListResult


calculate_power_with_difference([1, 2, 3])
