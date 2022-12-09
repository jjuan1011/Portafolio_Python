

'''
EJERCICIO 11

La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.'''

class pizzeria():
    def __init__(self):
        self.vegetariana = ["- Pimiento", "- tofu", "- lechuga", "- vinagreta"]
        self.peperoni = ["- Peperoni", "- Jamón", "- Salmón y queso"]
        self.carne = ["- Carne Desmechada", "- Salchica y Salchicón", "- Queso con tiras de pollo"]
        self.hawaiana = ["- Piña", "- Extra Queso", "- Jamón ligero"]
        self.ranchera = ["- Huevo", "- Carne desmechada", "- Mazorca"]
        self.nombre = str(input('Ingresa tu nombre => '))

        print(f'========================== {self.nombre} BIENVENIDA/O a Bella Napoli ========================')
        print('El día de hoy te ofrecemos :')
        print('___________________________')
        print(' - Pizza Vegetariana = C0DIGO 01\n - Pizza Peperoni = CODIGO 02\n - Pizza Carne = CODIGO 03\n - pizza hawaiana = CODIGO 04\n - pizza Ranchera = CODIGO 05\n')
        self.user_repeat =  ''

    def menu(self):
        # while self.user_repeat == 's':
        #     self.user_repeat =  input("Para ver los ingredientes de Una pizza Ingresa (s), pero si de lo contrario YA deseas elegir tu pizza Ingresa (n) =>  ")
        #     pass
        # self.user_repeat =  input("Para ver los ingredientes de Una pizza Ingresa (s), pero si de lo contrario YA deseas elegir tu pizza Ingresa (n) =>  ")

        while self.user_repeat != 'n': 

            self.user_search = str(input("Ingresa la opcion de pizza de la cual deseas ver sus ingredientes, RECUERDA hacerlo con el Codigo respectivo a cada pizza => "))

            if self.user_search == '01':
                print('==> PIZZA VEGETARIANA <==')
                for i in self.vegetariana:
                    print(i)
            elif self.user_search == '02':
                print('==> PIZZA PEPERONI <==')
                for i in self.peperoni:
                    print(i)
            elif self.user_search == '03':
                print('==> PIZZA DE CARNES <==')
                for i in self.carne:
                    print(i)
            elif self.user_search == '04':
                print('==> PIZZA HAWAIANA <==')
                for i in self.hawaiana:
                    print(i)
            elif self.user_search == '05':
                print('==> PIZZA RANCHERA <== ')
                for i in self.ranchera:
                    print(i)
            else:
                print('Ingresa una opcion válida')
            self.user_repeat =  input("Para ver los ingredientes de Una pizza Ingresa (s), pero si de lo contrario YA deseas elegir tu pizza Ingresa (n) =>  ")
            
        self.user_option = str(input("Ingresa la opcion de pizza que quieras comer, RECUERDA hacerlo con el codigo respectivo a cada pizza => "))

    
    def eleccion(self):

        if self.user_option == '01':
            print('¡ Elegiste una Deliciosa Pizza Vegetariana ! ♥ DISFRUTALA MUCHO ♥')
        elif self.user_option == '02':
            print('¡ Elegiste una Deliciosa Pizza de Peperoni ! ♥ DISFRUTALA MUCHO ♥')
        elif self.user_option == '03':
            print('¡ Elegiste una Deliciosa Pizza de Carne ! ♥ DISFRUTALA MUCHO ♥')
        elif self.user_option == '04':
            print('¡ Elegiste una Deliciosa Pizza Hawaiana ! ♥ DISFRUTALA MUCHO ♥')
        elif self.user_option == '05':
            print('¡ Elegiste una Deliciosa Pizza Ranchera ! ♥ DISFRUTALA MUCHO ♥')
        else:
            print('Ingresa una opción válida')
    
 







pizza = pizzeria()
print(pizza.menu())
print(pizza.eleccion())

#Mientras lo que digite el usuario sea diferente de n, elciclo se repetirá, operando las mismas sentencias dentro del ciclo, cuando el usuario ingrese n y unicamente n, el ciclo se detiene y ejecuta la sentencia afuera del ciclo, que sería el self.user_option, que es usado en la siguiente función para otro proceso.