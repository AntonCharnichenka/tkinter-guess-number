"""This module represents a 'guess number' game application"""

# import
import tkinter
import random


class Application(tkinter.Frame):
    """A model of game application"""
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        self.create_widgets()
        self.number = random.randint(1, 101)  # a number that user have to guess
        self.tries = 0  # user's tries to guess the number

    def create_widgets(self):
        """creates widgets necessary for the game"""
        # create instruction label
        tkinter.Label(self, text="The computer is thinking of a number between 1 and 100. "
                                 "Try to guess it!").grid(row=0, column=0, columnspan=3, sticky=tkinter.W)
        # create a label, a text entry and a button to accept player's suggestion
        tkinter.Label(self, text="Your suggestion?: ").grid(row=1, column=0, sticky=tkinter.W)
        self.suggestion_entry = tkinter.Entry(self)
        self.suggestion_entry.grid(row=1, column=1, sticky=tkinter.W)
        tkinter.Button(self, text="Submit", command=self.check_suggestion).grid(row=1, column=2, sticky=tkinter.W)
        # create a text region to display computer's response
        self.response_txt = tkinter.Text(self, width=48, height=5, wrap=tkinter.WORD)
        self.response_txt.grid(row=2, column=0, columnspan=3)

    def check_suggestion(self):
        """checks user suggestion"""
        try:
            suggestion = int(self.suggestion_entry.get())
            if suggestion > self.number:
                response = "Lower...\n\n"
            elif suggestion < self.number:
                response = "Higher...\n\n"
            else:
                response = "Yes! You've guessed it! It was: {}\n\n".format(str(self.number))
            self.tries += 1
        except Exception:
            response = "You haven't entered any number!\n\n"
        
        # display the response
        self.response_txt.delete(0.0, tkinter.END)
        self.response_txt.insert(0.0, "{}You've used: {} tries.".format(response, str(self.tries)))


# main
root = tkinter.Tk()
root.title("Guess a number")
app = Application(root)
root.mainloop()
