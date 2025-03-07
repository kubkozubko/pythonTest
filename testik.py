import tkinter as tk
from tkinter import colorchooser

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint Application")
        
        self.brush_color = "black"
        self.brush_size = 2
        
        self.canvas = tk.Canvas(self.root, bg="white", width=800, height=600)
        self.canvas.pack()

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<MouseWheel>", self.change_brush_size)

        self.color_button = tk.Button(self.root, text="Choose Color", command=self.choose_color)
        self.color_button.pack()

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

    def choose_color(self):
        self.brush_color = colorchooser.askcolor(color=self.brush_color)[1]

    def change_brush_size(self, event):
        if event.delta > 0:
            self.brush_size += 1
        else:
            self.brush_size -= 1
        self.brush_size = max(1, self.brush_size)  # Ensure brush size is at least 1

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()