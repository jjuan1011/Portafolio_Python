

'''
EJERCICIO 11

Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
'''

nombre_usuario = str(input('Bienvenido/a Ingresa tu nombre => '))
print('___________________________________________________')
print('Cuenta de Ahorros No 1029383648202')
print(f'Hola {nombre_usuario} BienvenidE de Nuevo ')
print('___________________________________________________')
print('Cuentanos, ¿Cómo te podemos ayudar?\n Elige alguna de las opciones, escribiendo el número según indique =\n')

# OPCIONES DE USUARIO
print('Para calcular tu interes Anual digita 1 en la barra de opción')
print('Para ver detalles de movimientos digita 2 en la barra de opción')
print('________________________________________________________________')
opcion_usuario = int(input('Elige tu opción => ')) #El usuario debe elegir opcion 1 o 2 o de lo contrario marcará error

balance_cuenta = 85000000
interes_anual = 4  #Interes del 4% anual


if opcion_usuario == 1:
    print('==============================================================')
    print(f'Balance de Cuenta = {balance_cuenta} ')
    print("______________________________________________________________")
    cantidad = int(input("Ingresa la cantidad que deseas invertir al 4 porciento interés compuesto anual MINIMO = 1.000.000 - MAXIMO = 100.000.000 = INGRESA AQUÍ => "))


# En una variable almacenamos la variable en la que el usuario puso el valor a invertir (cantidad) la multiplicamos por (interes_anual) que equivale a 4 y lo dividimos entre 100, así sacamos el interes de dicho año, y como es interes compuesto le sumamos el valor que puso el usuario, despues hacemos el mismo proceso pero como es interes compuesto debemos sumar el resultado final de cada año, al año siguiente y así sisesivamente
    interes_año_1 = cantidad * interes_anual / 100 + cantidad
    print(f'Interés del Primer año => {interes_año_1}')

    interes_año_2 = interes_año_1 * interes_anual / 100 + interes_año_1
    print(f'Interés del Segundo año => {interes_año_2}')

    interes_año_3 = interes_año_2 * interes_anual / 100 + interes_año_2
    print(f'Interés del Tercer año => {interes_año_3}')
    
    interes_año_4 = interes_año_3 * interes_anual / 100 + interes_año_3
    print(f'Interés del Cuarto año => {interes_año_4}')

    interes_año_5 = interes_año_4 * interes_anual / 100 + interes_año_4
    print(f'Interés del Quinto año => {interes_año_5} ')

    print('==============================================================')
elif opcion_usuario == 2:
    print('==============================================================')
    print(f'Balance de Cuenta = {balance_cuenta} ')
    print("______________________________________________________________")
    print('Movimientos')
    print('****************')
    print("Fecha 10/11/22")
    print('Valor = 5.500.000')
    print('Establecmiento de comercio => ZARA')
    print('****************')
    print("Fecha 15/11/22")
    print('Valor = 2.500.000')
    print('Establecmiento de comercio => ADIDAS')
    print('****************')
    print("Fecha 18/11/22")
    print('Valor = 1.200.000')
    print('Establecmiento de comercio => PORNHUB')
    print('****************')
    print("Fecha 25/11/22")
    print('Valor = 3.000.000')
    print('Establecmiento de comercio => ROSARITO')
    print('****************')
    print("Fecha 30/11/22")
    print('Valor = 800.000')
    print('Establecmiento de comercio => ALKOSTO')
    print("______________________________________________________________")
else:
    print('Digita una opción válida entre el 1 y el 2')



# 88400