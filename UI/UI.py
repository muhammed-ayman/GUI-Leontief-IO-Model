from tkinter import *

# Graphics Info
HEIGHT = 600
WIDTH = 600


root = Tk()
root.title("Leontif Input-Output Analysis")
root.geometry(str(WIDTH)+"x"+str(HEIGHT))

class App:
    def __init__(self, master):
        self.master = master
        AppFrame = Frame(master)
        AppFrame.pack()
        self.main_window()
    
    def main_window(self):
        self.matrix_dim_label1 = Label(self.master, 
                                    text="Enter The IO Matrix Dimension",
                                    font=('Arial', 14))
        self.matrix_dim_label2 = Label(self.master, 
                                    text="N =",
                                    font=('Arial', 14))
        self.matrix_dim_entry = Entry(self.master)
        self.matrix_dim_btn = Button(self.master,
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
        except:
            print("Invalid Dimension")