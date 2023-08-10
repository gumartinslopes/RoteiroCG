import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Roteiro de Computação Gráfica")
        self.width = 1200
        self.height = 600
        self.geometry(f"{self.width}x{self.height}")
        self.center_window()

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width/2) - (self.width/2)
        y = (screen_height/2) - (self.height/2)

        # centralizacao da janela
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, x, y-50))