import tkinter as tk
def createEmptyNet():
    root = tk.Tk()
    root.geometry("500x500")
    root.title("Rubiks Cube")


    canvas = tk.Canvas(root, bg = "white")
    canvas.config(width = 500, height = 500)
    canvas.pack()

    #Creates the RED Face
    canvas.create_rectangle(150,100,180, 130)
    canvas.create_rectangle(180,100,210, 130)
    canvas.create_rectangle(210,100,240, 130)

    canvas.create_rectangle(150,130,180, 160)
    canvas.create_rectangle(180,130,210, 160)
    canvas.create_rectangle(210,130,240, 160)

    canvas.create_rectangle(150,160,180, 190)
    canvas.create_rectangle(180,160,210, 190)
    canvas.create_rectangle(210,160,240, 190)

    #Creates the White Face
    canvas.create_rectangle(150,190,180, 220)
    canvas.create_rectangle(180,190,210, 220)
    canvas.create_rectangle(210,190,240, 220)

    canvas.create_rectangle(150,220,180, 250)
    canvas.create_rectangle(180,220,210, 250)
    canvas.create_rectangle(210,220,240, 250)

    canvas.create_rectangle(150,250,180, 280)
    canvas.create_rectangle(180,250,210, 280)
    canvas.create_rectangle(210,250,240, 280)

    #Creates the Orange face
    canvas.create_rectangle(150,280,180, 310)
    canvas.create_rectangle(180,280,210, 310)
    canvas.create_rectangle(210,280,240, 310)

    canvas.create_rectangle(150,310,180, 340)
    canvas.create_rectangle(180,310,210, 340)
    canvas.create_rectangle(210,310,240, 340)

    canvas.create_rectangle(150,340,180, 370)
    canvas.create_rectangle(180,340,210, 370)
    canvas.create_rectangle(210,340,240, 370)

    #Creates the Green face
    canvas.create_rectangle(60,190,90, 220)
    canvas.create_rectangle(90,190,120, 220)
    canvas.create_rectangle(120,190,150, 220)

    canvas.create_rectangle(60,220,90, 250)
    canvas.create_rectangle(90,220,120, 250)
    canvas.create_rectangle(120,220,150, 250)

    canvas.create_rectangle(60,250,90, 280)
    canvas.create_rectangle(90,250,120, 280)
    canvas.create_rectangle(120,250,150, 280)

    #Creates Blue face
    canvas.create_rectangle(240,190,270, 220)
    canvas.create_rectangle(270,190,300, 220)
    canvas.create_rectangle(300,190,330, 220)

    canvas.create_rectangle(240,220,270, 250)
    canvas.create_rectangle(270,220,300, 250)
    canvas.create_rectangle(300,220,330, 250)

    canvas.create_rectangle(240,250,270, 280)
    canvas.create_rectangle(270,250,300, 280)
    canvas.create_rectangle(300,250,330, 280)

    #Creates Yellow Face
    canvas.create_rectangle(330,190,360, 220)
    canvas.create_rectangle(360,190,390, 220)
    canvas.create_rectangle(390,190,420, 220)

    canvas.create_rectangle(330,220,360, 250)
    canvas.create_rectangle(360,220,390, 250)
    canvas.create_rectangle(390,220,420, 250)

    canvas.create_rectangle(330,250,360, 280)
    canvas.create_rectangle(360,250,390, 280)
    canvas.create_rectangle(390,250,420, 280)

    root.mainloop()

