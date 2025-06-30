import time
import random

sentences=[
    "Practice makes a man perfect ",
    "Python is a powerful programming language",
    "Consistency is key to success",
    "Always keep leaning something new",
    "Errors are proof that you are trying"
]

def typing_test():
    sentence=random.choice(sentences)
    print("\n Type this sentence as fast as you can:")
    print("-->",sentence)
    input("Press Enter when you ready....")

    start=time.time()
    typed=input("\nStart typing")
    end=time.time()

    time_taken=round(end-start,2)
    words=len(sentence.split())
    wpm=round((words/time_taken)*60,2)

    errors=0


    for i in range(min(len(sentence),len(typed))):
        if sentence!=typed[i]:
            errors+=1
        errors+=abs(len(sentence)-len(typed))

    print(f"\n Time Taken  {time_taken} in seconds")
    print("Your typing speed ",wpm," WPM")
    print(f"Errors:  {errors}")

typing_test()