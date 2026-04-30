'''This code gives users a quiz about New Zealand sports star, Lisa Carrington.
By Abigail Lavin - Created on 20/4/2026'''

# This code creates a user friendly message to introduce the quiz.
print("This is a quiz on New Zealand sports star, Lisa Carrignton")
print("The quiz will have a combination of multi-choice and short answer questions.")

# This code creates 10 questions and answers for the quiz. 
qanda = {"How many Oympic gold medals has Lisa Carrington won?\n" : 8,
         "What is the name of Lisa Carringon's dog?\n"
         "a) Max, b) Jack, c) Colin, d) Luna\n" : "a",
         "In what year did Lisa Carrington become a Dame?\n" : 2022,
         "In what city's Olympics did Lisa Carrington win her first gold medal\n"
         : "london",
         "True or False, Lisa Carrington has broken multiple kayaking records.\n" : "true",
         "What date is Lisa Carrington's birthday?\n"
         "a) 12th January, b) 23rd June, c) 26th November, d) 20th October\n" : "d",
         "How tall is Lisa Carrington? (In metres to 1dp)\n" : 1.7,
         "What city was Lisa Carrington born in?\n" : "tauranga",
         "True or False, Lisa Carrington is NZ's second most decorated olympian.\n" 
         : "false",
         "What University did Lisa Carrington attend while establishing her canoeing career?"
         "/na) Univeristy of Auckland, b) University of Waikato, c) Massey University, "
         "d) Victoria University\n" : "c"
         }

# This creates a score to keep track of how many questions the user has gotten
# right
score = 0

# This quizes the user and tests if their answer matches the correct answer
for question, answer in qanda.items():
    user_answer = input(question)
    while user_answer.type(str) == False
        print("Your answer must only include letters or numbers")
        user_answer = input(question)
    try:
        if int(answer) == int(user_answer):
            score += 1
    except:
        if answer == user_answer.lower() :
            score += 1 

print("You have finished the quiz. Well Done!")
print(f"Your score is {score}/10")

skill = ""

if score > 8 :
    skill = "excellent"
elif score > 5 :
    skill = "great"
elif score > 3 :
    skill = "okay"
else :
    skill = "bad"
        
print(f"You did {skill}")