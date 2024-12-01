import sys
def generate(n):
    file = open('gened.py', 'w+')
    isOdd=True
    file.write("def isOdd(n):\n")
    #file.write("n=int(sys.argv[1])\n")
    file.write("\tif n==1:\n")
    file.write("\t\tprint("+str(isOdd)+")\n")
    isOdd=not isOdd
    for i in range(2,n+1):
        file.write("\telif n=="+str(i)+":\n")
        file.write("\t\tprint("+str(isOdd)+")\n")
        isOdd=not isOdd

def run(n):
    import gened
    gened.isOdd(n)

def isOdd(n):
    generate(n)
    run(n)

def main():
    if len(sys.argv) < 2:
        n=input("Type in the input: ")
    else:
        n=sys.argv[1]
    n=int(n)
    isOdd(n)

if __name__ == "__main__":
    main()
