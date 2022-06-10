from tkinter import *


def main():
    class Window():
        def __init__(self):
            #   Creating main root
            self.root = Tk()
            self.root.title('Root Window')
            self.root.rowconfigure(0, weight=1)
            self.root.columnconfigure(0, weight=1)
            self.root.geometry('600x400+100+100')

            #Useful Vars
            self.seconds = 0
            self.minutes = 0
            self.game_on = None

            #   Creating our pages and configure

            # ==================================== page 1 ====================================#
            #   Home Frame
            self.frame_home = Frame(self.root, background='white')

            #   Buttons
            self.exit_button = Button(self.frame_home, text='Exit', command=self.Close)
            self.exit_button.grid(row=0, column=0, padx=20, pady=30)

            #   Title label
            self.title_label = Label(self.frame_home, text='Typing Speed test', font=('Helvetica', 24, 'bold'))
            self.title_label.grid(row=0, column=1, padx=120, pady=30)

            #   Difficulty options
            self.easy_mode_button = Button(self.frame_home, text='Easy', padx=40)
            self.easy_mode_button.grid(row=1, column=1, padx=20, pady=20)

            self.medium_mode_button = Button(self.frame_home, text='Medium', padx=30)
            self.medium_mode_button.grid(row=2, column=1, padx=20, pady=20)

            self.hard_mode_button = Button(self.frame_home, text='Hard', padx=40)
            self.hard_mode_button.grid(row=3, column=1, padx=20, pady=20)

            #   Start Game button
            self.start_game_button = Button(self.frame_home, text='Start Typing', padx=60
                                            , command=lambda: self.show_frame(self.frame_main))

            self.start_game_button.grid(row=4, column=1, padx=20, pady=40)

            # ==================================== page 2 ====================================#
            # Main Frame
            self.frame_main = Frame(self.root, background='white')

            #   Main Game Buttons
            self.exit_button = Button(self.frame_main, text='Exit', command=self.Close)
            self.exit_button.grid(row=0, column=0, padx=20, pady=30)

            #   clock
            self.clock = Label(self.frame_main, text='00:00', padx=20, font=("helvetica", 48), fg='black', bg='grey')
            self.clock.grid(row=0, column=1, padx=150, pady=30)

            #   Word Box
            self.word_box_border = Frame(self.frame_main, width=60, height=20, highlightbackground="blue",
                                         highlightthickness=2)
            self.word_box_border.grid(row=1, column=1, pady=5)
            self.word_box_label = Label(self.word_box_border, text='', bd=0)
            self.word_box_label.pack()

            # Text Box
            self.text_box = Text(self.frame_main, width=60, height=5, bd=1)
            self.text_box.bind("<Return>", self.return_typed_text)
            self.text_box.grid(row=2, column=1, pady=5)

            #   Buttons
            self.start_typing_button = Button(self.frame_main, text='Start', command=self.start_Game, padx=20)
            self.start_typing_button.grid(row=3, column=1, pady=(10, 5))

            self.reset_button = Button(self.frame_main, text='Reset', command=self.reset_Game, padx=20)
            self.reset_button.grid(row=4, column=1, pady=5)

            self.end_button = Button(self.frame_main, text='Home',
                                     command=lambda: self.back_Home(self.frame_home),
                                     padx=24)
            self.end_button.grid(row=5, column=1, pady=5)

            # ===================================== page 3 ====================================#
            self.frame_score_menu = Frame(self.root, background='grey')

            #   Position Frames
            self.position_frames(self.frame_main, self.frame_home, self.frame_score_menu)
            #   Show Frame on screen
            self.show_frame(self.frame_home)


            #   TKINTER Main loop
            self.root.mainloop()


        def return_typed_text(self, event):
            """
            bind return key
            :param frame:
            :return:
            """
            self.show_frame(self.frame_score_menu)



        def Close(self):
            """
            Closes the root window
            :return:
            """
            self.root.quit()

        def back_Home(self, frame):
            frame.tkraise()
            self.reset_Game()

        def start_Game(self):
            """
            1: Start button in frame main
            will focus the users on the text box
            2: Start timer
            :return:
            """
            self.game_on = True
            self.text_box.focus_set()
            self.timer()

        def reset_Game(self):
            """
            Resets timer
            resets random text
            resets all wpm and accuracy calculations
            resets all current game states
            :return:
            """
            self.game_on = False
            self.reset_timer()

        def timer(self):
            if self.game_on:
                #   Increment clock by one
                self.seconds += 1
                #   Configure clock display
                self.clock.config(text='00:' + str(self.seconds))
                #   Clock display
                if 10 > self.seconds > 0:
                    self.clock.config(text='00:0' + str(self.seconds))
                    self.clock.after(1000, self.timer)
                elif self.seconds == 0:
                    self.clock.config(text='Done')
                else:
                    self.clock.after(1000, self.timer)
            else:
                self.reset_timer()

        def reset_timer(self):
            self.seconds = 0
            self.clock.config(text='00:0' + str(self.seconds))

        def position_frames(self, f1, f2, f3):
            for frame in (f1, f2, f3):
                frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(self, frame):
            frame.tkraise()

    test = Window()


if __name__ == '__main__':
    main()
