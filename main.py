from tkinter import *


def main():
    class Window():
        def __init__(self):

            self.root = Tk()
            self.root.title('Root Window')
            self.root.rowconfigure(0, weight=1)
            self.root.columnconfigure(0, weight=1)
            self.root.geometry('600x500')

            #   Creating our pages and configure
            self.frame_home = Frame(self.root, background='blue')
            self.frame_main = Frame(self.root, background='grey')
            self.frame_score_menu = Frame(self.root, background='white')

            #   Position Frames
            self.position_frames(self.frame_main, self.frame_home, self.frame_score_menu)
            #   Show Frame on screen
            self.show_frame(self.frame_home)



            #   TKINTER Main loop
            self.root.mainloop()




        def position_frames(self, f1, f2, f3):
            for frame in (f1, f2, f3):
                frame.grid(row=0, column=0, sticky='nsew')


        def show_frame(self, frame):
            frame.tkraise()









    test = Window()


if __name__ == '__main__':
    main()
