import tkinter as tk
import tkinter.font as tkFont

# https://visualtk.com/
class App:
    def __init__(self, root):
        # setting title
        root.title("undefined")
        # setting window size
        width = 600
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_680 = tk.Label(root)
        ft = tkFont.Font(family='Times', size=10)
        GLabel_680["font"] = ft
        GLabel_680["fg"] = "#333333"
        GLabel_680["justify"] = "center"
        GLabel_680["text"] = "label"
        GLabel_680.place(x=50, y=60, width=70, height=25)

        GButton_948 = tk.Button(root)
        GButton_948["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times', size=10)
        GButton_948["font"] = ft
        GButton_948["fg"] = "#000000"
        GButton_948["justify"] = "center"
        GButton_948["text"] = "Wcisnij mnie"
        GButton_948.place(x=220, y=50, width=234, height=35)
        GButton_948["command"] = self.GButton_948_command

        GCheckBox_799 = tk.Checkbutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GCheckBox_799["font"] = ft
        GCheckBox_799["fg"] = "#333333"
        GCheckBox_799["justify"] = "center"
        GCheckBox_799["text"] = "CheckBox"
        GCheckBox_799.place(x=50, y=130, width=70, height=25)
        GCheckBox_799["offvalue"] = "0"
        GCheckBox_799["onvalue"] = "1"
        GCheckBox_799["command"] = self.GCheckBox_799_command

        GRadio_784 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_784["font"] = ft
        GRadio_784["fg"] = "#333333"
        GRadio_784["justify"] = "center"
        GRadio_784["text"] = "RadioButton"
        GRadio_784.place(x=370, y=110, width=85, height=25)
        GRadio_784["command"] = self.GRadio_784_command

        GLineEdit_707 = tk.Entry(root)
        GLineEdit_707["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GLineEdit_707["font"] = ft
        GLineEdit_707["fg"] = "#333333"
        GLineEdit_707["justify"] = "center"
        GLineEdit_707["text"] = "Entry"
        GLineEdit_707.place(x=400, y=210, width=70, height=25)

        GListBox_758 = tk.Listbox(root)
        GListBox_758["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        GListBox_758["font"] = ft
        GListBox_758["fg"] = "#333333"
        GListBox_758["justify"] = "center"
        GListBox_758.place(x=150, y=240, width=80, height=25)

        GMessage_871 = tk.Message(root)
        ft = tkFont.Font(family='Times', size=10)
        GMessage_871["font"] = ft
        GMessage_871["fg"] = "#333333"
        GMessage_871["justify"] = "center"
        GMessage_871["text"] = "Message"
        GMessage_871.place(x=330, y=340, width=80, height=25)

    def GButton_948_command(self):
        print("command")

    def GCheckBox_799_command(self):
        print("command")

    def GRadio_784_command(self):
        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
