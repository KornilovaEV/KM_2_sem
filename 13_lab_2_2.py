import random
import sys
import math as mth
from os import stat
from ast import literal_eval

def RandWord(L):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a, b = L
    str = ""
    while len(str) < random.randrange(a,b+1):
        str += random.choice(letters)
    return str

def RandLine(K, L):
    a, b = K
    str = " ".join(RandWord(L) for ind in range(random.randrange(a,b+1)))
    return str

def ProgBar(Name, MB):
    PER =  mth.floor(stat(Name).st_size/(MB*1024*1024)*100)
    PRBAR = '#'*mth.floor(PER/2)+' '*mth.ceil((100-PER)/2)
    sys.stdout.write('\rProgress: |{1}| [{0}%] '.format(PER, PRBAR))
    sys.stdout.flush()

def WriteFile(Name, MB, K, L):
    file = open(Name,"w")
    while stat(Name).st_size < MB*1024*1024:
        file.write(RandLine(K, L) + "\n")
        ProgBar(Name, MB)
    file.close()
    print("Done!")
    
def CheckTuples(Tup):
    try:
        Tup = literal_eval(Tup)
        if type(Tup) != tuple or len(Tup) != 2:
            print("The entered tuple is invalid.")
            sys.exit(0)
    except:
        print("The entered tuple is invalid.")
        sys.exit(0)
    return Tup
    
print("In order to use the default values of L and K, enter DEF for each.")
if len(sys.argv) == 1:
    args = input("Enter the arguments ('name.txt', MB, K, L)" \
        " using the spacebar: ").split()
    Name = args[0]; MB = args[1]; K_L = args[2:4]
else:
    Name = sys.argv[1]; MB = sys.argv[2]; K_L = sys.argv[3:5]

if Name.find('.txt') < 0:
    print("The entered name is invalid.")
    sys.exit(0)

try:
    MB = float(MB)
except:
    print("The entered number for MB is invalid (not of float type).")
    sys.exit(0)

DEF = ((10,100),(3,10))
for i in range(2):
    if K_L[i] == 'DEF':
        K_L[i] = DEF[i]
    else:
        K_L[i] = CheckTuples(K_L[i])
    
WriteFile(Name, MB, K_L[0], K_L[1])