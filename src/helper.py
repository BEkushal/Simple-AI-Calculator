import pyttsx3
import speech_recognition as sr

# Taking voice from my system
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)

engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)
#speak function
def speak(text):
    """This function takes text and returns voice

    Args:
        text (_type_): string
    """
    engine.say(text)
    engine.runAndWait()

# speech recognition function
def takeCommand():
    """this function will recognize voice & return text
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            #print(f"User said: {query}\n")
            print(query)

        except Exception as e:
            print("Say that again please...")
            return "None"
        return query
    

def welcome():
    speak('Hello there! I am SSM simple smart calculator what are the calculations you need me to perform ?')


def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        for e in t.split(','):
            try:
                l.append(float(e))
            except Exception:
                pass
    return l

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
        H-=1
        
def fact(a):
    f = 1
    while a:
        f*= a
        a-=1
    return f
        
def end():
    speak("Thank You for using Smart Calculator")
    print("Thank You for using Smart Calculator")
    #input("Press enter key to exit")
    exit()

def sorry():
    speak("This instruction is beyond my ability")
    print("This instruction is beyond my ability")
