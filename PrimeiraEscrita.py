#Comandos de arquivos

# Formas read, write and append
arq = open("arquivo1.txt", "w")
arq.write("Segundo arquivo de escrita")
arq.writelines(["\nEsse \n", "e o nosso \n", "Arquivo de escrita \n"])
arq.close()

# Formas read, write and append
arq = open("arquivo1.txt", "r")
# Faz toda a leitura do programa
#print(arq.read())

#Pega cada uma das linhas dos arquivo
for j in arq:
  print(j)
#Pega linha a linha e separa em vetores
#print(arq.readlines()[1])

arq.close()

#Comando seek anda certa quantidade de bytes
#Comando tell mostra onde o cursor está