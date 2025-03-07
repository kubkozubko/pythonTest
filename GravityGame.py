import tkinter as tk
import random

class GravityGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Gravity Game")
        
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack()

        self.ball = self.canvas.create_oval(390, 290, 410, 310, fill="blue")
        self.finish_line = self.canvas.create_rectangle(0, 0, 50, 50, fill="red")
        self.score = 0
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}")
        self.score_label.pack()

        self.dx = 0
        self.dy = 0

        self.obstacles = []

        self.root.bind("<Up>", self.go_up)
        self.root.bind("<Down>", self.go_down)
        self.root.bind("<Left>", self.go_left)
        self.root.bind("<Right>", self.go_right)

        self.move_finish_line()
        self.update()

    def update(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        pos = self.canvas.coords(self.ball)
        if pos[1] <= 0 or pos[3] >= 600:
            self.dy = 0
        if pos[0] <= 0 or pos[2] >= 800:
            self.dx = 0

        if self.check_collision(self.finish_line):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.move_finish_line()
            self.spawn_obstacles()

        for obstacle in self.obstacles:
            if self.check_collision(obstacle):
                self.dx = 0
                self.dy = 0

        self.root.after(10, self.update)

    def go_up(self, event):
        self.dx = 0
        self.dy = -1 * (1 + self.score * 0.1)

    def go_down(self, event):
        self.dx = 0
        self.dy = 1 * (1 + self.score * 0.1)

    def go_left(self, event):
        self.dx = -1 * (1 + self.score * 0.1)
        self.dy = 0

    def go_right(self, event):
        self.dx = 1 * (1 + self.score * 0.1)
        self.dy = 0

    def move_finish_line(self):
        x1 = random.randint(0, 750)
        y1 = random.randint(0, 550)
        x2 = x1 + 50
        y2 = y1 + 50
        self.canvas.coords(self.finish_line, x1, y1, x2, y2)

    def spawn_obstacles(self):
        for obstacle in self.obstacles:
            self.canvas.delete(obstacle)
        self.obstacles.clear()

        for _ in range(self.score):
            x1 = random.randint(0, 750)
            y1 = random.randint(0, 550)
            x2 = x1 + 50
            y2 = y1 + 50
            obstacle = self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            self.obstacles.append(obstacle)

    def check_collision(self, item):
        ball_pos = self.canvas.coords(self.ball)
        item_pos = self.canvas.coords(item)
        return (ball_pos[2] >= item_pos[0] and ball_pos[0] <= item_pos[2] and
                ball_pos[3] >= item_pos[1] and ball_pos[1] <= item_pos[3])

if __name__ == "__main__":
    root = tk.Tk()
    game = GravityGame(root)
    root.mainloop()