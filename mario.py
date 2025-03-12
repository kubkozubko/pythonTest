import tkinter as tk
import random

class MarioGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mario Game")
        self.root.geometry("800x600")
        
        self.canvas = tk.Canvas(self.root, bg="skyblue", width=800, height=600)
        self.canvas.pack()

        self.ground = self.canvas.create_rectangle(0, 500, 1600, 600, fill="green")
        self.mario = self.canvas.create_rectangle(50, 450, 100, 500, fill="red")
        self.lucky_blocks = []
        self.coins = 0
        self.score_label = tk.Label(self.root, text=f"Coins: {self.coins}", font=("Arial", 20))
        self.score_label.pack()

        self.dx = 0
        self.dy = 0
        self.gravity = 1
        self.jump_speed = -15
        self.is_jumping = False

        self.root.bind("<Left>", self.move_left)
        self.root.bind("<Right>", self.move_right)
        self.root.bind("<space>", self.jump)

        self.create_lucky_blocks()
        self.update()

    def create_lucky_blocks(self):
        for _ in range(5):
            x = random.randint(200, 1600)
            y = random.randint(300, 400)
            block = self.canvas.create_rectangle(x, y, x + 50, y + 50, fill="yellow")
            self.lucky_blocks.append(block)

    def update(self):
        self.canvas.move(self.mario, self.dx, self.dy)
        self.dy += self.gravity

        mario_pos = self.canvas.coords(self.mario)
        if mario_pos[3] >= 500:
            self.dy = 0
            self.is_jumping = False
            self.canvas.coords(self.mario, mario_pos[0], 450, mario_pos[2], 500)

        for block in self.lucky_blocks:
            block_pos = self.canvas.coords(block)
            if self.check_collision(mario_pos, block_pos):
                if self.dy < 0:  # Mario hits the block with his head
                    self.dy = 0
                    self.coins += 1
                    self.score_label.config(text=f"Coins: {self.coins}")
                    self.canvas.delete(block)
                    self.lucky_blocks.remove(block)

        if self.dx != 0:
            for block in self.lucky_blocks:
                self.canvas.move(block, -self.dx, 0)
            self.canvas.move(self.ground, -self.dx, 0)

        self.root.after(20, self.update)

    def move_left(self, event):
        self.dx = -5

    def move_right(self, event):
        self.dx = 5

    def jump(self, event):
        if not self.is_jumping:
            self.dy = self.jump_speed
            self.is_jumping = True

    def check_collision(self, pos1, pos2):
        return (pos1[2] >= pos2[0] and pos1[0] <= pos2[2] and
                pos1[3] >= pos2[1] and pos1[1] <= pos2[3])

if __name__ == "__main__":
    root = tk.Tk()
    game = MarioGame(root)
    root.mainloop()