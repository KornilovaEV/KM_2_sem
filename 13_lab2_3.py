#В алгоритме MergeSort подразумевается, что каждая строка исходного и
#конечного файлов написана с новой строчки.
import math as mth
import sys

def ProgBar(i, Range):
    PER =  mth.floor(i/Range*100)
    PRBAR = '#'*mth.floor(PER/2)+' '*mth.ceil((100-PER)/2)
    sys.stdout.write('\rProgress: |{1}| [{0}%] '.format(PER, PRBAR))
    sys.stdout.flush()

def Sort(Arr):
    FinArr = []
    Range = len(Arr)
    for i in range(len(Arr)):
        FinArr.append(min(Arr))
        Arr.remove(min(Arr))
        if flag:
            ProgBar(i, Range-1)
    return FinArr

def MergeSort(InFile, OutFile):
    global flag
    file = open(InFile)
    text = file.read().split("\n")
    print("\nSorting the words in the lines."); flag = False
    for i in range(len(text)):
        text[i] = " ".join(Sort(text[i].split()))
        ProgBar(i, len(text)-1)
    print("\nSorting the lines in the text."); flag = True
    text = "\n".join(Sort(text))
    file = open(OutFile, "w")
    file.write(text)
    file.close()
    print("\nDone!")

if len(sys.argv) == 1:
    names = input("Enter names of the input and" + \
                  " output files using the spacebar: ").split()
    InFile = names[0]; OutFile = names[1] 
else:
    if len(sys.argv) == 2:
        names = open(sys.argv[1]).read().split("\n")
        InFile = names[0]; OutFile = names[1]
    else:
        InFile = sys.argv[1]; OutFile = sys.argv[2]

MergeSort(InFile, OutFile)