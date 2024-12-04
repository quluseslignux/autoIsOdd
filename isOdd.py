import sys
def generate(n:int)->None:
    file = open('gened.py', 'w+')
    isOdd=True
    file.write("def isOdd(n)->bool:\n")
    file.write("\tif n==1:\n")
    file.write("\t\treturn "+str(isOdd)+"\n")
    isOdd=not isOdd
    for i in range(2,n+1):
        file.write("\telif n=="+str(i)+":\n")
        file.write("\t\treturn "+str(isOdd)+"\n")
        isOdd=not isOdd

def run(n:int)->bool:
    import gened
    return gened.isOdd(n)

def isOdd(n:int)->bool:
    generate(n)
    return run(n)

def main()->None:
    if len(sys.argv) < 2:
        n=input("Type in the input: ")
    else:
        n=sys.argv[1]
    n=int(n)
    print(isOdd(n))

if __name__ == "__main__":
    main()
