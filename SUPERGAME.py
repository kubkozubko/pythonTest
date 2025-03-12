import tkinter as tk
import random

class SlitherGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Slither.io Game")
        self.root.geometry("800x600")
        
        self.canvas = tk.Canvas(self.root, bg="black", width=800, height=600)
        self.canvas.pack()

        self.snake1 = [(20, 20), (20, 30), (20, 40)]
        self.snake2 = [(780, 580), (780, 570), (780, 560)]
        self.snake1_squares = []
        self.snake2_squares = []
        self.food = None
        self.direction1 = "Down"
        self.direction2 = "Up"
        self.game_over = False

        self.create_snake(self.snake1, self.snake1_squares, "green")
        self.create_snake(self.snake2, self.snake2_squares, "blue")
        self.create_food()

        self.root.bind("<Up>", self.go_up1)
        self.root.bind("<Down>", self.go_down1)
        self.root.bind("<Left>", self.go_left1)
        self.root.bind("<Right>", self.go_right1)
        self.root.bind("w", self.go_up2)
        self.root.bind("s", self.go_down2)
        self.root.bind("a", self.go_left2)
        self.root.bind("d", self.go_right2)

        self.update()

    def create_snake(self, snake, snake_squares, color):
        for x, y in snake:
            square = self.canvas.create_rectangle(x, y, x+10, y+10, fill=color)
            snake_squares.append(square)

    def create_food(self):
        if self.food:
            self.canvas.delete(self.food)
        x = random.randint(0, 79) * 10
        y = random.randint(0, 59) * 10
        self.food = self.canvas.create_rectangle(x, y, x+10, y+10, fill="red")

    def update(self):
        if self.game_over:
            self.canvas.create_text(400, 300, text="Game Over", fill="white", font=("Arial", 30))
            return

        self.move_snake(self.snake1, self.snake1_squares, self.direction1, "green")
        self.move_snake(self.snake2, self.snake2_squares, self.direction2, "blue")
        self.check_collisions()
        self.root.after(100, self.update)

    def move_snake(self, snake, snake_squares, direction, color):
        head_x, head_y = snake[-1]
        if direction == "Up":
            new_head = (head_x, head_y - 10)
        elif direction == "Down":
            new_head = (head_x, head_y + 10)
        elif direction == "Left":
            new_head = (head_x - 10, head_y)
        elif direction == "Right":
            new_head = (head_x + 10, head_y)

        snake.append(new_head)
        square = self.canvas.create_rectangle(new_head[0], new_head[1], new_head[0]+10, new_head[1]+10, fill=color)
        snake_squares.append(square)

        if self.check_food_collision(new_head):
            self.create_food()
        else:
            tail = snake.pop(0)
            self.canvas.delete(snake_squares.pop(0))

    def check_food_collision(self, head):
        food_coords = self.canvas.coords(self.food)
        return head[0] == food_coords[0] and head[1] == food_coords[1]

    def check_collisions(self):
        head1_x, head1_y = self.snake1[-1]
        head2_x, head2_y = self.snake2[-1]

        if head1_x < 0 or head1_x >= 800 or head1_y < 0 or head1_y >= 600:
            self.game_over = True
        if head2_x < 0 or head2_x >= 800 or head2_y < 0 or head2_y >= 600:
            self.game_over = True
        if len(self.snake1) != len(set(self.snake1)):
            self.game_over = True
        if len(self.snake2) != len(set(self.snake2)):
            self.game_over = True
        if (head1_x, head1_y) in self.snake2 or (head2_x, head2_y) in self.snake1:
            self.game_over = True

    def go_up1(self, event):
        if self.direction1 != "Down":
            self.direction1 = "Up"

    def go_down1(self, event):
        if self.direction1 != "Up":
            self.direction1 = "Down"

    def go_left1(self, event):
        if self.direction1 != "Right":
            self.direction1 = "Left"

    def go_right1(self, event):
        if self.direction1 != "Left":
            self.direction1 = "Right"

    def go_up2(self, event):
        if self.direction2 != "Down":
            self.direction2 = "Up"

    def go_down2(self, event):
        if self.direction2 != "Up":
            self.direction2 = "Down"

    def go_left2(self, event):
        if self.direction2 != "Right":
            self.direction2 = "Left"

    def go_right2(self, event):
        if self.direction2 != "Left":
            self.direction2 = "Right"

if __name__ == "__main__":
    root = tk.Tk()
    game = SlitherGame(root)
    root.mainloop()