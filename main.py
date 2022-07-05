import main_frame as mf
import main_window as mw

if __name__ == '__main__':
    app = mw.App()
    main_frame = mf.MainFrame(app)
    app.mainloop()
