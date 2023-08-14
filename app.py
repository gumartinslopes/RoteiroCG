from tkinter import *
import customtkinter as ctk
from PIL import ImageDraw
import PIL
from tkinter import filedialog, messagebox, colorchooser
from point import Point


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Roteiro de Computação Gráfica")
        self.width = 1200
        self.height = 600

        CANVAS_WIDTH = 500
        CANVAS_HEIGHT = 600
        
        self.geometry(f"{self.width}x{self.height}")
        self.center_window()
        
        self.point_list = []
        self.brush_width = 15
        self.current_color = "#000000"

        self.cnv = Canvas(self, width= CANVAS_WIDTH - 10, height=CANVAS_HEIGHT - 10, bg = "#ffffff")
        self.configure_canvas()
        
        self.image = PIL.Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT), (255,255,255))
        self.draw = ImageDraw.Draw(self.image)

        self.btn_frame = ctk.CTkFrame(self)
        self.configure_btn_frame()

    def configure_canvas(self):
        self.cnv.grid(row = 0, column=0, sticky=W)
        self.cnv.bind("<B1-Motion>", self.paint)

    def configure_btn_frame(self):
        self.btn_frame.grid(row = 0, column = 1, sticky = E)
        self.btn_frame.columnconfigure(0, weight = 1)
        self.btn_frame.columnconfigure(1, weight = 1)
        self.btn_frame.columnconfigure(2, weight = 1)

        self.clear_btn = ctk.CTkButton(self.btn_frame, text = "Clear", command = self.clear)
        self.save_btn = ctk.CTkButton(self.btn_frame, text="Save", command=self.save)
        self.bplus_btn = ctk.CTkButton(self.btn_frame, text = "B+", command = self.brush_plus)
        self.bminus_btn = ctk.CTkButton(self.btn_frame, text = "B-", command = self.brush_minus)
        self.color_btn = ctk.CTkButton(self.btn_frame, text = "Color", command = self.change_color)
        self.translate_btn = ctk.CTkButton(self.btn_frame, text="Translate", command=self.translate)

        self.clear_btn.grid(row = 1, column=0, sticky=W + E)
        self.save_btn.grid(row = 1, column=2, sticky=W + E)
        self.bplus_btn.grid(row = 0, column=0, sticky=W + E)
        self.bminus_btn.grid(row = 0, column=1, sticky=W + E)
        self.color_btn.grid(row = 1, column=1, sticky=W + E)
        self.translate_btn.grid(row = 0, column=2, sticky=W + E)
        
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width/2) - (self.width/2)
        y = (screen_height/2) - (self.height/2)

        # centralizacao da janela
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y-50))

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.point_list.append(Point(x1, y1, self.current_color))
        self.cnv.create_rectangle(x1,y1,x2,y2, 
                                  outline=self.current_color, fill = self.current_color, width=self.brush_width)
        self.draw.rectangle(
            [x1, y1, x2 + self.brush_width, y2 + self.brush_width],
            outline=self.current_color, fill=self.current_color, width = self.brush_width)
        
    def translate(self):
        point_list = self.point_list
        self.clear()
        translation_coefficient = 100;
        for point in point_list:
            x1, y1 = (point.x - 1) + translation_coefficient, (point.y - 1) + translation_coefficient
            x2, y2 = (point.x + 1) + translation_coefficient, (point.y + 1) + translation_coefficient
            self.cnv.create_rectangle(x1,y1,x2,y2, 
                                    outline=point.color, fill = point.color, width=self.brush_width)
            self.draw.rectangle(
                [x1, y1, x2 + self.brush_width, y2 + self.brush_width],
                outline=point.color, fill=point.color, width = self.brush_width)
            self.point_list.append(Point(x1, y1, point.color))
            
    def save(self):
        filename = filedialog.asksaveasfilename(initialfile="untitled.png", defaultextension="png")
        if filename != "":
            self.image.save(filename)
                                    

    def brush_plus(self):
        self.brush_width += 1

    def brush_minus(self):
        if self.brush_width > 1:
            self.brush_width -= 1

    def clear(self):
        self.cnv.delete("all")
        self.draw.rectangle([0, 0, 1000, 1000], fill = "white")
        self.point_list = []

    def change_color(self):
        _, self.current_color = colorchooser.askcolor(title="Choose a color")
app = App()
app.mainloop()