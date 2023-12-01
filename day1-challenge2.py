import re
from functools import reduce

FILE_NAME = 'input.txt'

number_dictionary = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
    "ten" : 10,
}

number_list = []

def main():
    read_file(FILE_NAME)
    result(number_list)
    
def read_file(fileName):
    with open(fileName, "r") as input:
        for line in input:
           
            first_number = search_numbers(line)[0]
            last_number = search_numbers(line)[-1]
        
            number_list.append(concat_numbers(replace_word_numbers(first_number),replace_word_numbers(last_number)))
            
def search_numbers(line):
     return re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
 
def replace_word_numbers(string,number_dictionary_keys = number_dictionary.keys()):

    for key in number_dictionary_keys:
        if string == key:
            return string.replace(string, str(number_dictionary[key]))
    
    return string
 
def concat_numbers(a, b):
    return int(a + b)

def result(number_list):
    print(reduce(lambda x, y: x+y, number_list))
    
if __name__ == '__main__': main()
