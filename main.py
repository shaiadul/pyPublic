import pyttsx3

print(":::: Welcome to pyBot 0.1 (type 's' to stop) ::::")


def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


if __name__ == '__main__':
    while True:
        try:
            text = input("Massage : ")
            if text == "s":
                speak_text("Thanks for using our bot !")
                break
            speak_text(text)
        except Exception as e:
            print(f"Error: {e}")

