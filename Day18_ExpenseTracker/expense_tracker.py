import csv
import os

from datetime import datetime

FILE_NAME="expenses.csv"


def add_expenses():
    amount=input("Enter amount:  ")
    category=input("Enter category eg(food,travel):  ")
    date=input("Enter date (YYYY-MM-DD) or leave blank for today date:  ")

    if not date:
        date=datetime.today().strftime('%Y-%m-%d')
    with open(FILE_NAME,mode='a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([amount,category,date])
    print("Expense added successfully")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recoded yet!")
        return
    with open(FILE_NAME,mode='r')as file:
        reader=csv.reader(file)
        total=0
        print("\n Your Expenses")

        for row in reader:
            print(f"Amount:${row[0]}, Category: {row[1]}, Date: {row[2]}")
            total+=float(row[0])
        print(f"\n Total spent: {total}")

def main():
    while True:
        print("\n ---Expense Tracker ---")
        print("1.Add Expenses")
        print("2.View Expenses")
        print("3.Exit")

        choice=input("choose an option(1-3): ")

        if choice =='1':
            add_expenses()
        elif choice=='2':
            view_expenses()
        elif choice=='3':
            print("Good Bye")
            break
        else:
            print("Invalid choice,Try again!")

main()