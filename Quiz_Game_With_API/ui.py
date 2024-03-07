from tkinter import *
from quiz_brain import QuizBrain
import time
THEME_COLOR = '#375362'

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        #Window itself
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        #Images
        right = PhotoImage(file='right.png')
        wrong = PhotoImage(file='wrong.png')

        #Canvas for question
        self.canvas = Canvas(height=250, width=300, bg='white')
        self.question_text = self.canvas.create_text(150, 125,
                                                     text='Put question here',
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=('Arial', 20, 'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2,pady=50)

        #Labels
        self.score_label = Label(text=f'Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Buttons
        self.true = Button(image=right, highlightthickness=0, bg=THEME_COLOR, padx=20, pady=20, command=self.true_pressed)
        self.true.grid(row=2, column=0)
        self.false = Button(image=wrong, highlightthickness=0, bg=THEME_COLOR,padx=20, pady=20, command=self.false_pressed)
        self.false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz!")
            self.true.config(state='disabled')
            self.false.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)


