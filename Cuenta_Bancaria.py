from IPython.core.display import clear_output # Limpia la consola

class Persona():

  def __init__(self,nombre:str,apellido:str) -> None:

    self.nombre = nombre
    self.apellido = apellido


class Cliente(Persona):

  def __init__(self,nombre:str,apellido:str,cuenta:str,balance:float) -> None:

    super().__init__(nombre,apellido)
    self.__cuenta = cuenta
    self.__balance = balance

  def __str__(self) -> str:

    return f'\nNombre: {self.nombre}\nApellido: {self.apellido}\nNumero de cuenta: {self.__cuenta}\nSaldo: {self.__balance}'

  def __imprimir_saldo(self) -> None:

    print(f'\nSaldo actual:{self.__balance}')

  def depositar(self,deposito:float) -> None:

    self.__balance += deposito
    self.__imprimir_saldo()

    print('\nDeposito exitoso.')

  def retirar(self,retiro:float) -> None:

    if self.__balance >= retiro:

      self.__balance -= retiro
      self.__imprimir_saldo()

      print('\nRetiro exitoso.')

    else:

      print('El monto pedido supera el saldo actual')

def crear_cliente() -> Cliente:

  nombre = input('Nombre del cliente:\n')
  apellido = input('\nApellido del cliente:\n')
  cuenta = input('\nCuenta del cliente:\n')
  balance = float(input('\nMonto inicial:\n'))
  clear_output()
  return Cliente(nombre,apellido,cuenta,balance)

def inicio() -> None:

  print('Bienvenido a Banca-Rota su banco amigo.\n\nLlego el momento de crear un nuevo cliente.\n')
  cliente = crear_cliente()

  print('\nCliente creado\n')
  print(cliente)

  while True:
    opcion_elegida = input(f'{"-"*60}\nQue desea hacer ?\n\n[1]: para realizar un deposito\n[2]: para realizar un retiro\n[3]: para salir del programa.\n\n')

    if opcion_elegida == '1':
      clear_output()
      cliente.depositar(float(input('\nIngrese el monto a depositar:\n')))

    elif opcion_elegida == '2':
      clear_output()
      cliente.retirar(float(input('\nIngrese el monto a retirar:\n')))

    elif opcion_elegida == '3':
      clear_output()
      print('Gracias por utlizar Banca-Rota su banco amigo')
      break

inicio()