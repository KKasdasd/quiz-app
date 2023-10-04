from tkinter import Tk, Canvas, Button, Label, PhotoImage, messagebox
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.minsize(width=300, height=500)
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, text="text", font=("Arial", 12, "italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, font=(
            "Arial", 12), fg="white")
        self.label.grid(row=0, column=1)

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(
            image=self.true_img, highlightthickness=0, borderwidth=0, command=self.true_answer)

        self.true_button.grid(row=2, column=0)
        self.false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(
            image=self.false_img, highlightthickness=0, borderwidth=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text, text=f"You've completed the quiz\nYour final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def false_answer(self):
        self.get_feedback(self.quiz.check_answer("true"))

    def true_answer(self):
        self.get_feedback(self.quiz.check_answer("false"))

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
