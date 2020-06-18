import re
import sys
from ast import literal_eval

def Number(num):
    num = str(num)
    return num

def String(string):
    string = '\"' + string + '\"'
    return string

def BoolNone(boo):
    trans = {True:'true', False:'false', None:'null'}
    boo = trans[boo]
    return boo

def Dictionary(dictary):
    result = '{'
    for key, value in dictary.items():
        result += ', ' + to_json(key) + ': ' + to_json(value)
    result = re.sub(', ', '' , result + '}' , count = 1)
    return result

def Array(arr):
    result = '['
    for elem in arr:
        if type(elem) == str:
            elem = String(elem)
        if type(elem) == int or type(elem) == float:
            elem = Number(elem)
        if type(elem) == bool or elem == None:
            elem = BoolNone(elem)
        if type(elem) == list or type(elem) == tuple:
            elem = Array(elem)
        if type(elem) == dict:
            elem = Dictionary(elem)
        result += ', ' + elem
    result = re.sub(', ', '' , result + ']' , count = 1)
    return result

def to_json(obj):
    if type(obj) == str:
        obj = String(obj)
    if type(obj) == int or type(obj) == float:
        obj = Number(obj)
    if type(obj) == list or type(obj) == tuple:
        obj = Array(obj)
    if type(obj) == bool or obj == None:
        obj = BoolNone(obj)
    if type(obj) == dict:
        obj = Dictionary(obj)
    return obj

if len(sys.argv) == 1:
    obj = input("Enter the object to convert to JSON: ")
else:
    obj = open(sys.argv[1]).read()
    
try:
    obj = literal_eval(obj)
except:
    obj = obj
    
print("\nThe original object: ", obj)
print("\nThe converted object: ", to_json(obj))
