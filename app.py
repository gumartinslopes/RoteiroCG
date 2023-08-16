from tkinter import *
import customtkinter as ctk
from PIL import ImageDraw
import PIL
from tkinter import filedialog, messagebox, colorchooser,simpledialog
from point import Point
from transforms import *
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Roteiro de Computação Gráfica")
        self.width = 1200
        self.height = 600

        self.geometry(f"{self.width}x{self.height}")
        self.center_window()
        
        self.point_list = []
        self.brush_width = 5
        self.current_color = "#000000"

        self.cnv = Canvas(self, width= CANVAS_WIDTH - 10, height=CANVAS_HEIGHT - 10, bg = "#ffffff")
        self.configure_canvas()
        self.canvas_center = self.compute_center_coords()
        self.draw_axis()
        self.image = PIL.Image.new("RGB", (CANVAS_WIDTH, CANVAS_HEIGHT), (255,255,255))
        self.draw = ImageDraw.Draw(self.image)

        self.btn_frame = ctk.CTkFrame(self)
        self.configure_btn_frame()

    def compute_center_coords(self):
        self.cnv.update_idletasks()  # Atualizar tarefas pendentes para garantir medidas precisas
        canvas_width = self.cnv.winfo_reqwidth()
        canvas_height = self.cnv.winfo_reqheight()
        return canvas_width / 2, canvas_height / 2

    def configure_canvas(self):
        self.cnv.grid(row = 0, column=0, sticky=W)
        self.cnv.bind("<B1-Motion>", self.paint)
        self.cnv.bind("<Motion>", self.update_coords_info)

    def draw_axis(self):
        # Draw a red line on the canvas
        x_axis_x1, x_axis_y1 = 0,self.canvas_center[1]
        x_axis_x2, x_axis_y2 = CANVAS_WIDTH, self.canvas_center[1]

        y_axis_x1, y_axis_y1 = self.canvas_center[0],0
        y_axis_x2, y_axis_y2 = self.canvas_center[0], CANVAS_HEIGHT
       
        self.cnv.create_line(x_axis_x1, x_axis_y1,x_axis_x2, x_axis_y2, fill="red", width=2, tags="x_axis")
        self.cnv.create_line(y_axis_x1, y_axis_y1,y_axis_x2,y_axis_y2, fill="red", width=2, tags="y_axis")
        
    def configure_btn_frame(self):
        self.btn_frame.grid(row = 0, column = 1, sticky = E+W+S+N)
        self.btn_frame.columnconfigure(0, weight = 1)
        self.btn_frame.columnconfigure(1, weight = 1)
        self.btn_frame.columnconfigure(2, weight = 1)

        self.clear_btn = ctk.CTkButton(self.btn_frame, text = "Clear", command = self.clear)
        self.save_btn = ctk.CTkButton(self.btn_frame, text="Save", command=self.save)
        self.color_btn = ctk.CTkButton(self.btn_frame, text = "Color", command = self.change_color)
        self.translate_btn = ctk.CTkButton(self.btn_frame, text="Translate", command=self.translate)
        self.rotate_btn = ctk.CTkButton(self.btn_frame, text="Rotate around center", command=self.rotate)

        self.mirror_x_btn = ctk.CTkButton(self.btn_frame, text="X Axis Mirroring", command=lambda: self.mirror(axis = "x"))
        self.mirror_y_btn = ctk.CTkButton(self.btn_frame, text="Y Axis Mirroring", command=lambda: self.mirror(axis = 'y'))
        self.mirror_both_btn = ctk.CTkButton(self.btn_frame, text="Both Axis Mirroring", command=lambda: self.mirror(axis = "both"))

        self.coords_label = ctk.CTkLabel(master=self.btn_frame, text="Coords: (x, y)")

        self.clear_btn.grid(row = 1, column=0,padx = 20,pady = 20,   sticky=W + E)
        self.save_btn.grid(row = 1, column=2,padx = 20, pady = 20,sticky=W + E)
        self.color_btn.grid(row = 1, column=1,padx = 20,pady = 20, sticky=W + E)
        self.translate_btn.grid(row = 0, column=2,padx = 20, pady = 20, sticky=W + E)
        self.rotate_btn.grid(row = 0, column=1,padx = 20, pady = 20, sticky=W + E)
        self.mirror_x_btn.grid(row = 4, column=0,padx = 20, pady = 20, sticky=W + E)
        self.mirror_y_btn.grid(row = 4, column=1,padx = 20, pady = 20, sticky=W + E)
        self.mirror_both_btn.grid(row = 4, column=2,padx = 20, pady = 20, sticky=W + E)
        
        self.coords_label.grid(row = 5, column = 0, padx = 20,sticky = S + W)
        
        
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
    
    def update_coords_info(self, event):
        self.coords_label.configure(text = f"Coords: ({event.x - self.canvas_center[0]}, {event.y - self.canvas_center[1]})")

    def rotate(self):
        theta = simpledialog.askinteger("Rotation Angle", "Insert the rotation angle.")
        #self.translate(-self.canvas_center[0], -self.canvas_center[1])
        point_list = self.point_list
        self.clear()
        for point in point_list:
            new_x, new_y = rotation(point.x - self.canvas_center[0], point.y - self.canvas_center[1], theta)
            print("")
            new_x = new_x + self.canvas_center[0]# + CANVAS_WIDTH
            new_y = new_y + self.canvas_center[1]#+ CANVAS_HEIGHT
            self.cnv.create_rectangle(new_x,new_y,new_x,new_y, 
                                    outline=point.color, fill = point.color, width=self.brush_width)
            self.draw.rectangle(
                [new_x, new_y, new_x + self.brush_width, new_y + self.brush_width],
                outline=point.color, fill=point.color, width = self.brush_width)
            self.point_list.append(Point(new_x, new_y, point.color))
    
    def translate(self, tx = None, ty = None):
        if tx == None:
            tx = simpledialog.askfloat("Translation coefficient", "Insert tx")
        if ty == None:
            ty = simpledialog.askfloat("Translation coefficient", "Insert ty")
        point_list = self.point_list
        self.clear()
        for point in point_list:
            new_x, new_y = translation(point.x, point.y, tx, ty)
            self.cnv.create_rectangle(new_x,new_y,new_x,new_y, 
                                    outline=point.color, fill = point.color, width=self.brush_width)
            self.draw.rectangle(
                [new_x, new_y, new_x + self.brush_width, new_y + self.brush_width],
                outline=point.color, fill=point.color, width = self.brush_width)
            self.point_list.append(Point(new_x, new_y, point.color))
    
    def mirror(self, axis):
        point_list = self.point_list
        self.clear()
        for point in point_list:
            new_x, new_y = mirroring(point.x, point.y, self.canvas_center, axis)
            print(f"Old->x:{point.x}, y:{point.y}")
            print(f"x:{new_x}, y:{new_y}")
            self.cnv.create_rectangle(new_x,new_y,new_x,new_y, 
                                    outline=point.color, fill = point.color, width=self.brush_width)
            self.draw.rectangle(
                [new_x, new_y, new_x + self.brush_width, new_y + self.brush_width],
                outline=point.color, fill=point.color, width = self.brush_width)
            self.point_list.append(Point(new_x, new_y, point.color))
            
    def save(self):
        filename = filedialog.asksaveasfilename(initialfile="untitled.png", defaultextension="png")
        if filename != "":
            self.image.save(filename)
                                    
    def clear(self):
        self.cnv.delete("all")
        self.draw.rectangle([0, 0, 1000, 1000], fill = "white")
        self.point_list = []
        self.draw_axis()

    def change_color(self):
        _, self.current_color = colorchooser.askcolor(title="Choose a color")
app = App()
app.mainloop()