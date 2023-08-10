from tkinter import *
from tkinter import ttk
app = Tk()

v = ttk.Scrollbar(app, orient=VERTICAL)
h = ttk.Scrollbar(app, orient=HORIZONTAL)

canvas = Canvas(app, scrollregion=(0,0,1000,1000), 
                     yscrollcommand=v.set, xscrollcommand=h.set)

v['command'] = canvas.yview
h['command'] = canvas.xview

ttk.Sizegrip(app).grid(column=1, row=1, sticky=(S,E))
canvas.grid(column=0, row=0, sticky=(N,W,E,S))
v.grid(column = 1, row = 0, sticky=(N,S))
h.grid(column = 0, row = 1, sticky=(W,E))

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    print('Lasx', lastx)
    print('Lasy', lasty)
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag("all", "paletteSelected")
    canvas.itemconfigure("palette", outline = "white")
    canvas.addtag("paletteSelected", "withtag", "palette%s " % color)
    canvas.itemconfigure("paletteSelected", outline="#999999")

def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill = color, width=5, tags='currentline')
    lastx, lasty = x, y

def doneStroke(event):
    canvas.itemconfigure("currentline", width = 1)
    print(get_painted_pixels(canvas))

def get_painted_pixels(canvas):
    painted_pixels = []

    # Obter todos os itens desenhados no canvas
    items = canvas.find_all()
    #print(items)
    # Percorrer os itens e extrair as coordenadas dos pixels
    for item in items:
        tags = canvas.gettags(item)
        print(tags)
        if "palette" in tags:  # Certifique-se de marcar seus pixels ao desenhar
            x, y = canvas.coords(item)
            painted_pixels.append((int(x), int(y)))

    return painted_pixels

canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStroke)

id = canvas.create_rectangle((10, 10, 30, 30), fill = "red", tags=("palette", "pelettered"))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))

id = canvas.create_rectangle((10, 35, 30, 55), fill = "blue", tags=("palette", "peletteblue"))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))

id = canvas.create_rectangle((10, 60, 30, 80), fill = "black", tags=("palette", "peletteblack"))
canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

setColor("black")
canvas.itemconfigure("pallete", width=5)
app.mainloop()