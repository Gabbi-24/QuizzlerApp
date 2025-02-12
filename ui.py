from tkinter import *
from quiz_brain import QuizBrain
from data import parameters

THEME_COLOR = "#375362"
SCORE_FONT = ("Arial", 12)
QUESTION_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain_object: QuizBrain):   # Basically specifies that the input must be an object of QuizBrain
        self.quiz_brain_object = quiz_brain_object

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.true_img = PhotoImage(file="images\\right.png")
        self.false_img = PhotoImage(file="images\\wrong.png")

        self.create_canvas()
        self.create_buttons()
        self.create_labels()
        self.get_next_question()

        self.window.mainloop()


    def create_canvas(self):
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     text="Sample",
                                                     fill=THEME_COLOR,
                                                     font=QUESTION_FONT,
                                                     width=280)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)


    def create_buttons(self):
        self.button_true = Button()
        self.button_true.config(image=self.true_img,
                                bg=THEME_COLOR,
                                highlightthickness=0,
                                command=self.true_button_method)
        self.button_true.grid(column=0, row=2)

        self.button_false = Button()
        self.button_false.config(image=self.false_img,
                                 bg=THEME_COLOR,
                                 highlightthickness=0,
                                 command=self.false_button_method)
        self.button_false.grid(column=1, row=2)


    def create_labels(self):
        self.label_score = Label(text=f"Score: {self.quiz_brain_object.score}",
                                 font=SCORE_FONT,
                                 bg=THEME_COLOR,
                                 fg="white")
        self.label_score.grid(column=1, row=0, sticky="e")


    def get_next_question(self):
        self.canvas.config(bg="white")
        self.label_score.config(text=f"Score: {self.quiz_brain_object.score}")
        if self.quiz_brain_object.still_has_questions():
            q_text = self.quiz_brain_object.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"Quiz Complete!\n\n"
                                        f"Final Score: {self.quiz_brain_object.score}/{parameters["amount"]}",
                                   anchor="center",
                                   justify="center")


    def false_button_method(self):
        given_answer = "False"
        is_right = self.quiz_brain_object.check_answer(given_answer)
        self.give_feedback(is_right)


    def true_button_method(self):
        given_answer = "True"
        is_right = self.quiz_brain_object.check_answer(given_answer)
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)




