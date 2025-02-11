import pyautogui
import speech_recognition as sr
import time
import playsound

def voice_control():
    # time.sleep(5)  # Delay before execution
    pyautogui.moveTo(960, 540)  # Move cursor to center of screen
    
    def move_cursor(direction, move_type):
        distance = 150 if move_type == 'small' else 400
        x, y = pyautogui.position()
        if direction == 'u':
            pyautogui.moveTo(x, y - distance)
        elif direction == 'd':
            pyautogui.moveTo(x, y + distance)
        elif direction == 'l':
            pyautogui.moveTo(x - distance, y)
        elif direction == 'r':
            pyautogui.moveTo(x + distance, y)
    
    def scroll_page(scroll_type, direction):
        scroll_amount = 100 if scroll_type == 'scroll1' else 370
        pyautogui.scroll(scroll_amount if direction == 'u' else -scroll_amount)
    
    def click_at_cursor():
        pyautogui.click()
    
    def close_tab():
        pyautogui.hotkey("ctrl","w")

    def go_back():
        pyautogui.hotkey("alt", "left")
    
    def go_front():
        pyautogui.hotkey("alt", "right")
    
    def recognize_speech():
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            playsound.playsound("C:\\Users\\Tharunkrishna\\Desktop\\vitnex25\\saroopen.mp3")
            print("Listening for commands...")
            recognizer.adjust_for_ambient_noise(source)
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                return command
            except sr.UnknownValueError:
                print("Sorry, I didn't understand.")
                playsound.playsound("C:\\Users\\Tharunkrishna\\Desktop\\vitnex25\\saroclose.mp3")
                return None
            except sr.RequestError:
                print("Error with speech recognition service.")
                playsound.playsound("C:\\Users\\Tharunkrishna\\Desktop\\vitnex25\\saroclose.mp3")
                return None
    
    while True:
        command = recognize_speech()
        if command:
            if "move" in command:
                move_type = 'small' if "small" in command else 'big'
                if "up" in command:
                    move_cursor('u', move_type)
                elif "down" in command:
                    move_cursor('d', move_type)
                elif "left" in command:
                    move_cursor('l', move_type)
                elif "right" in command:
                    move_cursor('r', move_type)
            elif "scroll" in command or "press" in command:
                scroll_type = 'scroll1' if "small" in command else 'scroll2'
                if "up" in command:
                    scroll_page(scroll_type, 'u')
                elif "down" in command:
                    scroll_page(scroll_type, 'd')
            elif "click" in command:
                click_at_cursor()
            elif "go back" in command:
                go_back()
            elif "go front" in command:
                go_front()
            elif "close tab" in command:
                close_tab()
            elif "exit" in command or "stop" in command or "terminate" in command:
                print("Program has stopped.")
                playsound.playsound("C:\\Users\\Tharunkrishna\\Desktop\\vitnex25\\saroclose.mp3")
                break

if __name__ == "__main__":
    voice_control()
