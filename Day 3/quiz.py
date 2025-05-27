#Quiz App

#step 1:Define a list of quiz Questions

def quiz_app():
    questions=[
           {
            "question":"What is the capital of India?",
            "options":["A.Delhi","B.Mumbai","C.Chennai","D.Kolkata"],
            "answer":"A"#Correct Option
          },
         {
            "question":"Which language is used for Web App?",
            "options":["A.Python","B.Java","C.Javascript","D.All of the above"],
            "answer":"D"

        },
        {
            "question":"What is the output of 2+2*2?.",
            "options":["A.6","B.8","C.4","D.10"],
            "answer":"A"

        }
    ]

    global score
    score=0#variable to keep track on correct answers

#step 2:Loop through each question

    for q in questions:

        print("\n"+q["question"])
        for option in q["options"]:
            print(option)
#step 3:Get user answers and make sure it uppercase
        user_answer=input("Enter your answer(A/B/C/D)").strip().upper()

        if user_answer==q["answer"]:
             print("Correct!")
             score+=1#Increase score by 1
        else:
             print(f"Wrong! answer the correct answer is{q['answer']} ")
    print(f"\n Your Total score is {score} out of {len(questions)}")

quiz_app()



