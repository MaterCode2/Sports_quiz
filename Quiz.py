'''This code gives users a quiz about New Zealand sports star, Lisa Carrington.
By Abigail Lavin - Created on 20/4/2026'''

# This code creates a user friendly message to introduce the quiz.
print("This is a quiz on New Zealand sports star, Lisa Carrignton")
print("The quiz will have a combination of multi-choice and short answer"
      " questions.")

# This code creates 10 questions and answers for the quiz. 
qanda = {"How many Oympic gold medals has Lisa Carrington won?\n" : 8,
         "What is the name of Lisa Carringon's dog?\n"
         "a) Max, b) Jack, c) Colin, d) Luna\n" : "a",
         "In what year did Lisa Carrington become a Dame?\n" : 2022,
         "True or False, Lisa Carrington won her first Olympic Gold medal in "
         "Rio De Janeiro\n" : "false",
         "True or False, Lisa Carrington has broken multiple kayaking records."
         "\n" : "true",
         "What date is Lisa Carrington's birthday?\na) 12th January, "
         "b) 23rd June, c) 26th November, d) 20th October\n" : "d",
         "How tall is Lisa Carrington? (In centimetres)\n" : 168,
         "What city was Lisa Carrington born in?\n a) Wellington, b) Tauranga,"
         " c) Auckland, d) Christchurch\n" : "b",
         "True or False, Lisa Carrington is NZ's second most decorated olympian"
         ".\n" : "false",
         "What University did Lisa Carrington attend while establishing her "
         "canoeing career?\na) Univeristy of Auckland, b) University of Waikato, "
         "c) Massey University, d) Victoria University\n" : "c"
         }

# This creates a score to keep track of how many questions the user 
# has gotten right.
score = 0

trueorfalse = ["true", "false"]
multichoice = ["a", "b", "c", "d"]

# This quizes the user and tests if their answer matches the correct
# answer.
for question, answer in qanda.items():
    user_answer = str(input(question))

    # This tests the answers for true or false questions.  
    if answer in trueorfalse :
        while user_answer.lower() not in trueorfalse :
            print("Your answer must be True or False")
            user_answer = str(input(question))
        if user_answer.lower() == answer :
            score += 1

    # This tests the answers for multi-choice questions. 
    elif answer in multichoice :
        while user_answer.lower() not in multichoice :
            print("Your answer must be one of the multichoice options.")
            user_answer = str(input(question))
        if user_answer.lower() == answer :
            score += 1

    # This tests the answers of number questions.
    elif type(answer) is int :
        work = "no"
        while work == "no":           
            try :
                
                # This tests the user's answer to make sure their 
                # answer's are not too large or small.
                user_answer = int(user_answer)
                if user_answer <= 0 :
                    print("Your number must be bigger than 0")
                    user_answer = str(input(question))
                elif answer <= 5 and user_answer >= 10 :
                    print("Your answer must be lower than 10")
                    user_answer = str(input(question))
                elif answer <= 10 and user_answer >= 20 :
                    print("Your answer must be lower than 20")
                    user_answer = str(input(question))
                elif answer <= 200 and user_answer > 400 :
                    print("Your answer must be lower than 400")
                    user_answer = str(input(question))
                elif answer <= 2500 and user_answer >= 2026 :
                    print("Your answer must be lower than 2026")
                    user_answer = str(input(question))
                elif answer >= 2000 and user_answer < 1991 :
                    print("Your answer must be bigger than 1990")
                    user_answer = str(input(question))
                elif int(user_answer) == answer :
                        print("correct")
                        score += 1
                        work = "yes"
                else:
                    work = "yes"
            except :
                if type(user_answer) == float :
                    print("Your answer must not include decimals.")
                else:
                    print("Your answer must be a number")
                user_answer = str(input(question))




print("You have finished the quiz. Well Done!")
print(f"Your score is {score}/10")



if score > 8 :
    skill = "excellent"
elif score > 5 :
    skill = "great"
elif score > 3 :
    skill = "okay"
else :
    skill = "bad"
        
print(f"You did {skill}")