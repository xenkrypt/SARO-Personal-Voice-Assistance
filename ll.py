import pyttsx3 #text to speech conversion
import speech_recognition as sr #speech to text conversion
import webbrowser #web pages
import wikipedia #wikipedia results
import pyscreenshot #screenshot
import os #access desktop apps
import datetime #for date and time
import ctypes #background picture
import pyjokes #jokes
import pyautogui #mouse movements, click on objects, send text, and even use hotkeys.
import random #random
import time #time
import subprocess
from ecapture import ecapture as ec #camera
import pygame #playing sound file


def say(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('rate', 160)
    engine.setProperty('voice',voices[1].id)
    engine.say(text)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("  listening...")
        pygame.mixer.init()
        pygame.mixer.music.load(r'C:\Users\abina\Documents\Saro Heart\saro open.mp3')
        pygame.mixer.music.play()
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("  recognizing...")
            pygame.mixer.init()
            pygame.mixer.music.load(r'C:\Users\abina\Documents\Saro Heart\saro close.mp3')
            pygame.mixer.music.play()
            text = r.recognize_google(audio, language='en-in')
            print(f"  user said : {text}\n")
        except Exception as e:
            print(e)
            print("  can not recognize your voice")
            return "none"
        return text



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        print("  GOOD MORNING !")
        say("GOOD MORNING !")

    elif hour >= 12 and hour < 18:
        print("  GOOD AFTERNOON !")
        say("GOOD AFTERNOON !")

    else:
        print("  GOOD EVENING !")
        say("GOOD EVENING !")




def get_time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    return Time


def get_date():
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)

    Date = day + "/" + month + "/" + year
    return Date

def ss():
    image = pyscreenshot.grab()
    image.show()
    image.save(r"C:\Users\abina\Documents\Saro Heart\saro ss\saro_img.jpg")


def my_age():
    birthday = datetime.datetime(2023, 8, 10)
    diff = datetime.datetime.now() - birthday
    print(diff.days)


