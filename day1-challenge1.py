import re
from functools import reduce

FILE_NAME = 'input.txt'

number_list = []

def main():
    read_file(FILE_NAME)
    result(number_list)
    
def read_file(fileName):
    with open(fileName, "r") as input:
        for line in input:
            first_number = search_numbers(line)[0]
            last_number = search_numbers(line)[-1]
            
            number_list.append(concat_numbers(first_number,last_number))
            
def search_numbers(line):
     return re.findall(r'\d', line)
 
def concat_numbers(a, b):
    return int(a + b)

def result(number_list):
    print(reduce(lambda x, y: x+y, number_list))
    
if __name__ == '__main__': main()
