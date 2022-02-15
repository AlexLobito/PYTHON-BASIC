"""
Write function which receives line of space sepparated words.
Remove all duplicated words from line.
Restriction:
Examples:
    >>> remove_duplicated_words('cat cat dog 1 dog 2')
    'cat dog 1 2'
    >>> remove_duplicated_words('cat cat cat')
    'cat'
    >>> remove_duplicated_words('1 2 3')
    '1 2 3'
"""
def remove_duplicated_words(line: str) -> str:
    used=set()
    List=line.split(" ")
    uniqueList = [x for x in List if x not in used and (used.add(x) or True)]
    print(list(uniqueList))
    

def remove_duplicated_words2(line: str) -> str:
    tempList=[]
    
    data=line.split(" ")
    tempList=data.copy()
    tempList=set(tempList)
    print(tempList)
    
remove_duplicated_words('cat cat dog 1 dog 2')
remove_duplicated_words('cat cat cat')
remove_duplicated_words('1 2 3')
