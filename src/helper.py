def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        for e in t.split(','):
            try:
                l.append(float(e))
            except Exception as e:
                pass

def recieveinput():
    pass

def speak():
    pass

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def sqrt(a):
    return a**0.5
def lcm(a,b):
    l= a if a>b else b
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l
        l+=1
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        
def end():
    print("Thank You for using Smart Calculator")
    input("Press enter key to exit")
    exit()
def sorry():
    print("This instruction is beyond my ability")
