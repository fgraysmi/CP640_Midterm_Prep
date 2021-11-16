import pandas as pd


questions_df = pd.read_csv('MultipleChoiceQuestions.csv')
questions_df = questions_df.sample(frac=1).reset_index(drop=True)

questions_answered = 0
correct_answers = 0
incorrect_answers = []

for question in questions_df.iterrows():
    print(question[1]['Question'])
    print("A: " + question[1]['A'])
    print("B: " + question[1]['B'])
    print("C: " + question[1]['C'])
    print("D: " + question[1]['D'])
    print("E: " + question[1]['E'])
    user_answer = input("Answer, or enter 'X' to quit: ")
    user_answer = user_answer.upper()
    if user_answer == "X":
        break
    elif user_answer == question[1]['Answer']:
        print("Correct!")
        questions_answered+=1
        correct_answers+=1
    elif user_answer in (question[1]['Answer']):
        print("Partially correct!You answered: "+user_answer)
        print("The correct answer is: "+(question[1]['Answer']))
        questions_answered+=1
        correct_answers+=0.5
        incorrect_answers.append(question[1]['Question'])
    else:
        print("Incorrect. You answered: "+user_answer)
        print("The correct answer is: "+(question[1]['Answer']))
        questions_answered+=1
        incorrect_answers.append(question[1]['Question'])

score = round(correct_answers/questions_answered*100,3)
print("Your score is: "+str(score)+"%")


textfile = open("incorrect answers.txt", "w")
for element in incorrect_answers:
    textfile.write(element + "\n")
textfile.close()

