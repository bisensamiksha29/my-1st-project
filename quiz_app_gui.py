import tkinter as tk

questions = [
    {
        "question": "Which of these is used to define a function in Python?",
        "options": ["function", "def", "func", "define"],
        "answer": "def"
    },
    {
        "question": "What data type is the result of: 5 / 2 in Python 3?",
        "options": ["int", "float", "str", "bool"],
        "answer": "float"
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["list.add()", "list.insert()", "list.append()", "list.push()"],
        "answer": "list.append()"
    },
    {
        "question": "What will type([]) return?",
        "options": ["<class 'list'>", "<class 'dict'>", "<class 'tuple'>", "<class 'set'>"],
        "answer": "<class 'list'>"
    },
    {
        "question": "Which keyword is used to handle exceptions in Python?",
        "options": ["catch", "except", "error", "handle"],
        "answer": "except"
    },
    {
        "question": "What does the len() function do?",
        "options": ["Converts a string to lowercase", "Returns the length of an object", "Rounds a number", "Sorts a list"],
        "answer": "Returns the length of an object"
    },
    {
        "question": "How do you write a single-line comment in Python?",
        "options": ["// comment", "/* comment */", "# comment", "<!-- comment -->"],
        "answer": "# comment"
    },
    {
        "question": "Which of these creates an empty dictionary?",
        "options": ["dict = []", "dict = ()", "dict = {}", "dict = \"\""],
        "answer": "dict = {}"
    },
    {
        "question": "Which of these is a valid variable name in Python?",
        "options": ["2score", "score_2", "score-2", "score 2"],
        "answer": "score_2"
    },
    {
        "question": "What is the output of: print(type(3.0))?",
        "options": ["<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'bool'>"],
        "answer": "<class 'float'>"
    },
    {
        "question": "Which loop is used to repeat code a fixed number of times using range()?",
        "options": ["while loop", "for loop", "do-while loop", "repeat loop"],
        "answer": "for loop"
    },
    {
        "question": "What does the 'in' keyword check for in an if statement, e.g. if 'a' in my_list?",
        "options": ["Data type", "Membership", "Length", "Index position"],
        "answer": "Membership"
    },
    {
        "question": "Which operator is used for exponentiation (power) in Python?",
        "options": ["^", "**", "%%", "exp()"],
        "answer": "**"
    },
    {
        "question": "What does the input() function always return?",
        "options": ["An integer", "A string", "A boolean", "A list"],
        "answer": "A string"
    },
    {
        "question": "Which of these correctly checks if a number is even?",
        "options": ["num % 2 == 0", "num / 2 == 0", "num // 2", "num * 2 == 0"],
        "answer": "num % 2 == 0"
    },
]

current_question = 0
score = 0

window = tk.Tk()
window.title("Quiz App")
window.geometry("500x400")

question_label = tk.Label(window, text="", font=("Arial", 14), wraplength=400)
question_label.pack(pady=30)

option_buttons = []
for i in range(4):
    btn = tk.Button(window, text="", font=("Arial", 12), width=30,
                     command=lambda i=i: check_answer(i))
    btn.pack(pady=5)
    option_buttons.append(btn)


def load_question():
    question_data = questions[current_question]
    question_label.config(text=question_data["question"])
    for i, option in enumerate(question_data["options"]):
        option_buttons[i].config(text=option)


def check_answer(button_index):
    global current_question, score
    question_data = questions[current_question]
    selected_option = option_buttons[button_index].cget("text")

    if selected_option == question_data["answer"]:
        score += 1

    current_question += 1

    if current_question < len(questions):
        load_question()
    else:
        show_final_score()


def show_final_score():
    question_label.config(text=f"You scored {score} out of {len(questions)}!")
    for btn in option_buttons:
        btn.pack_forget()


load_question()
window.mainloop()
