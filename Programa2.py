def funcao1():
  '''
    Primeiro Doc string
  '''
  global M, X
  X += X
  def funcao2():
    print(X)
  funcao2()

print("Sou feliz", end = "\t")
X = 800
M = 20

funcao1()

