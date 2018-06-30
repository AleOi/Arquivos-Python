MeurPrimeiroDic = {"nome":"Arthur", "comida_preferida":"Abacate", "Estatura":"Baixa"}

# Primeira ideia de dicionario
print(MeurPrimeiroDic["nome"])

#Facilmente conseguimos adicionar um elemento no dicionario
MeurPrimeiroDic[21] = "Ana"
print(MeurPrimeiroDic[21])

#Podemos armazenar funcoes, ou seja, podemos armazenar tudo
MeurPrimeiroDic["funcao"] = (lambda x: x + 1)
print(MeurPrimeiroDic["funcao"](10))

#Podemos printar
for coisa in MeurPrimeiroDic:
  print(coisa)
print(len(MeurPrimeiroDic))

#Alguns métodos para dicionario
MeurPrimeiroDic.get("nome")

#Imprime tuplas values e keys
for i in MeurPrimeiroDic.items():
  print(i)

# Imprime os keys associados aos values
for i in MeurPrimeiroDic.keys():
  print(i)

# Imprime os keys associados aos values
for i in MeurPrimeiroDic.values():
  print(i)


# Outros comandos que existem: copy, clear
#O comando pop retira o key do dicionario e retorna o value retirado
print(MeurPrimeiroDic.pop(21))

#O comando popitem remove o primeiro elemento do dicionario
print(MeurPrimeiroDic.popitem())

#O comando setdefault adiciona um key caso ele não esteja no dicionario
#Perceba que Celular entrou com item none
MeurPrimeiroDic.setdefault("Celular")
print(MeurPrimeiroDic.items())