from tkinter import *

class Application:

    def __init__(self, master=None):
        self.master = master
        self.mainContainer = Frame(master, padx=10)
        self.title = Label(master, text="Menu", bg="white")
        self.title["font"] = ("Verdana", "12", "bold")
        self.title.pack(pady=10)
        self.mainContainer.pack(pady=20)
        self.homeView()
        
    def homeView(self):
        self.listButton = Button(self.mainContainer, width=15, text="Lista Encadeada", bg="midnight blue", fg="white")
        self.stackButton = Button(self.mainContainer, width=15, text="Pilha", bg="midnight blue", fg="white")
        self.queueButton = Button(self.mainContainer, width=15, text="Fila", bg="midnight blue", fg="white")
        self.binaryTreeButton = Button(self.mainContainer, width=15, text="Árvore Binária", bg="midnight blue", fg="white")
        self.graphButton = Button(self.mainContainer, width=15, text="Grafo", bg="midnight blue", fg="white")
        self.exitButton = Button(self.mainContainer, width=15, text="Sair", command=self.master.quit, bg="midnight blue", fg="white")

        self.listButton.pack(pady=10) 
        self.stackButton.pack(pady=10)
        self.queueButton.pack(pady=10)
        self.binaryTreeButton.pack(pady=10)
        self.graphButton.pack(pady=10)
        self.exitButton.pack(pady=10)




root = Tk()
root["bg"] = "white" #bg=background

#Width x Height + Left + Top
#root.geometry("500x500")#tamanho e posição da tela

Application(root)
root.mainloop()