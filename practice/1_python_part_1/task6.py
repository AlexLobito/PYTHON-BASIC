"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    File2Read = open (filename, "r")
    
    StrFile=File2Read.read()
    ListFile = list( filter(None, list(StrFile.split("\n")) ) )
    print(ListFile)
    minF=min(ListFile)
    maxF=max(ListFile)
    
    print(minF,maxF)
    File2Read.close()
    
    return minF, maxF
    

def get_min_max_old(filename: str) -> Tuple[int, int]:
    File2Read = open (filename, "r")
    
    iLine=0
    min=0
    max=0
    
    for Linea2Read in File2Read :
        FileLine=Line2Read.rstrip()
        
        if (iLine == 0) :
            min=FileLine
            max=FileLine
        else :
            if (FileLine > max) :
                max=FileLine
            if (FileLine < min) :
                min=FileLine
                
        iLine=iLine + 1
    print(min, max)
    File2Read.close()
    
    return min, max

get_min_max('somefile.txt')
