import speech_recognition as sr
from utils import take_screenshot  


recognizer = sr.Recognizer()

def listen_for_command():
    """Listen for a specific voice command and take a screenshot when detected."""
    with sr.Microphone() as source:
    
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            command = recognizer.recognize_google(audio).lower()
            
            
            if "screenshot" in command:
                print("Command recognized: Taking screenshot")
                take_screenshot()  # Call the screenshot function
            else:
                print("Command not recognized. Please say 'take screenshot'.")
                
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")

if __name__ == "__main__":
    while True:
        listen_for_command()
