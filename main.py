#2)funcion PPT
def PPT_juego():
    a = int(input("P1: 1)Piedra, 2)Papel, 3)Tijera\n"))
    b = int(input("P2: 1)Piedra, 2)Papel, 3)Tijera\n"))

    if a == 1 and b == 3:
        print("P1 gana!, Piedra gana Tijera")
    elif a == 2 and b == 1:
        print("P1 gana!, Papel gana Piedra")
    elif a == 3 and b == 2:
        print("P2 gana!, Tijera gana Papel")
    elif a == 1 and b == 3:
        print("P1 Gana!, Piedra gana Tijera")
    elif a == 2 and b == 1:
        print("P1 Gana!, Papel gana Piedra ")
    elif a == 3 and b == 2:
        print("P1 Gana!, Tijera gana Papel ")
    elif a == 3 and b == 1:
        print("P2 Gana!, Piedra gana Tijera")
    elif a == 1 and b == 2:
        print("P2 Gana!, Papel gana Piedra")
    elif a == 2 and b == 3:
        print("P2 Gana!, Tijera gana Papapel")
    else:
        print("Ninguno gana, vualve a intentarlo\n")

#3) Funcion Menu
def Menu():
  print("********************\n Juego de Piedra Papel o Tijera!\n *************************\n")
  opcion = input("Seleccione:\n 1) Iniciar Juego: \n 2) volver a menu:\n ")
  if opcion == "1":PPT_juego()
  elif opcion == "3": "break"


#1) codigo para incializar la app
while True:
  Menu1 = input("a) Iniciar\n b) Salir\n")
  if Menu1 == "a": Menu()
  elif Menu1 == "b": break
  else:
      print("valor invalido, digite a) o b)\n")

