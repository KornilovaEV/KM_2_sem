
import re
import sys

def Number(num):
    try:
       num = int(num)
    except:
        num = float(num)
    return num

def String(stry):
    stry = re.sub('\"','',stry)
    return stry

def BoolNone(boo):
    trans = {'true':True, 'false':False, 'null':None}
    boo = trans[boo]
    return boo

def Indecies(string, words):
    ind = []
    start = 0
    for word in words:
        ind.append(string.find(word, start))
        start = string.find(word,start) + len(word)
    return ind

def Array(arr):
    patterns = ['(\[.*?\])','(\".*?\")','[0-9]*\.[0-9]*|[0-9]+','[a-z]+']
    funcs = [Array, String, Number, BoolNone]
    arrhelp = arr
    arr = re.sub('^\[|\]$','',arr)
    result = []
    elems = [0]*4
    ind = []
    for i in range(4):
        elems[i] = re.findall(patterns[i], arr)
        ind += Indecies(arrhelp,elems[i])
        result += list(map(funcs[i], elems[i]))
        for el in elems[i]:
            arr = arr.replace(el, '')
    result = [x for _,x in sorted(zip(ind,result))]
    return result

def Dictionary(dicty):
    elem = []
    pattern = '(?<=\{)(.*?|\{.*?\}|\[.*?\]):(\[.*?\]|\{.*?\}|.*?)(?=\,|\})'
    while len(dicty) > 2:
        elem += re.findall(pattern,dicty)
        dicty = re.sub(pattern,'',dicty)
        dicty = re.sub('(?<=\{)(\,\s+|\,)','',dicty)
    new_dicty = {}
    for el in elem:
        new_dicty[from_json(el[0])] = from_json(el[1])
    return new_dicty

def from_json(obj):
    patterns = ['(\{.*\})','(\[.*\])','(\".*?\")',\
                '[0-9]*\.[0-9]*|[0-9]+','[a-z]+']
    funcs = [Dictionary, Array, String, Number, BoolNone]
    for i in range(5):
        objhelp = re.findall(patterns[i],obj)
        if len(objhelp) != 0:
            objhelp = list(map(funcs[i], objhelp))
            break
    return objhelp[0]

if len(sys.argv) == 1:
    obj = input("Enter the object to convert from JSON: ")
else:
    obj = open(sys.argv[1]).read()
    
print("\nThe original object: ", obj)
print("\nThe converted object: ", from_json(obj))
    
