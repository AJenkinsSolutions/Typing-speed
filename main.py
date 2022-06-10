from tkinter import *


def main():
    class Window():
        def __init__(self):

            #   Creating main root
            self.root = Tk()
            self.root.title('Root Window')
            self.root.rowconfigure(0, weight=1)
            self.root.columnconfigure(0, weight=1)
            self.root.geometry('600x500+100+100')

            #   Creating our pages and configure

            #   Home Frame
            self.frame_home = Frame(self.root, background='white')

            #   Buttons
            self.exit_button = Button(self.frame_home, text='Exit')
            self.exit_button.grid(row=0, column=0, padx=20, pady=20)

            #   Title label
            self.title_label = Label(self.frame_home, text='Typing Speed test', font=('Helvetica', 24, 'bold'))
            self.title_label.grid(row=0, column=1, padx=120, pady=20)










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
