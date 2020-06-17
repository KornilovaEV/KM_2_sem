import sys
import ast      


def flatten_it(array):
    try:
        if array == []:
            return array
        if isinstance(array[0], list):
            return flatten_it(array[0]) + flatten_it(array[1:])
        return [array[0]] + flatten_it(array[1:])
    except:
        raise ValueError
    
def main():
    if len(sys.argv) > 1:
        array = ast.literal_eval(sys.argv[1])
    else:
        array = [1, [2, 3], "sdfsfss",[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[343434]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]]], [[6, 7]]]
        #array = [0]
        #array[0] = array
    try:
        print(flatten_it(array))
    except ValueError: 
        print('Array that refers to itself')
        
if __name__ == "__main__":
    main()