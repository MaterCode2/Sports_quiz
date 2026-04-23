'''This code gives users a quiz about New Zealand sports star, Lisa Carrington.
By Abigail Lavin - Created on 20/4/2026'''

#Creates a user friendly statement to introduce the quiz
print("This is a quiz on New Zealand sports star, Lisa Carrignton")
print("The quiz will have a combination of multi-choice and short answer questions.")

#Creates a dictionary of 10 questions and answers
qanda = {"How many Oympic gold medals has Lisa Carrington won?\n" : 8,
         "What is the name of Lisa Carringon's dog?\na) Max, b) Jack, c) Colin, d) Luna\n" : "a",
         "In what year did Lisa Carrington become a Dame?\n" : 2022,
         "In what city's Olympics did Lisa Carrington win her first gold medal\n" : "london",
         "True or False, Lisa Carrington has broken multiple kayaking records.\n" : "true",
         "What date is Lisa Carrington's birthday?\na) 12th January, b) 23rd June, c) 26th November, d) 20th October\n" : "d",
         "How tall is Lisa Carrington? (In metres to 1dp)\n" : 1.7,
         "What city was Lisa Carrington born in?\n" : "tauranga",
         "True or False, Lisa Carrington is NZ's second most decorated olympian.\n" : "false",
         "What University did Lisa Carrington attend while establishing her canoeing career?/na) Univeristy of Auckland, b) University of Waikato, c) Massey University, d) Victoria University\n" : "c"
         }

print(qanda.keys())
for question, answer in qanda.items():
    print(question)
    if answer.isnumeric() :
        print("Yes")