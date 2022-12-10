

'''
Ejercicio 10
Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIT, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
Preguntar por el NIF del cliente y mostrar sus datos.
Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
Terminar el programa.
'''

class Base_Datos():
    def __init__(self):
        self.dictionary_client = {}
        self.menu = ''
    
    def program(self):
        while self.menu != 't':
            self.menu = input(' Para añadir un cliente ingrese => (A)\n Para Eliminar un cliente ingrese => (E)\n Para mostrar un cliente ingrese => (M)\n Para listar todos los clientes ingrese => (L)\n Para listar clientes preferentes ingrese => (P)\n Para terminar ingrese => (T)\n ======================= INGRESE OPCIÓN =>>> ').lower()
            if self.menu == 'a':
                self.cc_client = str(input('Ingrese la CC del cliente => '))
                self.info_client = input('Ingrese, nombre, dirección, teléfono, correo,preferente en este mismo orden seguido de comas =>').lower() 
                self.dictionary_client[self.cc_client] = self.info_client

            elif self.menu == 'e':
                self.delete_client = str(input('Ingrese la CC del cliente que desea eliminar => '))
                self.delete = self.dictionary_client.pop(self.delete_client)
                print('Se eliminó el cliente =>'+ self.delete)
                if not self.delete_client in self.dictionary_client:
                    print('El usuario NO se encuentra en nuestra base de datos')
                else:
                    print('El usuario se eliminó con satisfacción')
            elif self.menu == 'm':
                self.show_client = input('Ingrese el cliente que desea mostrar => ').lower()
                for i in self.dictionary_client:
                    if i in self.show_client:
                        print('El cliente registrado es => ' + self.dictionary_client[i])
                    else:
                        print('El cliente no se encuentra registrado')
            elif self.menu == 'l':
                for i in self.dictionary_client:
                    if i in self.show_client:
                        print('Base de datos => ' + i)
            # elif self.menu == 'p':
            #     # Clientes preferenciales

        print('¡ Sliste del programa !')




base_datos = Base_Datos()
base_datos.program()