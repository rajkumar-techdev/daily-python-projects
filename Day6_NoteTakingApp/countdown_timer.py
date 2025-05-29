import time
import winsound

def countdown(seconds):
    while seconds>0:
        mins,secs=divmod(seconds,60)
        timer=f"{mins:02d}:{secs:02d}"
        print(timer)
        time.sleep(1)
        seconds-=1
    print("Times Up")
    #play sound
    frequency=1000
    duration=2000
    winsound.Beep(frequency,duration)

def main():
    try:
        total_seconds=int(input("Enter time in seconds"))
        countdown(total_seconds)
    except ValueError:
        print("Please enter a valid number")

main()