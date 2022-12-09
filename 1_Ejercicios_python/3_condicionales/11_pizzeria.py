

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
        self.user_search = str(input("Ingresa la opcion de pizza de la cual deseas ver sus ingredientes, RECUERDA hacerlo con el Codigo respectivo a cada pizza => "))
        self.user_repeat =  input("Para ver los ingredientes de otra pizza Ingresa (s), pero si de lo contrario YA deseas elegir tu pizza ya Ingresa (n) =>  ")

        
    def menu(self):
        while self.user_repeat != 's':
            if self.user_search == '01':
                for i in self.vegetariana:
                    print(i)
            elif self.user_search == '02':
                for i in self.peperoni:
                    print(i)
            elif self.user_search == '03':
                for i in self.carne:
                    print(i)
            elif self.user_search == '04':
                for i in self.hawaiana:
                    print(i)
            elif self.user_search == '05':
                for i in self.ranchera:
                    print(i)
            else:
                print('Ingresa una opcion válida')

    
    def eleccion(self):
        self.user_option = str(input("Ingresa la opcion de pizza que quieras comer, RECUERDA hacerlo con el codigo respectivo a cada pizza => "))
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
    
 


pizza = pizzeria()
print(pizza.menu())
print(pizza.eleccion())