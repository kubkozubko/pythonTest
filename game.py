import tkinter as tk
import random
import time

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Game")
        self.root.geometry("400x400")
        
        self.colors = ["red", "green", "blue", "yellow"]
        self.buttons = []
        self.sequence = []
        self.player_sequence = []
        self.current_round = 0

        self.create_buttons()
        self.start_game()

    def create_buttons(self):
        for i, color in enumerate(self.colors):
            button = tk.Button(self.root, bg=color, width=10, height=5, command=lambda c=color: self.player_click(c))
            button.grid(row=i//2, column=i%2, padx=20, pady=20)
            self.buttons.append(button)

    def start_game(self):
        self.sequence = []
        self.player_sequence = []
        self.current_round = 0
        self.next_round()

    def next_round(self):
        self.current_round += 1
        self.player_sequence = []
        self.sequence.append(random.choice(self.colors))
        self.play_sequence()

    def play_sequence(self):
        for i, color in enumerate(self.sequence):
            self.root.after(1000 * i, lambda c=color: self.light_up(c))
        self.root.after(1000 * len(self.sequence), self.enable_buttons)

    def light_up(self, color):
        button = next(b for b in self.buttons if b.cget("bg") == color)
        button.config(state="normal")
        self.root.after(500, lambda: button.config(state="disabled"))

    def enable_buttons(self):
        for button in self.buttons:
            button.config(state="normal")

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state="disabled")

    def player_click(self, color):
        self.player_sequence.append(color)
        if self.player_sequence == self.sequence[:len(self.player_sequence)]:
            if len(self.player_sequence) == len(self.sequence):
                self.disable_buttons()
                self.root.after(1000, self.next_round)
        else:
            self.disable_buttons()
            self.root.after(1000, self.start_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()