import pyttsx3
import speech_recognition as sr
import subprocess
import time

# Voice interpreting Function
def voice_interpretion():
    controller=sr.Recognizer()
    # sr.Microphone()
    try:
        with sr.Microphone() as source:
            print("Listening ...")
            audio=controller.listen(source,timeout=20,phrase_time_limit=3)
        text=controller.recognize_google(audio,language="en=US")
        print(text)
        if text is None:
           print("Nothing's here gng !")
        return text  #returning the text to use it in logic function

    except sr.WaitTimeoutError:
        print("Speak Louder !")
    # except UnboundLocalError:
    #     print("Nothings here gang !")
    except sr.UnknownValueError:
        print("Transcribing Failed !")

# voice_interpretion()


def process_initiation():
    text_variable=voice_interpretion() #using this variable to use mic function
    if "open firefox" in text_variable.lower():
        subprocess.Popen("firefox")

    elif "open brave" in text_variable.lower():
        subprocess.Popen("brave")
    elif "open cheese" in text_variable.lower():
        subprocess.Popen("cheese")
    elif "open pycharm" in text_variable.lower():
        subprocess.Popen("pycharm")
    elif "open code" in text_variable.lower():
        subprocess.Popen("code")

process_initiation()




#
#
#
# engine=pyttsx3.init()
# user_inputs=input("Enter words to speak: ")
# engine.say(user_inputs)
# engine.runAndWait()