from tkinter import * 
from tkinter import messagebox

class Interface:
    
    def __init__(self):
        self.root = Tk()
        self.root.title("Estrutura de Dados")
        self.root.minsize(width = 1280, height= 720)
        self.root.config(bg="#fff3e6")
        
        self.mainFrame = Frame(self.root,width = 1020, height= 768, bg="#fff3e6")
        self.mainFrame.pack() #Executa o mainframe

        self.root.mainloop() #Roda o programa

i = Interface()
