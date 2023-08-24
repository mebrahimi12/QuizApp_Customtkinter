import customtkinter
from tkinter import messagebox

questions = [
    {
        "question": "Which of the following is a web browser?",
        "options": ["chrome", "Python", "MySQL", "Java"], 
        "correct_answer": "chrome"
    },
    {
        "question": "Which of the following is a programming language?",
        "options": ["Python", "Linux", "Windows", "chrome"],
        "correct_answer": "Python" 
    },
    {
        "question": "Which of the following is not an operating system?",
        "options": ["Windows", "Linux", "Android", "Vscode"],
        "correct_answer": "Vscode"
    },
    {
        "question": "Which of the following is a Python Framework?",
        "options": ["node", "Spark", "Bootstrap", "Django"],
        "correct_answer": "Django" 
    },
]

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("480x350")
app.title("Quiz App")



question_label = customtkinter.CTkLabel(app, text="", 
                                        font=customtkinter.CTkFont(size=18, weight="bold"))
question_label.pack(pady=12)

option_buttons = []
for i in range(4):
    btn = customtkinter.CTkButton(app, fg_color=("gray75", "gray30"))
    btn.pack(pady=12, padx=20)
    option_buttons.append(btn)
     

current_question = 0
score = 0

def next_question():
    global current_question
    if current_question < len(questions):
        ask_question(questions[current_question])
        current_question += 1
    else:
        show_final_score()
        
def ask_question(question):
    question_label.configure(text=question["question"])
    
    for i in range(4):
        option = question["options"][i]
        option_buttons[i].configure(text=option, command=lambda x=option: check_answer(x))
        
def check_answer(answer):
    global score
    
    if answer == questions[current_question-1]["correct_answer"]:
        score += 1
        result_label.configure(text="Correct!") 
    else:
        result_label.configure(text=f"Incorrect. The answer is {questions[current_question-1]['correct_answer']}")
    
    next_question()
    
def show_final_score():
    final_text = f"Your final score is {score} / {len(questions)}"
    result_label.configure(text=final_text)
    app.destroy() 
    messagebox.showinfo("Quiz Completed", final_text)

result_label = customtkinter.CTkLabel(app, text="")
result_label.pack(pady=12)

next_question()
app.mainloop()