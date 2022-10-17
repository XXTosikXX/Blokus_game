import winsound
import tkinter

#winsound.PlaySound('hehe boii.wav', winsound.SND_FILENAME|winsound.SND_LOOP|winsound.SND_ASYNC)


tk = tkinter.Tk()
tk.geometry("600x300")

def sound():
    winsound.PlaySound('Sounds/undo.wav', winsound.SND_FILENAME|winsound.SND_ASYNC)

Button = tkinter.Button(tk, text="Play Sound", command=sound).pack()
tk.mainloop()
