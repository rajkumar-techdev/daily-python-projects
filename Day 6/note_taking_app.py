#Note-Taking App

#Add Notes
def add_note():
    note=input("Write your note")
    with open("notes.txt",'a') as file:
        file.write(note+"\n")
    print("Note saved successfully")

#view Notes

def view_notes():
    print("\n Your saved notes")

    try:
        with open("notes.txt",'r')  as file:
            notes=file.readlines()
            for i,note in enumerate(notes,start=1):
                print(f"{i}.{note.strip()}")
    except FileNotFoundError:
        print("No notes found,Please add a note first")

def main():
    while True:
        print("\n===Note-Taking App====")
        print("1.Add note")
        print("2.View  All Notes")
        print("3.Exit")

        choice=input("Enter your choice(1/2/3): ")

        if choice=='1':
            add_note()
        elif choice=='2':
            view_notes()
        elif choice=='3':
            print("Good Bye")
            break
        else:
            print("Invalid Choice,please enter 1,2, or 3")

main()


