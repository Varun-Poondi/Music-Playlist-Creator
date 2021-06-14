from tkinter import CENTER, SW
from tkmacosx import Button
import Youtube_Video_Downloader as YT
import PlayLists as PL
import tkinter.font as font
import tkinter as tk


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#EBDEF0')

        # Travel Buttons
        buttonFont = font.Font(family='Helvetica', size=16)
        video_downloader = Button(self, text='Video Downloader', font=buttonFont, bg='#A3E4D7', fg='#5F4B8B',
                                  borderless=1,
                                  activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=80, pady=20,
                                  command=lambda: controller.show_frame(SecondPage))
        playlists = Button(self, text='Your Playlists', font=buttonFont, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                           activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D', padx=96, pady=20,
                           command=lambda: controller.show_frame(ThirdPage))
        video_downloader.place(y=-40, relx=0.5, rely=0.5, anchor=CENTER)
        playlists.place(y=20, relx=0.5, rely=0.5, anchor=CENTER)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#EBDEF0')
        buttonFont = font.Font(family='Helvetica', size=16)

        # Travel Button
        home = Button(self, text="Home", font=buttonFont, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                      activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D',
                      command=lambda: controller.show_frame(FirstPage))
        home.place(x=10, y=-10, relx=0.0, rely=1.0, anchor=SW)

        YT.YoutubeDownloader(self)


class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='#EBDEF0')

        buttonFont = font.Font(family='Helvetica', size=16)

        b = Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        b.place(x=650, y=450)

        home = Button(self, text="Home", font=buttonFont, bg='#A3E4D7', fg='#5F4B8B', borderless=1,
                      activebackground=('#AE0E36', '#D32E5E'), activeforeground='#E69A8D',
                      command=lambda: controller.show_frame(FirstPage))
        home.place(x=10, y=-10, relx=0.0, rely=1.0, anchor=SW)

        PL.PlayLists(self)

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        root = tk.Frame(self)
        root.pack()

        root.grid_rowconfigure(0, minsize=300)
        root.grid_columnconfigure(0, minsize=600)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(root, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Youtube-Playlist-Creator")


app = Application()
app.maxsize(600, 300)
app.mainloop()