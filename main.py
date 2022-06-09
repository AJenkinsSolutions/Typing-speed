from tkinter import *


def main():
    class Window():
        def __init__(self):
            self.root = Tk()
            self.root.geometry('600x500')
            self.root.title('Root Window')




            self.root.mainloop()

    test = Window()


if __name__ == '__main__':
    main()
