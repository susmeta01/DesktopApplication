import speech_recognition as sr
import pyttsx3
import pyjokes
import datetime

def speechtotext():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print ("Listening.....")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"Me:{text}")
        except:
            print("Try Again!")

def texttospeech(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.say(text)
    engine.runAndWait()

def jokes():
    jokes = pyjokes.get_joke(category="all")
    print(jokes)
    texttospeech(jokes)

def time():
    time = datetime.datetime.now().strftime("%I:%M %p")
    print(time)
    texttospeech(time)

## Main
print("Hello, I am your personal assistant")
option = True
while (option !=0):
    option = int(input("Options: \n 1. Speech to text\n 2. Text to Speech \n 3. Tell me a joke \n 4. What's the time? \n Press 0 to exit \n Please let me know which option you want to perform: "))
    if (option == 1):
        speechtotext()
    elif (option == 2):
        text = input("Enter the text to be converted to audio: ")
        texttospeech(text)
    elif (option == 3):
        jokes()
    elif (option == 4):
        time()
    elif (option == 0):
        exit()
    else:
        print("\n \n I am not able to understand. Please try again")
        continue

