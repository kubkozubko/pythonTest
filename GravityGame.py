import tkinter as tk
import random

class GravityGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Gravity Game")
        self.root.attributes('-fullscreen', True)
        
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.start_screen()

    def start_screen(self):
        self.canvas.delete("all")
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game, font=("Arial", 20))
        self.start_button.pack(pady=20)
        self.canvas.create_text(self.root.winfo_screenwidth() // 2, self.root.winfo_screenheight() // 2, text="Gravity Game", font=("Arial", 50), fill="black")

    def start_game(self):
        if hasattr(self, 'start_button'):
            self.start_button.pack_forget()
        if hasattr(self, 'play_again_button'):
            self.play_again_button.pack_forget()
        if hasattr(self, 'score_label'):
            self.score_label.pack_forget()
        self.canvas.delete("all")
        self.score = 0
        self.dx = 0
        self.dy = 0
        self.obstacles = []

        self.ball = self.canvas.create_oval(390, 290, 410, 310, fill="blue")
        self.finish_line = self.canvas.create_rectangle(0, 0, 50, 50, fill="red")
        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 20))
        self.score_label.pack()

        self.root.bind("<Up>", self.go_up)
        self.root.bind("<Down>", self.go_down)
        self.root.bind("<Left>", self.go_left)
        self.root.bind("<Right>", self.go_right)

        self.move_finish_line()
        self.update()

    def update(self):
        self.canvas.move(self.ball, self.dx, self.dy)
        pos = self.canvas.coords(self.ball)
        if pos[1] <= 0 or pos[3] >= self.root.winfo_screenheight():
            self.dy = 0
        if pos[0] <= 0 or pos[2] >= self.root.winfo_screenwidth():
            self.dx = 0

        if self.check_collision(self.finish_line):
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.dx = 0
            self.dy = 0
            self.move_finish_line()
            self.spawn_obstacles()

        for obstacle in self.obstacles:
            if self.check_collision(obstacle):
                self.end_game()
                return

        self.root.after(10, self.update)

    def go_up(self, event):
        self.dx = 0
        self.dy = -2 * (1 + self.score * 0.1)  # Increased initial speed

    def go_down(self, event):
        self.dx = 0
        self.dy = 2 * (1 + self.score * 0.1)  # Increased initial speed

    def go_left(self, event):
        self.dx = -2 * (1 + self.score * 0.1)  # Increased initial speed
        self.dy = 0

    def go_right(self, event):
        self.dx = 2 * (1 + self.score * 0.1)  # Increased initial speed
        self.dy = 0

    def move_finish_line(self):
        x1 = random.randint(0, self.root.winfo_screenwidth() - 50)
        y1 = random.randint(0, self.root.winfo_screenheight() - 50)
        x2 = x1 + 50
        y2 = y1 + 50
        self.canvas.coords(self.finish_line, x1, y1, x2, y2)

    def spawn_obstacles(self):
        for obstacle in self.obstacles:
            self.canvas.delete(obstacle)
        self.obstacles.clear()

        for _ in range(self.score):
            shape_type = random.choice(['rectangle', 'oval', 'triangle'])
            x1 = random.randint(0, self.root.winfo_screenwidth() - 50)
            y1 = random.randint(0, self.root.winfo_screenheight() - 50)
            x2 = x1 + 50
            y2 = y1 + 50

            if shape_type == 'rectangle':
                obstacle = self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")
            elif shape_type == 'oval':
                obstacle = self.canvas.create_oval(x1, y1, x2, y2, fill="black")
            elif shape_type == 'triangle':
                obstacle = self.canvas.create_polygon(x1, y2, (x1 + x2) // 2, y1, x2, y2, fill="black")

            self.obstacles.append(obstacle)

    def check_collision(self, item):
        ball_pos = self.canvas.coords(self.ball)
        item_pos = self.canvas.coords(item)
        return (ball_pos[2] >= item_pos[0] and ball_pos[0] <= item_pos[2] and
                ball_pos[3] >= item_pos[1] and ball_pos[1] <= item_pos[3])

    def end_game(self):
        self.dx = 0
        self.dy = 0
        self.canvas.create_text(self.root.winfo_screenwidth() // 2, self.root.winfo_screenheight() // 2, text="Game Over", font=("Arial", 50), fill="red")
        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.start_game, font=("Arial", 20))
        self.play_again_button.pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    game = GravityGame(root)
    root.mainloop()