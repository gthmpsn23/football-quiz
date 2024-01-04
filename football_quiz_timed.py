import re

import time

# Email validator, validates the email based on the format of the string.

# def email_validator(email):
#     pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#     if re.match(pattern, email, re.IGNORECASE):
#         print("Valid Email")
#     else:
#         print("Invalid Email")


# Forces user to create a username with more than six characters

# while True:
#     print("Create your username. Your username must be more than six characters.")
#     user_name = input("Enter a username: ")

#     if len(user_name) > 6:
#         print(f"Hey {user_name}")
#         break
#     else:
#         print("username is too short!")


# calls email validator

# email_address = input("Enter your email address: ").strip()
# email_validator(email_address)

# quiz function based on time. 

def quiz(questions, options, correct_letter):
    print(question)
    for option in options:
        print(option)

# max score for each correctly answered question based on time.

    max_score = 20
    time_penalty = 1

# takes start time

    start_time = time.time()

    answer = input("\nEnter your answer A,B,C or D: ").lower()

# takes end time

    end_time = time.time()

# calculates how long it has taken them to answer

    time_taken = end_time - start_time

    if answer == correct_letter.lower():
        print("Correct")
        raw_score = max(max_score - (time_penalty * time_taken), 0)
        int_score = int(raw_score)
        score = max(int_score, 0)
        return score
    else: 
        print("Wrong!")
        return 0
        


print("\nWelcome to the football quiz")

# quiz questions 

questions = [ 
("\nWho has scored the most goals in premier league history?", [ "A: Wayne Rooney",
"B: Harry Kane",
"C: Alan Shearer",
"D: Thierry Henry"], "C"),

("\nWho has won the Champions League the most times?", ["A: Barcelona", "B: A.C Milan", "C: Manchester United", "D: Real Madrid"], "D"),

("\nWho has won the World Cup the most times?", ["A: Germany", "B: France", "C: Argentina", "D: Brazil"],"D"),

("\nHow many times have Brazil won the World Cup?", ["A: 1", "B: 3", "C: 5", "D: 12"],"C"),

("\nWho has won the Serie A the most times?", ["A: A.C Milan", "B: Inter Milan", "C: Juventus", "D: Roma"],"C"),

]

score = 0

for question, options, correct_letter in questions:
    score += quiz(questions, options, correct_letter)

print(score)

if score > 80:
    print(f"Your score is {score} - Great Work!")
elif score >= 60: 
    print(f"Your score is {score} - Good try!")
else:
    print(f"Your score is {score} - Poor finishing!")