def respond(text):
    
    if "good morning" in text or "good afternoon" in text or "good evening" in text:
        wishMe()

    # FOR OPENING WEBSITES


    elif "open WhatsApp" in text:
        print("  OPENING WHATSAPP")
        say("OPENING WHATSAPP..")
        webbrowser.open("https://web.whatsapp.com/")
        exit()


    elif "open YouTube" in text:
        print("  OPENING YOUTUBE..")
        say("OPENING YOUTUBE..")
        webbrowser.open("https://www.youtube.com/")
        exit()

    elif "open Google" in text:
        print("  OPENING GOOGLE..")
        say("OPENING GOOGLE..")
        webbrowser.open("https://www.google.co.in/")
        exit()

    elif "open Facebook" in text:
        print("  OPENING FACEBOOK..")
        say("OPENING FACEBOOK..")
        webbrowser.open("https://www.facebook.com/")
        exit()

    elif "open Instagram" in text or "open insta" in text:
        print("  OPENING INSTAGRAM..")
        say("OPENING instaAGRAM..")
        webbrowser.open("https://www.instagram.com/")
        exit()

    elif "open Twitter" in text:
        print("  OPENING TWITTER..")
        say("OPENING TWITTER..")
        webbrowser.open("https://twitter.com/i/flow/login")
        exit()

    elif "open g map" in text or "open map" in text:
        print("  OPENING GOOGLE MAP..")
        say("OPENING GOOGLE MAP..")
        webbrowser.open("https://www.google.com/maps/@21.125498,81.914063,5z")
        exit()

    elif "open hotstar" in text:
        print("  OPENING HOTSTAR..")
        say("OPENING HOTSTAR..")
        webbrowser.open("https://www.hotstar.com/in")
        exit()

    elif "open Netflix" in text:
        print("  OPENING NETFLIX..")
        say("OPENING NETFLIX..")
        webbrowser.open("https://www.netflix.com/in/")
        exit()


    elif "open Amazon" in text:
        print("  OPENING AMAZON..")
        say("OPENING AMAZON..")
        webbrowser.open("https://www.amazon.in/")
        exit()

    elif "open Prime" in text:
        print("  OPENING AMAZON PRIME..")
        say("OPENING AMAZON PRIME..")
        webbrowser.open(
            "https://www.primevideo.com/?ref_=dvm_pds_amz_in_as_s_gm_159&gclid=CjwKCAiAyfybBhBKEiwAgtB7fsXpkU8_sGO_12CsFNWaSTG2qIh-l907EO8M1z1BRWivx7GvRz0YABoCfToQAvD_BwE")
        exit()

    elif "open Flipkart" in text:
        print("  OPENING FLIPKART..")
        say("OPENING FLIPKART..")
        webbrowser.open("https://www.flipkart.com/")
        exit()

    elif "open zee5" in text:
        print("  OPENING ZEE5..")
        say("OPENING Z5..")
        webbrowser.open(
            "https://www.zee5.com/?utm_source=GoogleSearch&utm_medium=Mark_CPA&utm_campaign=Search_SVOD_ZEE5-Brand-ZEE5-Only-Ex-Performance&utm_term=zee5&utm_content=Brand-ZEE5-Only-Ex&gclid=CjwKCAiAyfybBhBKEiwAgtB7fgwEs43NpKI0GBhhr7Az7CX8cNESfEinn2rL2TMijj1ZPSlFBj2zcBoCQgUQAvD_BwE&gclsrc=aw.ds")
        exit()

    elif "open Mega" in text:
        print("  OPENING MEGA..")
        say("OPENING MEGA..")
        webbrowser.open("https://mega.nz/fm/iV4HkL4C")
        exit()

    elif "open poster" in text:
        print("  OPENING MAIL..")
        say("OPENING MAIL..")
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
        exit()

    elif "open my note" in text:
        print("  OPENING YOUR NOTE..")
        say("OPENING YOUR NOTE..")
        os.startfile(r"C:\Users\abina\Documents\Saro Heart\saro notes.txt")
        exit()



    # OPENING AND CLOSING

    elif "open Notepad" in text:
        print("  OPENING NOTEPAD..")
        say("OPENING NOTEPAD..")
        os.startfile('notepad.exe')

    elif "close notepad" in text:
        print("  CLOSING NOTEPAD..")
        say("CLOSING NOTEPAD..")
        os.system("TASKKILL /F /IM notepad.exe")

    # TAKING NOTE

    elif "take a note" in text:
        print("  TAKING DOWN")
        say("TAKING DOWN")
        file = open(r"C:\Users\abina\Documents\Saro Heart\saro notes.txt", 'w')
        note = takecommand()
        file.write(note)
        file.close()
        print("  NOTE SAVED")
        say("NOTE SAVED")


    # LOGING IN MEGA

    elif "login Mega" in text:
        print("  LOGING IN MEGA..")
        say("LOGING IN MEGA..")
        webbrowser.open("https://mega.nz/login")
        time.sleep(10)
        pyautogui.write("signinsignupacc@gmail.com")
        pyautogui.press("enter")
        pyautogui.write("signinsignupacc@0005")
        pyautogui.press("enter")
        exit()

    # FOR TIME

    elif "what is the time" in text or "what's the time" in text or "time" in text:
        print("  The Time is : ", get_time())
        say(get_time())

    # FOR DATE

    elif "what is today's date" in text or "date" in text:
        print("  The Date is : ", get_date())
        say(get_date())

    # TAKING SCREENSHOT

    elif "take screenshot" in text or "screenshot" in text or "capture" in text:
        ss()


    # VOLUME

    elif "volume up" in text or "increase the volume" in text:
        pyautogui.press("volumeup")
        pyautogui.press("volumeup")


    elif "volume down" in text or "decrease the volume" in text:
        pyautogui.press("volumedown")
        pyautogui.press("volumedown")

    elif "volume mute" in text or "mute the volume" in text:
        pyautogui.press("volumemute")

    # CAMERA

    elif "camera" in text or "take a photo" in text :
        ec.capture(0, "saro camera", "TS.jpg")

    # SEARCHING IN WIKIPEDIA

    elif 'search in Wikipedia for' in text:
        query = text.replace("search in Wikipedia for", "")
        say('Searching in Wikipedia for'), say(query)
        result = wikipedia.summary(query, sentences=2)
        print("  ACCORDING TO WIKIPEDIA")
        say("According to Wikipedia")
        print("")
        print(result)
        say(result)



    # SEARCHING IN YOUTUBE

    elif "search in youtube for" in text.lower():
        ind = text.lower().split().index("for")
        search = text.split()[ind + 1:]
        webbrowser.open(
            "https://www.youtube.com/results?search_query=" +
            "+".join(search)
        )
        say("results in youtube for"), say(search)
        exit()

    # SEARCHING IN GOOGLE

    elif "search in google" in text.lower():
        ind = text.lower().split().index("for")
        search = text.split()[ind + 1:]
        webbrowser.open(
            "https://www.google.com/search?q=" + "+".join(search)
        )
        say("re,sullts in google for"), say(search)
        exit()



    # CHANGING BACKGROUND

    elif "change background" in text or "change wallpaper" in text:
        img = r'C:\Users\abina\Documents\Saro Heart\saro setting background'
        list_img = os.listdir(img)
        imgChoice = random.choice(list_img)
        randomImg = os.path.join(img, imgChoice)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, randomImg, 0)
        print("  BACKGROUND CHANGED SUCCESSFULLY")
        say("BACKGROUND CHANGED SUCCESSFULLY")

    # JOKES

    elif "say some joke" in text or "say some jokes" in text or "joke" in text or "jokes" in text:
        joke = pyjokes.get_joke()
        print(joke, end=" ")
        print("\U0001F606")
        say(joke)

    # OPENING LOCATIONS

    elif "where is" in text:
        ind = text.lower().split().index("is")
        location = text.split()[ind + 1:]
        url = "https://www.google.com/maps/place/" + "".join(location)
        say("THIS IS WHERE"), say(location), say("is")
        webbrowser.open(url)
        exit()



    # SLEEP

    elif "wait" in text or "sleep" in text:
        print("  FOR HOW MANY SECONDS DO YOU WANT ME TO SLEEP")
        say("FOR HOW MANY SECONDS DO YOU WANT ME TO SLEEP")
        a = int(takecommand())
        time.sleep(a)
        say(a), say("SECONDS COMPLETED NOW YOU CAN ASK ME ANYTHING")

    # EXIT

    elif "exit" in text or "quit" in text or "stop listening" in text or "break" in text:
        exit()

    # SHUTDOWN

    elif "power of" in text or "power off system" in text or "power off the system" in text or "shutdown" in text:
        say("SHUTTING DOWN")
        os.system("shutdown /s /t 1")


    # TO PLAY SONG

    elif "play" in text or "song" in text or "play a song" in text:
        print("  WHAT SONG I SHOULD PLAY")
        say("WHAT SONG I SHOULD PLAY")
        s = takecommand()
        os.startfile(r"C:\Users\abina\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Spotify.lnk")
        time.sleep(7)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(2)
        pyautogui.write(s, interval=0.1)
        time.sleep(3)
        pyautogui.press("enter")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
        exit()
    
    elif "send a mail" in text or "email" in text or "send a email" in text or "mail" in text:
        print("  TO WHOM I SEND")
        say("TO WHOM I SEND")
        s = takecommand().replace(" ", "")
        webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox?compose=new")
        time.sleep(10)
        pyautogui.write(s)
        time.sleep(2)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.write("SARO VOICE ASSISTANT")
        pyautogui.press("tab")
        print("  WHAT SHOULD I SEND")
        say("WHAT SHOULD I SEND")
        t = takecommand()
        pyautogui.write(t)
        time.sleep(2)
        pyautogui.press("tab")
        pyautogui.press("enter")
        exit()
    else:
        model_name="llama3.2"
        ollama_command = f"ollama run {model_name} !start {text}"
        result = subprocess.run(ollama_command, capture_output=True, text=True, shell=True)
        print(result.stdout.strip())
        say(result.stdout.strip())
while True:
    text=takecommand()
    respond(text)
