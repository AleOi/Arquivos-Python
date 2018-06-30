class Animal():
  def __init__(self, tipo, raca):
    self.tipo = tipo
    self.raca = raca
  def get_raca(self):
    print(self.raca)

  def falar(self):
    print("haha")

class Cachorro(Animal):
  def __init__(self, raca, nome, idade):
    self.raca = raca
    self.nome = nome
    self.idade = idade

  def get_raca(self):
    print(self.raca)
    super().falar()

  def get_nome(self):
    print(self.nome)

  def get_idade(self):
    print(self.idade)

#Amanda = Cachorro("Poodle", "Amanda", 12)
#Lira = Animal("Animal","Borboleta")
#Lira.get_raca()
#Amanda.get_idade()


