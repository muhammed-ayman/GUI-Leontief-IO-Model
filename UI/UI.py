from tkinter import *

# Graphics Info
HEIGHT = 600
WIDTH = 600

# Tkinter Info
root = Tk()
root.title("Leontif Input-Output Analysis")
root.geometry("{0}x{1}".format(WIDTH, HEIGHT))

class App:
    def __init__(self, master):
        self.master = master
        self.AppFrame = Frame(self.master, width=WIDTH, height=HEIGHT)
        self.AppFrame.pack()
        self.main_window()
    
    def main_window(self):
        self.matrix_dim_label1 = Label(self.AppFrame, 
                                    text="Enter The IO Matrix Dimension",
                                    font=('Arial', 14))
        self.matrix_dim_label2 = Label(self.AppFrame, 
                                    text="N =",
                                    font=('Arial', 14))
        self.matrix_dim_entry = Entry(self.AppFrame)
        self.matrix_dim_btn = Button(self.AppFrame,
                                    text="Proceed",
                                    command=self.proceedToAnalysisWindow)

        self.matrix_dim_entry.place(x=(HEIGHT/2)-50, y = (WIDTH/2)-50, width=100, height=30)
        self.matrix_dim_label1.place(x=150,
                                    y=200)
        self.matrix_dim_label2.place(x=(HEIGHT/2)-100,
                                    y = (WIDTH/2)-50)
        self.matrix_dim_btn.place(x=(HEIGHT/2)-50,
                                y = (WIDTH/2),
                                height=30,
                                width=100)
    
    def proceedToAnalysisWindow(self):
        try:
            matrix_dim = int(self.matrix_dim_entry.get())
            print("Valid Matrix Dimension")
            self.clearFrame()
        except:
            print("Invalid Dimension")
    
    def clearFrame(self):
        for widget in self.AppFrame.winfo_children():
            widget.destroy()
        self.AppFrame.pack_forget()