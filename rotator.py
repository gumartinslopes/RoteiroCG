import tkinter as tk
import math

class RotatingCanvasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rotating Canvas")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        self.center_x = 200
        self.center_y = 200
        self.angle = 0

        self.object = self.canvas.create_rectangle(150, 150, 250, 250, fill="blue")

        self.rotation_button = tk.Button(root, text="Rotate", command=self.rotate_object)
        self.rotation_button.pack()

    def rotate_object(self):
        self.angle += 15  # Increase the angle by 15 degrees

        # Rotate the object using a rotation matrix
        radians = math.radians(self.angle)
        cos_theta = math.cos(radians)
        sin_theta = math.sin(radians)

        # Get the coordinates of the rectangle's corners
        coords = self.canvas.coords(self.object)
        original_points = [(coords[i], coords[i + 1]) for i in range(0, len(coords), 2)]

        # Rotate each corner point around the center
        rotated_points = [
            (
                self.center_x + (x - self.center_x) * cos_theta - (y - self.center_y) * sin_theta,
                self.center_y + (x - self.center_x) * sin_theta + (y - self.center_y) * cos_theta,
            )
            for x, y in original_points
        ]

        # Update the object's position
        new_coords = [coord for point in rotated_points for coord in point]
        self.canvas.coords(self.object, *new_coords)

        # Update the canvas
        self.canvas.update()

def main():
    root = tk.Tk()
    app = RotatingCanvasApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
