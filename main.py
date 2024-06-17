from tkinter import *
import pyscreenrec

root = Tk()
root.geometry("400x600")
root.title("Screen Recorder")
root.config(bg="#000000")
root.resizable(False, False)

def start_rec():
    file = Filename.get()
    rec.start_recording(str(file + ".mp4"), 5)

def pause_rec():
    rec.pause_recording()

def resume_rec():
    rec.resume_recording()

def stop_rec():
    rec.stop_recording()

rec = pyscreenrec.ScreenRecorder()

# icon
image_icon = PhotoImage(file="camera.png")
root.iconphoto(False, image_icon)

# background images
image1 = PhotoImage(file="test (1).png")
Label(root, image=image1, bg="#000000").place(x=-2, y=35)

image2 = PhotoImage(file="test2 (1).png")
Label(root, image=image2, bg="#000000").place(x=223, y=200)

# heading
lbl = Label(root, text="Screen Recorder",fg="white", bg="#221C1C", font="arial 15 bold")
lbl.pack(pady=20)

image3 = PhotoImage(file="recording.png")
Label(root, image=image3, bd=0).pack(pady=30)

# entry
Filename = StringVar()
entry = Entry(root, textvariable=Filename, width=18, font="arial 15")
entry.place(x=100, y=350)
Filename.set("your_recording")

# buttons
start = Button(root, text="Start", font="arial 22", bd=0, command=start_rec)
start.place(x=140, y=250)

image4 = PhotoImage(file="pause.png")
pause = Button(root, image=image4, bd=0, bg="#000000", command=pause_rec)
pause.place(x=65, y=450)

image5 = PhotoImage(file="resume.png")
resume = Button(root, image=image5, bd=0, bg="#000000", command=resume_rec)
resume.place(x=165, y=450)

image6 = PhotoImage(file="stop.png")
stop = Button(root, image=image6, bd=0, bg="#000000", command=stop_rec)
stop.place(x=265, y=450)

root.mainloop()
