

'''
Crea un programa que permita hacer la busqueda en una "Base de datos", o diccionario como la interfaz de  un banco que permita hacer varias cosas al usuario, como buscar sus datos mirar los mismos, mirar reportes en centrales, antecedentes, certificados pension y eps, mirar la opción de si puede adquirir un crédito, acomodar las cuotas.
'''

class Bank():
    def __init__(self):
        self.data_dictionary = {'1001049220':{'Nombre':'Juan David Meneses',        'Edad':20,          'Reportes': '3 Reportes positivos en centrales de riesgo'},
        '1001341591':{'Nombre':'Felipe Meneses', 'Edad':22, 'Reportes': '3 Reportes Negativos en centrales de riesgo'}, '52970170':{'Nombre':'Samuel Meneses', 'Edad':15, 'Reportes': '1 Reporte positivo en central de riesgo'}}
        self.user_antecedentes = {'1001049220':'El usuario tiene antecedentes penales, por hurto, en dos ocasiones', '1001078620':'El usuario tiene antecedentes penales, por hurto, en dos ocasiones', '1001023220':'El usuario tiene antecedentes penales, por hurto, en dos ocasiones' }
        self.request = ''
        self.request_2 = ''
    

    def sistem(self):
        while self.request != 'si':
            print('======================== BIENVENIDO A BANCO BBVA =====================')
            print('- Para consultar un usuario ingrese => C\n' '- Para consultar antecedentes ingrese => A \n' '- Para consultar certificados ingrese => F \n' '- Para adquirir un crédito ingrese = E')
            self.user_option = input('Ingrese la opción que desea => ').lower()

            if self.user_option == 'c':
                self.consult_user = input('Igrese el # de cedula del usuario => ').lower()
                print(self.data_dictionary.get(self.consult_user, 'El usuario No se encuentra registrado ;( '))
            elif self.user_option == 'a':
                self.user_ced = input('Ingrese la cedula del usuario que desea consltar => ')
                for i in self.user_antecedentes:
                    if i in self.user_antecedentes:
                        print(self.user_antecedentes[i])
            
            elif self.user_option == 'f':
                print('Mira tu certificado perra .|.')
            
            elif self.user_option == 'e':
                self.dictionary_score = {1001049220:220, 1001341591:524,5874668:120}
                self.type_ced = int(input('Ingrese el número de cedula a consultar => '))
                print(self.dictionary_score.get(self.type_ced, 'El usuario no se encuentra registrado'))
                self.type_score = int(input('Ingrese score => '))
                if self.type_score <= 200:
                    print('Tu puntaje NO es suficiente para adquirir un crédito')
                else:
                    print('Puedes adquirir un credito con la entidad financiera')
                    while self.request_2 != 2:
                        self.user_deb = int(input('Para continuar con el proceso digite 1, para salir ingrese 2  INGRESE => '))
                        if self.user_deb == 1:
                            print('Cupo disponible por maximo 45.000.000')
                            self.take = str(input('Para tomar el crédito ingrese Si, de lo contrario ingrese No, INGRESE => ')).lower()
                            if self.take == 'si':
                                print('Felicitaciones en 24 horas le desembolsamos su dinero')
                            else:
                                print('Su puntaje a bajado 10 puntos por no aceptar el crédito')
                        self.request_2 = int(input('Si desea recuperar sus puntos y adquirir el credito ingrese 1, si adquirió el credito ignore el mensaje e ingrese = 2   INGRESE => '))
            
            self.request = input('Si desea salir igrese = si, para hacEr otro proceso ingreses no ="  INGRESE SU OPCIÓN => ').lower()


            
result_ = Bank()
result_.sistem()