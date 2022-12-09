

'''
Ejercicio 8

En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.
'''

class Evaloacion():
    def __init__(self):
        print('============================  Bienvenido a Genesis Best Worker ===============================')
        self.resultado_trabajador = float(input('Ingrese la puntuación del Worker => '))
        self.salario = float(input('             Ingresa tu salario Mensual => '))
        self.calculo = self.salario * self.resultado_trabajador
    
    def puntuacion(self):
        if self.resultado_trabajador == 0.0:
            print('____________________________________________________________________')
            print('Tus resultados son insufucientes, No le sirves a esta compañía Puto, serás despedido el otro mes si sigues así ') 
        elif self.resultado_trabajador >= 0.1 and self.resultado_trabajador <= 0.4:
            print('____________________________________________________________________')
            print(f'Tus resultados son ACEPTABLES Tendrás un aumento de sueldo de {self.calculo} Pesos, Gracias Por tu dedicación, esperamos que subas a la categoría de MERITORIO, Suerte........')
        elif self.resultado_trabajador >= 0.6:
            print('____________________________________________________________________')
            print(f'Tus resultados son MERITORIOS Tendrás un aumento de sueldo de {self.calculo} Pesos, gracias por hacer parte de esta compañía y crecer junto con ella, sigue así...............')


# class Meritorio(Evaloacion):
#     def meritocracia(self):
#         # super().__init__(self)
#         # self.resultado_trabajador >= 0.10
#         # self.salario >= 10000000
#         self.resultado_trabajador = float(input('Ingrese la puntuación del Worker => '))
#         if self.resultado_trabajador >= 0.90:
#             print('Eres increíble Bro !!!!')
#         else:
#             print('Dale más esfuerzo Bro ;(')

# Crear objeto y llamar al metodo dentro de la clase que queremos usar
evaloar = Evaloacion()
print(evaloar.puntuacion())

# el_merito = Meritorio()
# print(el_merito.meritocracia())
