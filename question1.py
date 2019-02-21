# -*- coding: utf-8 -*-
"""
Created on Thu 21 Feb 2018
@author: Trung Hoang
"""

### Executalbe with python3 ###
### On terminal: python3 question1.py tornik-map-20171006.10000.tsv

import pdb  # debugger
import re  # regular expression
import sys

def read_file(file_name):
    log = []
    with open(file_name, 'r') as file:
        content = file.readlines()
    log = [x.split('\t') for x in content]
    return(log)

def mapper(log):
    data = []
    # Check for the prefix
    assert log[0][1][:14]=='/map/1.0/slab/'  # True
    
    for line in log:
        if (len(line)>1) and (line[1][:14]=='/map/1.0/slab/'):
            t = re.match('(\w+)', line[1][14:])
            if t.group(0) is not None:
                data.append((t.group(0), 1))
    return(data)

def reducer(data):
    result = []
    current_category = None
    current_count = 0
    category = None
    for item in data:
        # pdb.set_trace()
        category, count = item[0], item[1]
        if current_category == category:
            current_count += count
        else:
            if current_category:
                result.append((current_category, current_count))
            current_count = count
            current_category = category
    return(result) 

def main(file_name, seperator='\t'):
    # file_name = 'tornik-map-20171006.10000.tsv'
    log = read_file(file_name)
    print(log[:5])
    data = mapper(log)
    print(data[:5])
    result = reducer(data)

    # write output to txt
    with open('log1.txt', 'w') as file:
        [file.write('{}{}{}\n'.format(line[0], seperator, line[1])) for line in result]

if  __name__== '__main__':
    if len(sys.argv) == 1:
        raise Exception('Please enter the name of tsv file as an argument!\n ex: python3 question1.py tornik-map-20171006.10000.tsv')
    else:
        main(sys.argv[1])
    




        