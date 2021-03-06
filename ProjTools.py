import pathlib
from tkinter import *
from tkinter import font
from tkmacosx import Button
from PIL import Image


def create_home_button(self, controller, frame):
    buttonFont = font.Font(family='Helvetica', size=16)

    # Travel Button
    home = Button(self, text="Home", font=buttonFont, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                  activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D',
                  command=lambda: controller.show_frame(frame))
    home.place(x=10, y=-10, relx=0.0, rely=1.0, anchor=SW)


def create_Frame_label(root, text):
    home_label = Label(root, text=text, font=font.Font(family='Helvetica', size=20), bg='#EBDEF0', bd=3)
    home_label.place(relx=0.5, rely=0.1, anchor=CENTER)


def file_checker(entry):
    directory = pathlib.Path(entry.get())
    hold = entry.get()
    if hold == '':
        directory = ''
    if directory != '' and directory.exists():
        return True
    else:
        return False


def format_vars(string):
    return str(string).strip()


def listToString(s):  # GeeksForGeeks
    str1 = ""
    for ele in s:
        str1 += ele
    return str1


def db_validator(result, row, col):
    if len(result) == 0:
        result = None
    else:
        result = result[row][col]

    return result


def img_transparent(path):
    img = Image.open(path)
    img = img.convert("RGBA")
    data = img.getdata()

    newData = []
    for item in data:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            if item[0] > 150:
                newData.append((0, 0, 0, 255))
            else:
                newData.append(item)

    img.putdata(newData)
    img.save(path, "PNG")
