
class Phone():
    def __init__(self):
        self.request = ''
        self.request_t = '' 
        self.request_f = ''                             

    
    def choice(self):
        while self.request != 'no':
            print('================= OPTIONS ==================')
            print(' (T). Ir a tiktok\n (F) Ir a Facebook\n (I) Ir a Instagram\n (W) Ir a Watsapp') 
            self.usser_option = str(input('Ingresa la opción de acuerdo a lo que deseas hacer => ')).lower()

            if self.usser_option == 't':
                while self.request_t != 2:
                    print('============= BIENVENIDO A TIKTOK ============')
                    print('Para elegir contenido sexual digita => 1 \n Para elegir contenido infantil digita => 2 \n Para elegir contenido biblico digita => 3 \n para elegir al temach digitA => 4')
                    self.tiktok_option = int(input('iNGRESA EL NÚMERO DE LA OPCIÓN QUE DESEAS >>>'))
                    if self.tiktok_option == 1:
                        print('MALDITO PAJERO')
                    elif self.tiktok_option == 2:
                        print('A TU CASA A VER POCOYÓ')
                    elif self.tiktok_option == 3:
                        print('AMEN PERRASSSSS')
                    elif self.tiktok_option == 4:
                        print('PONGASE MAMADO MI COMPA')
                    else:
                        print('digita una opción válida zorrita')
                    self.request_t = int(input('Para salir ingresa >>> 2 Para volver al menú tiktok ingresa >>> 1'))
            elif self.usser_option == 'f':
                while self.request_f != 2:
                    print('============= BIENVENIDO A TIKTOK ============')
                    print('Para elegir contenido sexual digita => 1 \n Para elegir contenido infantil digita => 2 \n Para elegir contenido biblico digita => 3 \n para elegir al temach digitA => 4')
                    self.tiktok_option = int(input('iNGRESA EL NÚMERO DE LA OPCIÓN QUE DESEAS >>>'))
                    if self.tiktok_option == 1:
                        print('MALDITO PAJERO')
                    elif self.tiktok_option == 2:
                        print('A TU CASA A VER POCOYÓ')
                    elif self.tiktok_option == 3:
                        print('AMEN PERRASSSSS')
                    elif self.tiktok_option == 4:
                        print('PONGASE MAMADO MI COMPA')
                    else:
                        print('digita una opción válida zorrita')
                    self.request_f= input('Para salir ingresa >>> 2 Para volver al menú tiktok ingresa >>> 1')
        
            self.request = input('Para salir ingrese SI, Para volver al menú principal ingrese NO  INGRESE >>> ')


phone = Phone()
phone.choice()
        
