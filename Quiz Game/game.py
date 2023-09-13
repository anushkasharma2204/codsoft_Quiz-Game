import tkinter as tk
from tkinter import StringVar

root = tk.Tk()
root.title("Game Quiz")
root.geometry('500x550')

questions = [ "Who developed Python Programming Language=?","Which of the following is the correct extension of the Python file=?","Is Python a Case-Sensitive Language=?","What is the maximum length of a Python identifier=?","Which types of  loops are not supported in Python=?",
             "Which of the following is a Python tuple=?","Which of the following is a Python List=?","Which of the following is a Python Set=?","Which of the following is a Python Dictionary=?","Which are Mutable in python=?","Comments in python Begin with=?",
             "How to print Hello World in python=?","str = [(1, 1), (2, 2), (3, 3)] ..What type of data is in this expression=?"," Which of the following arithmetic operators cannot be used with strings in python=?","Which of the following blocks allows you to test the code blocks for errors=?"]
options = [['Wick van Rossum','Rasmus Lerdorf', 'Guido van Rossum', 'Niene Stom','Guido van Rossum'], ['.python', '.pl','.py' ,'.p','.py'], ['Yes','No','None','Both','yes'],['30','60','108','Not Fixed','Not Fixed'],['For','While','Do-While','All of above','Do-While'],
           ['{1, 2, 3}','{}','[1, 2, 3]','(1, 2, 3)','(1, 2, 3)'],['[1,2,3]','(1,2,3)','{1,2,3}','None of them','[1,2,3]'],['[1,2,3]','(1,2,3)','{1,2,3}','All of them','{1,2,3}'],['{1:Hellow,2:Hello}','{1,2,3}','(1,2,3)','[2,3,4]','{1:Hellow,2:Hello}'],['List','Tupple','Both','None','List'],
           ['/','*','#','!','#'],['print("Hello World")','print Hello World','print(Hello World)','print("Hello World":)','print("Hello World")'],['String type','Array list','List of tupple','Str list','List of tupple'],['+','-','*','All','-'],['except block','try block','finally block','None of above','try block']]
          


frame = tk.Frame(root, padx=10, pady=10,bg='#fff')
question_label = tk.Label(frame,height=5, width=28,bg='grey',fg="#fff", 
                          font=('Verdana', 20),wraplength=500)


v1 = StringVar(frame)
v2 = StringVar(frame)
v3 = StringVar(frame)
v4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="#fff", variable=v1, font=('Verdana', 20),
                         command = lambda : checkAnswer(option1))
option2 = tk.Radiobutton(frame, bg="#fff", variable=v2, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option2))
option3 = tk.Radiobutton(frame, bg="#fff", variable=v3, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option3))
option4 = tk.Radiobutton(frame, bg="#fff", variable=v4, font=('Verdana', 20), 
                         command = lambda : checkAnswer(option4))

button_next = tk.Button(frame, text='Next',bg='Orange', font=('Verdana', 20), 
                        command = lambda : displayNextQuestion())

frame.pack(fill="both", expand="true")
question_label.grid(row=0, column=0)

option1.grid(sticky= 'W', row=1, column=0)
option2.grid(sticky= 'W', row=2, column=0)
option3.grid(sticky= 'W', row=3, column=0)
option4.grid(sticky= 'W', row=4, column=0)

button_next.grid(row=6, column=0)


index = 0
correct = 0

# create a function to disable radiobuttons
def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state


# create a function to check the selected answer
def checkAnswer(radio):
    global correct, index
    
    # the 4th item is the correct answer
    # we will check the user selected answer with the 4th item
    if radio['text'] == options[index][4]:
        correct +=1

    index +=1
    disableButtons('disable')


# create a function to display the next question
def displayNextQuestion():
    global index, correct

    if button_next['text'] == 'Restart The Quiz':
        correct = 0
        index = 0
        question_label['bg'] = 'grey'
        button_next['text'] = 'Next'

    if index == len(options):
       question_label['text'] = str(correct) + " / " + str(len(options))
       button_next['text'] = 'Restart The Quiz'
       if correct >= len(options)/2:
           question_label['bg'] = 'green'
       else:
            question_label['bg'] = 'red'





    else:
        question_label['text'] = questions[index]
        
        disableButtons('normal')
        opts = options[index]
        option1['text'] = opts[0]
        option2['text'] = opts[1]
        option3['text'] = opts[2]
        option4['text'] = opts[3]
        v1.set(opts[0])
        v2.set(opts[1])
        v3.set(opts[2])
        v4.set(opts[3])

        if index == len(options) - 1:
            button_next['text'] = 'Check the Results'





displayNextQuestion()

root.mainloop()

                                       



