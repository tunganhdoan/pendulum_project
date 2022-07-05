from main_frame import *
from main_window import *

if __name__ == '__main__':
    app = App()
    main_frame = MainFrame(app)
    app.mainloop()