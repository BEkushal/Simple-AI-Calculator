from src.helper import extract_numbers_from_text,add,sub,mul,div,lcm,hcf,sqrt,sorry,end

def welcome():
    print('Hello there! I am SSM simple smart calculator what are the calculations you need me to perform ?')
    

operations0={'CLOSE':end,'END':end,'TERMINATE':end,'EXIT':end,'QUIT':end,'FINISH':end}
operations1={ 'ROOT':sqrt}
operations2={
    'PLUS':add,'ADD':add,'ADDITION':add,'SUM':add,
    'MINUS':sub,'SUBTRACT':sub,'SUBTRACTION':sub,'DIFFERENCE':sub,
    'PRODUCT':mul,'MULTIPLY':mul,'MULTIPLICATION':mul,
    'MULTIPLIED':mul,
    'DIVIDE':div,'DIVISION':div,'LCM':lcm,'HCF':hcf
}


def main():
    print("Welcome to the SMART CALCULATOR")
    while True:
        print()
        text=input("Enter some text\n")
        for word in text.split(' '):
            if word.upper() in operations2.keys():
                try:
                    l=extract_numbers_from_text(text)
                    r=operations2[word.upper()](l[0],l[1])
                    print('result is',r)
                except:
                    print("Something is wrong, please retry")
                finally:
                    break
            elif word.upper() in operations0.keys():
                operations0[word.upper()]()
                break
            elif word.upper() in operations1.keys():
                l=extract_numbers_from_text(text)
                r=operations1[word.upper()](l[0])
                print('result is',r)
                break
        else:
            sorry()
            
if __name__=='__main__':
    main()