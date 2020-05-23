import tkinter as tk
# import os


class Gui:
    guiArray = []

    def guiCreate(self):

        window = tk.Tk()

        label = tk.Label(window, text='File Name')
        label.place(x=65, y=50)

        entry = tk.Entry(window)
        entry.insert(-1, 'input10.txt')
        entry.grid(row=0, column=1)
        entry.place(x=140, y=50)

        # files = os.listdir("files/")
        # files.sort()
        # fileDrop = tk.StringVar(window)
        # fileDrop.set(files[0])
        # drop1 = tk.OptionMenu(window, fileDrop, *files)
        # drop1.place(x=140, y=45)

        label = tk.Label(window, text='Algorithm')
        label.place(x=65, y=85)

        opt = ["MST (Prims)", "MST (Kruskal)", "SPT (Dijkstra)",
               "SPT (Bellman Ford)", "SPT (Floyd)"]
        varDrop = tk.StringVar(window)
        varDrop.set(opt[0])
        drop = tk.OptionMenu(window, varDrop, *opt)
        drop.place(x=140, y=80)

        varEdge = tk.IntVar()
        varWeight = tk.IntVar()
        edge = tk.Checkbutton(window, text="Show All Edges", variable=varEdge)
        weight = tk.Checkbutton(
            window, text="Show Edge Weights", variable=varWeight)
        edge.place(x=100, y=140)
        weight.place(x=100, y=160)

        def getGuiInput():
            temp = varDrop.get()
            for i in range(len(opt)):
                if opt[i] == temp:
                    self.guiArray = [
                        entry.get(), i, varEdge.get(), varWeight.get()]
                    window.destroy()

        button = tk.Button(window, text='Generate Graph',
                           width=25, command=getGuiInput)
        button.place(x=80, y=200)

        window.title('Graph')
        window.geometry("400x300+10+10")
        window.mainloop()


""" import tkinter as tk


class Gui:
    guiArray = []

    def guiCreate(self):

        window = tk.Tk()

        label = tk.Label(window, text='File Name')
        label.place(x=0, y=5)
        # label.pack()

        files = ["input10.txt", "input20.txt", "input30.txt", "input40.txt", "input50.txt",
                 "input60.txt", "input70.txt", "input80.txt", "input90.txt", "input100.txt", ]

        varDrop1 = tk.StringVar(window)
        varDrop1.set(files[0])
        drop1 = tk.OptionMenu(window, varDrop1, *files)
        drop1.place(x=80, y=0)
        # drop1.pack()

        label = tk.Label(window, text='Algorithm')
        label.place(x=0, y=40)
        # label.pack()

        opt = ["Prims", "Kruskal", "Dijkstra",
               "Bellman Ford", "Floyd"]

        varDrop = tk.StringVar(window)
        varDrop.set(opt[0])
        drop = tk.OptionMenu(window, varDrop, *opt)
        drop.place(x=80, y=35)
        # drop.pack()

        varEdge = tk.IntVar()
        # varWeight = tk.IntVar()
        # weight = tk.Checkbutton(
        #     window, text="Show Edge Weights", variable=varWeight)
        # weight.place(x=30, y=70)
        # # weight.pack()

        varWeight = True

        def getGuiInput():
            temp = varDrop.get()
            temp1 = varDrop1.get()
            for i in range(len(opt)):
                if opt[i] == temp:
                    for j in range(len(files)):
                        if files[j] == temp1:
                            self.guiArray = [
                                files[j], i, varEdge.get(), varWeight]
                            window.destroy()

        button = tk.Button(window, text='Show Result',
                           width=25, command=getGuiInput)
        button.place(x=0, y=70)
        # button.pack()

        window.title('Graph')
        window.geometry("230x105+10+10")
        window.mainloop()
 """
