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


for question, answer in qanda.items():
    user_answer = input(question)
    if answer is int :
        if int(answer) == int(user_answer):
        