import speech_recognition as sr 
import pyttsx3
import wikipedia

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speaking speed

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Please repeat.")
            return None
        except sr.RequestError:
            speak("Could not request results, please check your internet connection.")
            return None

def process_command(command):
    if 'wikipedia' in command:
        speak("Searching Wikipedia...")
        topic = command.replace("wikipedia", "").strip()
        try:
            result = wikipedia.summary(topic, sentences=2)
            speak(result)
        except Exception:
            speak("Sorry, I couldn't find anything on Wikipedia.")
    elif 'hello' in command:
        speak("Hello! How can I assist you today?")
    elif 'exit' in command:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that. Can you try again?")

if __name__ == "__main__":
    speak("Welcome! I am your custom voice assistant.")
    while True:
        command = listen()
        if command:
            process_command(command)
