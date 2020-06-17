import sys
from ast import literal_eval
from re import search

def to_json(obj):
    try:
        if (type(obj) in (float, int, str, tuple, dict, list, bool) 
            or obj == None):
            if type(obj) == str:
                obj = '"' + obj + '"'
            if type(obj) == int or type(obj) == float:
                obj = str(obj)
            if type(obj) == None:
                obj = 'null'
            if type(obj) == bool:
                if obj == True:
                    obj = 'true'
                else:
                    obj = 'false'              
            if type(obj) == dict:
                line = ''
                i = 0
                for item in obj.items():
                    line += to_json(item[0]) + ' : ' + to_json(item[1])
                    if i < len(obj) - 1:
                        line += ', '
                        i += 1
                    else: break
                obj = '{' + line + '}'
            if type(obj) == list or type(obj) == tuple:
                line = ''
                for element in range(len(obj)):
                    line += to_json(obj[element])
                    if element < len(obj) - 1:
                        line += ', '
                    else: break
                obj = '[' + line + ']'
        return obj
                        
                
                
    except ValueError:
        print("Your object in question is not a type from this list: ")
        print("float, int, str, tuple, dict, list, None, bool")
        
def main():
    if len(sys.argv) > 1:
        try:
            fileName = sys.argv[1]
            if search(r'\b.txt\b', fileName):
                file = open(fileName, "r")
                obj = file.read()
                try:
                    obj = literal_eval(obj)
                except:
                    obj = obj
            else:
                try:
                    obj = literal_eval(obj)
                except:
                    obj = obj
                
        except:    
            print("You are not enter .txt file or you enter a space in the",
              "line command.")
            print("Please, write file without space and with .txt format ")
            sys.exit()
    else:
        obj = input("Enter your words: ")
        try:
            try:
                obj = literal_eval(obj)
            except:
                obj = obj
                
            
        except ValueError: 
            print("Your object in question is not a type from this list: ")
            print("float, int, str, tuple, dict, list, None, bool")
        
    print(to_json(obj))    
        
if __name__ == "__main__":
    main()