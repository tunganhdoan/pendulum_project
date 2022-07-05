from tkinter import Tk

if __name__ == '__main__':
    # how to create an instance "root" that initialize a tkinter gui
    root = Tk()
    # mainloop() method will loop the gui in a predetermined rate
    # The mainloop() keeps the window visible on the screen.
    # If you don’t call the mainloop() method, the window will display and disappear immediately.
    # It will be so fast that you may not see its appearance.
    root.mainloop()
