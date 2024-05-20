from src.helper import extract_numbers_from_text,add,sub,mul,div,lcm,hcf,sqrt,sorry,end,fact,welcome,takeCommand,speak
 

operations0={'CLOSE':end,'END':end,'TERMINATE':end,'EXIT':end,'QUIT':end,'FINISH':end}
operations1={ 'ROOT':sqrt,'FACTORIAL':fact,'FACT':fact}
operations2={
    'PLUS':add,'ADD':add,'ADDITION':add,'SUM':add,'SOME':add,
    'MINUS':sub,'SUBTRACT':sub,'SUBTRACTION':sub,'DIFFERENCE':sub,
    'PRODUCT':mul,'MULTIPLY':mul,'MULTIPLICATION':mul,
    'MULTIPLIED':mul,
    'DIVIDE':div,'DIVISION':div,'LCM':lcm,'HCF':hcf
}


def main():
    #print("Welcome to the SMART CALCULATOR")
    welcome()
    
    while True:
        query = takeCommand()
        print()
        #text=input("Enter some text\n")
        for word in query.split(' '):
            if word.upper() in operations2.keys():
                try:
                    l=extract_numbers_from_text(query)
                    if len(l)>2:
                        speak('only the first two numbers are considred for the operation')
                        print('only the first two numbers are considred for the operation')
                    r=operations2[word.upper()](l[0],l[1])
                    speak(f'result is {r}')
                    print('result is',r)
                except:
                    speak("Something is wrong, please retry")
                    print("Something is wrong, please retry")
                finally:
                    break
            elif word.upper() in operations0.keys():
                operations0[word.upper()]()
                break
            elif word.upper() in operations1.keys():
                l=extract_numbers_from_text(query)
                if len(l)>1:
                    speak('only the first number is considred for the operation')
                    print('only the first number is considred for the operation')
                r=operations1[word.upper()](l[0])
                speak(f'result is {r}')
                print('result is',r)
                break
        else:
            sorry()
            
if __name__=='__main__':
    main()