
 
from typing import List

def sum_list(numbers: List[int]) -> int:
    total = 0  
    for number in numbers:  
        total += number  
    return total 


numbers = [10, 20, 30, 40, 50]  
result = sum_list(numbers)  
print(result)  