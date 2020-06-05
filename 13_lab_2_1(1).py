import math as mth
import sys
import ast      
           
def build_blocks(arr):
    blocks = [0]*block_size
    i = 0
    while (i <= len(arr)-1):
        blocks[mth.floor(i/block_size)] += arr[i]
        i += 1
    return blocks
            
def summin(left, right, arr):
    blocks = build_blocks(arr)
    start_block = mth.floor(left/block_size)
    end_block = mth.floor(right/block_size)
    sum = 0
    if start_block == end_block:
        exp = left
        while (exp <= right):
            sum += array[exp]
            exp += 1
    else:
        i = left
        while (i <= (start_block+1)*block_size - 1):
            sum += array[i]
            i += 1 
        j = end_block*block_size
        while (j <= right):
            sum += array[j]
            j += 1
        k = start_block + 1
        while (k <= end_block - 1):
            sum += blocks[k]
            k += 1
    return sum

if len(sys.argv) == 1:
    print("Welcome! To find the sum of elements from L through R in an array,",
      "please follow the instructions below.")
    
    while True:
        try:    
            array = input("Enter the array using the spacebar: ")
            array = [float(x) for x in array.split()]
            break
        except:
            print()
            print("Please, enter valid elements (of interger or float types)",
                          "for the array.")
                
    while True:
        while True:
            try:
                L = int(input("Enter the starting index (L): "))
                R = int(input("Enter the ending index (R): "))
                break
            except:
                print()
                print("Please, enter valid indexes (of integer type).")
            
        if R > len(array)-1 or L > len(array)-1:
            print()
            print("Please, enter indexes smaller than",
                              "the length of the array.")
        else:
            if L > R:
                print()
                print("Please, enter a starting index (L) smaller than",
                          "the ending index (R).")
            else: break
        
else:
    file = open(sys.argv[1]);
    arr = file.read(); 
    arr = arr.split('\n');
    try:
        array = ast.literal_eval(arr[0])
        print("The array: ", array)
        L = int(arr[1])
        R = int(arr[2]) 
    except:
        print("Invalid data was entered. Please check your file.")
        quit()
    
block_size = mth.ceil(len(array)**(0.5))
print()
print("The sum of elements from {0} through {1}".format(L,R),
              "in the array equals {0}".format(summin(L,R,array)))