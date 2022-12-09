

'''
EJERCICIO 9

Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión.
'''
convertidor = float(input('Ingresa la cantidad en pesos que será convertida a Dólares => '))
calculado = convertidor / 5000
print(f'Tus pesos equivalen a {calculado} Dólares debes ingresar esta cifra en la siguiente linea')
inversion = float(input('Ingresa la cantidad en Dólares que quieres invertir => '))


print('==========> ELIGE TU PERFIL DE RIESGO <==========\n')
print('======> $$$ ENTRE MÁS ALTO SEA TU PERFIL MÁS GANANCIA POTENCIAL, PERO MÁS PROBABILIDAD DE PERDERLO TODO, ASÍ QUE TEN MUCHO CUIDADO $$$ <======\n')
print('PERFIL ~ CONSERVADOR ~ ofrece un retorno del 3 porciento efectivo anual\n')
print('PERFIL ~ ENTUCIASTA ~ Ofrece un retorno del 5 porciento efectivo anual\n')
print('PERFIL ~ CALCULADOR ~ Ofrece un retorno del 10 porciento efectivo anual\n')
print('PERFIL ~ RIESGOSO ~ Ofrece un retorno del 15 porciento efectivo anual\n')
print('PERFIL ~ CLAVADISTA ~ Ofrece un retorno del 20 porciento efectivo anual\n')
print('PERFIL ~ EXPOSICIÓN TOTAL ~ Ofrece RETORNO del 100 porciento efectivo anual\n')


# calculo 1
conservador = float(input('Para ver cuanto obtendras si eliges el PERFIL ~ CONSERVADOR ~ Ingresa 3 => '))
resultado_conservador = conservador * inversion / 100
print(f'Obtendras {resultado_conservador} Al finalizar un periodo de 365 días')

# calculo 2
entuciasta =  float(input('Para ver cuanto obtendras si eliges el PERFIL ~ ENTUCIASTA ~ Ingresa 5 => '))
resultado_entuciasta = entuciasta * inversion / 100
print(f'Obtendras {resultado_entuciasta} Dólares Al finalizar un periodo de 365 días')

# calculo 3
calculador = float(input('Para ver cuanto obtendras si eliges el PERFIL ~ CALCULADOR ~ Ingresa 10 => '))
resultado_calculador = calculador * inversion / 100
print(f'Obtendras {resultado_calculador} Dólares Al finalizar un periodo de 365 días')

# calculo 4
riesgoso = float(input('Para ver cuanto obtendras si eliges el PERFIL ~ RIESGOSO ~ Ingresa 15 => '))
resultado_riesgoso = riesgoso * inversion / 100
print(f'Obtendras {resultado_riesgoso} Dólares Al finalizar un periodo de 365 días')

# calculo 5
clavadista = float(input('Para ver cuanto obtendras si eliges el PERFIL ~ CLAVADISTA ~ Ingresa 20 => '))
resultado_clavadista = clavadista * inversion / 100
print(f'Obtendras {resultado_clavadista} Dólares Al finalizar un periodo de 365 días')

# calculo 6
exposicion_total = float(input('Para ver cuanto obtendras si eliges el PERFIL ~ EXPOSICIÓN TOTAL ~ Ingresa 100 => '))
resultado_exposicion_total = exposicion_total * inversion / 100
print(f'Obtendras {resultado_exposicion_total} Dólares Al finalizar un periodo de 365 días')





