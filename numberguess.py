import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.secret_number = 0
        self.max_attempts = 5
        self.attempts = 0

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Welcome to the Number Guessing Game!", font=("Helvetica", 14), bg="lightgreen", fg="blue")
        self.label.pack(pady=50)

        self.guess_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.guess_entry.pack(pady=50)

        self.guess_button = tk.Button(self.master, text="Submit Guess", command=self.check_guess, font=("Helvetica", 12), bg="green", fg="white")
        self.guess_button.pack(pady=30)

        self.play_again_button = tk.Button(self.master, text="Play Again", command=self.start_new_game, font=("Helvetica", 12), bg="orange", fg="white")
        self.play_again_button.pack_forget()

        self.exit_button = tk.Button(self.master, text="Exit", command=self.master.destroy, font=("Helvetica", 12), bg="red", fg="white")
        self.exit_button.pack(pady=30)

        self.attempts_label = tk.Label(self.master, text="", font=("Helvetica", 12), fg="purple")
        self.attempts_label.pack(pady=30)

    def start_new_game(self):
        self.secret_number = random.randint(1, 20)
        self.attempts = 0
        self.label.config(text="I have selected a random number between 1 and 20. Can you guess it? \n You have 5 chances!!", fg="blue")
        self.play_again_button.pack_forget()
        self.guess_button.config(state=tk.NORMAL)
        self.update_attempts_label()

    def check_guess(self):
        try:
            user_guess = int(self.guess_entry.get())
            self.attempts += 1

            if user_guess == self.secret_number:
                messagebox.showinfo("Congratulations!", f"You guessed the correct number {self.secret_number}!", icon="info")
                self.play_again_button.pack()
                self.guess_button.config(state=tk.DISABLED)
            elif user_guess < self.secret_number:
                messagebox.showinfo("Incorrect Guess", "Try a higher number.", icon="warning")
            else:
                messagebox.showinfo("Incorrect Guess", "Try a lower number.", icon="warning")

            if self.attempts >= self.max_attempts:
                messagebox.showinfo("Game Over", f"Sorry, you've reached the maximum number of attempts. The correct number was {self.secret_number}!")
                self.play_again_button.pack()
                self.guess_button.config(state=tk.DISABLED)
            else:
                self.update_attempts_label()

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    def update_attempts_label(self):
        attempts_left = self.max_attempts - self.attempts
        self.attempts_label.config(text=f"Attempts left: {attempts_left}", fg="purple")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x350")
    root.configure(bg="lightgray")
    game = NumberGuessingGame(root)
    game.start_new_game()
    root.mainloop()
