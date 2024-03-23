import tkinter as tk
import random

class HolidayGreetingGenerator:
    def __init__(self, master):
        self.master = master
        master.title("🎄 Holiday Greeting Generator 🎅")

        self.greetings = [
            "Merry Christmas!",
            "Happy Hanukkah!",
            "Joyous Kwanzaa!",
            "Season's Greetings!",
            "Happy New Year!",
        ]

        self.greeting_label = tk.Label(master, text="Generated Greeting", font=("Arial", 16))
        self.greeting_label.pack(pady=10)

        self.generate_button = tk.Button(master, text="Generate Greeting", command=self.generate_greeting, font=("Arial", 14))
        self.generate_button.pack(pady=20)

    def generate_greeting(self):
        random_greeting = random.choice(self.greetings)
        self.greeting_label.config(text=random_greeting)

# Creating the Tkinter root window
root = tk.Tk()
app = HolidayGreetingGenerator(root)

# Running the GUI
root.mainloop()