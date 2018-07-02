#Bibliotecas para jogos
#Calculadora para estatística

from tkinter import *

#Notar que essas coisas sao dicionarios
def Calcular():
  texto["text"] = ent.get()
  texto["fg"] = "green"

#Inicializacao
i = Tk()
# Tamanho da janela
i.geometry("400x300")
#Titulo
i.title("Calculadora para Estatisitca")
#icone
#i.wm_iconbitmap("icone.ico")

fonte = ('Verdana', '25', 'bold')
# RGB to hexadecimal
#bg = A3FF..
AZUL = "#91B4FF"

i["bg"] = AZUL

# Frames
Janela1 = Frame(i, bg = "blue") #Frame com check
Janela2 = Frame(i, bg = "green") # Frame de texto
Janela3 = Frame(i, bg = "black", pady = 100) #Frame com calcular
Janela4 = Frame(i) #Frame com formulas
Janela5 = Frame(i) #Frame com botoes especificos

#Empacotando as frames
Janela1.pack()
Janela2.pack()
Janela3.pack()
Janela4.pack()
Janela5.pack()

#Colocando Label
texto = Label(Janela1, text = "Resultado", bg = "red", fg = "blue", font = fonte)
texto.pack()

#Colocando entry (caixa de texto)
ent = Entry(Janela2)
ent.pack()

#Colocando botao
#b = Button(Janela3, text = "Calcular", command = Calcular)
#b.pack()

botao = ("Primeiro Botao", "Segundo Botao", "Terceiro Botao")
'''
indice = 1
for b in botao:
  if indice % 4 == 0:
    a = Button(Janela3, text = b, bg = "green")
    a.pack()
  else:
    a = Button(Janela3, text = b, bg = "green")
    a.pack(side = LEFT)
    indice += 1
'''

for b in botao:
    a = Button(Janela3, text = b, bg = "green")
    a.pack()

#Abre uma janela
i.mainloop()
