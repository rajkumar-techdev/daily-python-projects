import pyttsx3


def text_to_speech():
    engine=pyttsx3.init()

    text=input("Enter the text you convert to speech:  ")

    #Speak the text

    engine.say(text)
    engine.runAndWait()


    #Save the audio file

    engine.save_to_file(text,'output.mp3')
    engine.runAndWait()

    print("Speech played and saved as output.mp3")


text_to_speech()