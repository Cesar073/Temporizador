from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QMainWindow, QMessageBox
import sys
import threading
import time

import source.mdb as mdb

'''
HACER:
    Tengo que modificar la base de datos con los siguientes datos: 
        - Día de incio de la Actividad
        - Tiempo acumulado hasta el momento
        - Tener a mano un valor con la situación actual del día, la semana y el mes
    Lo que sucede es que si por ejemplo en el día de hoy ya estoy superando las horas que me corresponden a un día, lo que hace el sistema es reiniciar el contador. Pero el 
    problema es que lo reinicia siempre aunque quizás yo esté recuperando horas perdidas del día anterior. Entonces eso está mal, debería marcarme que yo sigo suamando tiempo 
    pero en realidad no estoy al día con lo que corresponda. O por ejemplo, que estoy acumulando horas para la semana que viene.
    La cuestión es que para saber todo eso necesito primero tener el día de inicio de la actividad, luego determinar cuántos días tuve que haber trabajado hasta el momento, y 
    controlar si la cantidad de tiempo trabajado corresponde a lo que voy hasta el momento. De lo contrario, yo no puedo saber si estoy recuperando horas perdidas de días 
    anteriores o si estoy acumulando horas para días posteriores.

    Una vez corregido eso, debería controlar si necesito otro hilo o no al momento de guardar los datos cada un minuto porque los relojes se me están deteniendo
    










    Eliminar las líneas que tengan éste comentario:
    ***Eliminar



    def enterEvent(self, event):
        self.ui.pushButton.setText("hola ganso")
'''

# VENTANA PRINCIPAL: MENÚ
from source.ppal import Ui_MainWindow

class V_Ppal(QMainWindow):
    def __init__(self):
        super(V_Ppal, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Contador para que cada un minuto se guarden los datos acumulados en la db, para evitar que un apagón haga perder todos los datos obtenidos.
        # Ver función: "Reloj()"
        self.CONTADOR = 0

        # Indica si el reloj está corriendo o apagado
        self.EST_RELOJ = False

        # Variable que indica la hora en que se inició el contador. Al mismo tiempo la uso para saber si tal temporizador está o no encendido
        self.INICIO_1 = 0
        self.INICIO_2 = 0
        self.INICIO_3 = 0
        self.INICIO_4 = 0
        self.INICIO_5 = 0
        self.INICIO_6 = 0
        self.INICIO_7 = 0
        self.INICIO_8 = 0
        self.INICIO_9 = 0
        self.INICIO_10 = 0

        # Variables que acumulan todos los tiempos de cada uno de los temporizadores. Al inicio del programa se cargan con lo acumulado en la base de datos, y luego que un
        # temporizador está encendido, al ser detenido ese tiempo nuevo que se ha acumulado se suma a ésta variable y luego se lo utiliza para actualizar el acumulado en la base
        # de datos.
        # Debido a que si en plena ejecución el PC se apaga, se perderían los datos, entonces lo que hacemos es en otro temporizador actualizar la base de datos cada 1 minuto.
        self.ACUM_1 = mdb.Dev_Tiempo_Acum_Dia(1)
        self.ACUM_2 = mdb.Dev_Tiempo_Acum_Dia(2)
        self.ACUM_3 = mdb.Dev_Tiempo_Acum_Dia(3)
        self.ACUM_4 = mdb.Dev_Tiempo_Acum_Dia(4)
        self.ACUM_5 = mdb.Dev_Tiempo_Acum_Dia(5)
        self.ACUM_6 = mdb.Dev_Tiempo_Acum_Dia(6)
        self.ACUM_7 = mdb.Dev_Tiempo_Acum_Dia(7)
        self.ACUM_8 = mdb.Dev_Tiempo_Acum_Dia(8)
        self.ACUM_9 = mdb.Dev_Tiempo_Acum_Dia(9)
        self.ACUM_10 = mdb.Dev_Tiempo_Acum_Dia(10)

        self.METODO = 0
        self.METODO = 0
        self.METODO = 0
        self.METODO = 0
        self.METODO = 0
        self.METODO = 0
        self.METODO = 0
        self.METODO = 0
        self.METODO = 0
        self.METODO = 0
        self.METODO = 0

        # Actualizamos el valor que tienen acumulado todos los temporizadores
        #cant = self.Actualiza_Temporizadores()

        # Conectamos los botones con sus funciones
        self.ui.push_Act_1.clicked.connect(lambda: self.Btn_Actividad(1))
        self.ui.push_Act_2.clicked.connect(lambda: self.Btn_Actividad(2))
        self.ui.push_Act_3.clicked.connect(lambda: self.Btn_Actividad(3))
        self.ui.push_Act_4.clicked.connect(lambda: self.Btn_Actividad(4))
        self.ui.push_Act_5.clicked.connect(lambda: self.Btn_Actividad(5))
        self.ui.push_Act_6.clicked.connect(lambda: self.Btn_Actividad(6))
        self.ui.push_Act_7.clicked.connect(lambda: self.Btn_Actividad(7))
        self.ui.push_Act_8.clicked.connect(lambda: self.Btn_Actividad(8))
        self.ui.push_Act_9.clicked.connect(lambda: self.Btn_Actividad(9))
        self.ui.push_Act_10.clicked.connect(lambda: self.Btn_Actividad(10))

    '''
    def Actualiza_Temporizadores(self):
        cantidad = source.mdb.Dev_Cant_Activos()
        #ejeX
        self.setGeometry .setMaximumSize(QSize(1094, 1000))
        return cantidad
    
    # Obtiene y devuelve la posición actual de la ventana
    def moveEvent(self, Event):
        ejeX = Event.pos().x()
        ejeY = Event.pos().y()
        return ejeX, ejeY
    '''
    # Carga los cambios en las actividades. Tener en cuenta que pueden ejecutarse una o más actividades al mismo tiempo
    def Btn_Actividad(self, Nro):
        if Nro == 1:
            if self.INICIO_1 > 0:
                self.Guardar_Finalizacion(1)
                self.INICIO_1 = 0
            else:
                self.INICIO_1 = int(time.time())
        if Nro == 2:
            if self.INICIO_2 > 0:
                self.Guardar_Finalizacion(2)
                self.INICIO_2 = 0
            else:
                self.INICIO_2 = int(time.time())
        if Nro == 3:
            if self.INICIO_3 > 0:
                self.Guardar_Finalizacion(3)
                self.INICIO_3 = 0
            else:
                self.INICIO_3 = int(time.time())
        if Nro == 4:
            if self.INICIO_4 > 0:
                self.Guardar_Finalizacion(4)
                self.INICIO_4 = 0
            else:
                self.INICIO_4 = int(time.time())
        if Nro == 5:
            if self.INICIO_5 > 0:
                self.Guardar_Finalizacion(5)
                self.INICIO_5 = 0
            else:
                self.INICIO_5 = int(time.time())
        if Nro == 6:
            if self.INICIO_6 > 0:
                self.Guardar_Finalizacion(6)
                self.INICIO_6 = 0
            else:
                self.INICIO_6 = int(time.time())
        if Nro == 7:
            if self.INICIO_7 > 0:
                self.Guardar_Finalizacion(7)
                self.INICIO_7 = 0
            else:
                self.INICIO_7 = int(time.time())
        if Nro == 8:
            if self.INICIO_8 > 0:
                self.Guardar_Finalizacion(8)
                self.INICIO_8 = 0
            else:
                self.INICIO_8 = int(time.time())
        if Nro == 9:
            if self.INICIO_9 > 0:
                self.Guardar_Finalizacion(9)
                self.INICIO_9 = 0
            else:
                self.INICIO_9 = int(time.time())
        if Nro == 10:
            if self.INICIO_10 > 0:
                self.Guardar_Finalizacion(10)
                self.INICIO_10 = 0
            else:
                self.INICIO_10 = int(time.time())
        # Sólo vamos a llamar a la función  el Reloj en caso de que esté apagado, de lo contrario estaríamos iniciando otro bucle con threading. Tener en cuenta que dentro de
        # esa función se fija si debe permanecer encendido el timer o no, desde aquí sólo la llamamos en el único caso en que esté apagado.
        if self.EST_RELOJ == False:
            self.Reloj()

    # Es el inicio del contador. Se llama por única vez, luego es recursivo siempre y cuando hayan valores que sumar, de eso se encarga él mismo de saber si debe continuar
    def Reloj(self):
        if self.Comprueba_Reloj():
            self.EST_RELOJ = True
            self.Calcula_Reloj()

            # Cada ciclo es de medio segundo, entonces, cada 120 ciclos (1 minuto) ejecutamos la función que va a guardar los datos obtenidos hasta el momento y reiniciamos el
            # contador
            self.CONTADOR += 1
            if self.CONTADOR == 120:
                self.CONTADOR = 0
                self.Guardar_Progreso()

            # Línea que deberá ser eliminada en algún momento, por ahora es un mostrardor de que el reloj está funcionando correctamente (***Eliminar)
            print(self.CONTADOR)
            print(self.INICIO_1)
            print()

            # Volvemos a llamar a ésta misma función ya que se encarga de saber si seguimos utilizando hilos o no
            threading.Timer(0.5, self.Reloj).start()
        else:
            self.EST_RELOJ = False

    # Devuelve True si el reloj está activo, False si hay que pararlo
    def Comprueba_Reloj(self):
        if self.INICIO_1 > 0:
            return True
        elif self.INICIO_2 > 0:
            return True
        elif self.INICIO_3 > 0:
            return True
        elif self.INICIO_4 > 0:
            return True
        elif self.INICIO_5 > 0:
            return True
        elif self.INICIO_6 > 0:
            return True
        elif self.INICIO_7 > 0:
            return True
        elif self.INICIO_8 > 0:
            return True
        elif self.INICIO_9 > 0:
            return True
        elif self.INICIO_10 > 0:
            return True
        else:
            return False

    # Calcula el tiempo que lleva cada temporizador y lo muestra en pantalla
    def Calcula_Reloj(self):
        tiempo = int(time.time())
        if self.INICIO_1 > 0:
            Resultado = (tiempo - self.INICIO_1) + self.ACUM_1
            self.ui.label_tiempo_1.setText(self.Dev_string_tiempo(Resultado))
        if self.INICIO_2 > 0:
            Resultado = (tiempo - self.INICIO_2) + self.ACUM_2
            self.ui.label_tiempo_2.setText(self.Dev_string_tiempo(Resultado))
        if self.INICIO_3 > 0:
            Resultado = (tiempo - self.INICIO_3) + self.ACUM_3
            self.ui.label_tiempo_3.setText(self.Dev_string_tiempo(Resultado))
        if self.INICIO_4 > 0:
            Resultado = (tiempo - self.INICIO_4) + self.ACUM_4
            self.ui.label_tiempo_4.setText(self.Dev_string_tiempo(Resultado))
        if self.INICIO_5 > 0:
            Resultado = (tiempo - self.INICIO_5) + self.ACUM_5
            self.ui.label_tiempo_5.setText(self.Dev_string_tiempo(Resultado))
        if self.INICIO_6 > 0:
            Resultado = (tiempo - self.INICIO_6) + self.ACUM_6
            self.ui.label_tiempo_6.setText(self.Dev_string_tiempo(Resultado))
        if self.INICIO_7 > 0:
            Resultado = (tiempo - self.INICIO_7) + self.ACUM_7
            self.ui.label_tiempo_7.setText(self.Dev_string_tiempo(Resultado))
        if self.INICIO_8 > 0:
            Resultado = (tiempo - self.INICIO_8) + self.ACUM_8
            self.ui.label_tiempo_8.setText(self.Dev_string_tiempo(Resultado))
        if self.INICIO_9 > 0:
            Resultado = (tiempo - self.INICIO_9) + self.ACUM_9
            self.ui.label_tiempo_9.setText(self.Dev_string_tiempo(Resultado))
        if self.INICIO_10 > 0:
            Resultado = (tiempo - self.INICIO_10) + self.ACUM_10
            self.ui.label_tiempo_10.setText(self.Dev_string_tiempo(Resultado))

    # Guarda el acumulado en la base de datos. A ésta función se la llama cada vez se pausa el tiempo en una actividad.
    def Guardar_Finalizacion(self, Nro):
        nuevo = int(time.time())
        if Nro == 1:
            auxiliar = nuevo - self.INICIO_1
            mdb.Act_Tiempos(1,auxiliar)
        if Nro == 2:
            auxiliar = nuevo - self.INICIO_2
            mdb.Act_Tiempos(2,auxiliar)
        if Nro == 3:
            auxiliar = nuevo - self.INICIO_3
            mdb.Act_Tiempos(3,auxiliar)
        if Nro == 4:
            auxiliar = nuevo - self.INICIO_4
            mdb.Act_Tiempos(4,auxiliar)
        if Nro == 5:
            auxiliar = nuevo - self.INICIO_5
            mdb.Act_Tiempos(5,auxiliar)
        if Nro == 6:
            auxiliar = nuevo - self.INICIO_6
            mdb.Act_Tiempos(6,auxiliar)
        if Nro == 7:
            auxiliar = nuevo - self.INICIO_7
            mdb.Act_Tiempos(7,auxiliar)
        if Nro == 8:
            auxiliar = nuevo - self.INICIO_8
            mdb.Act_Tiempos(8,auxiliar)
        if Nro == 9:
            auxiliar = nuevo - self.INICIO_9
            mdb.Act_Tiempos(9,auxiliar)
        if Nro == 10:
            auxiliar = nuevo - self.INICIO_10
            mdb.Act_Tiempos(10,auxiliar)

    # Guarda el acumulado en la base de datos. A ésta función se la llama cada vez que se detiene un temporizado indicando cuál es el mismo, y también cada un minuto.
    def Guardar_Progreso(self):
        nuevo = int(time.time())
        if self.INICIO_1 > 0:
            auxiliar = nuevo - self.INICIO_1 + self.ACUM_1
            mdb.Act_Tiempos(1,auxiliar)
        if self.INICIO_2 > 0:
            auxiliar = nuevo - self.INICIO_2 + self.ACUM_2
            mdb.Act_Tiempos(2,auxiliar)
        if self.INICIO_3 > 0:
            auxiliar = nuevo - self.INICIO_3 + self.ACUM_3
            mdb.Act_Tiempos(3,auxiliar)
        if self.INICIO_4 > 0:
            auxiliar = nuevo - self.INICIO_4 + self.ACUM_4
            mdb.Act_Tiempos(4,auxiliar)
        if self.INICIO_5 > 0:
            auxiliar = nuevo - self.INICIO_5 + self.ACUM_5
            mdb.Act_Tiempos(5,auxiliar)
        if self.INICIO_6 > 0:
            auxiliar = nuevo - self.INICIO_6 + self.ACUM_6
            mdb.Act_Tiempos(6,auxiliar)
        if self.INICIO_7 > 0:
            auxiliar = nuevo - self.INICIO_7 + self.ACUM_7
            mdb.Act_Tiempos(7,auxiliar)
        if self.INICIO_8 > 0:
            auxiliar = nuevo - self.INICIO_8 + self.ACUM_8
            mdb.Act_Tiempos(8,auxiliar)
        if self.INICIO_9 > 0:
            auxiliar = nuevo - self.INICIO_9 + self.ACUM_9
            mdb.Act_Tiempos(9,auxiliar)
        if self.INICIO_10 > 0:
            auxiliar = nuevo - self.INICIO_10 + self.ACUM_10
            mdb.Act_Tiempos(10,auxiliar)

    # Recibe unos segundos en int, y devuelve lo que debe mostrar en pantalla en formato de string 00:00:00
    def Dev_string_tiempo(self, Tiempo):
        if Tiempo > 60:
            if Tiempo > 3600:
                horas = Tiempo // 3600
                minutos = (Tiempo - (horas * 3600)) // 60
                segundos = Tiempo - (horas * 3600) - (minutos * 60)

                if horas > 9:
                    horas = str(horas) + ":"
                else:
                    horas = "0" + str(horas) + ":"

                if minutos > 9:
                    minutos = str(minutos) + ":"
                else:
                    minutos = "0" + str(minutos) + ":"

                if segundos > 9:
                    segundos = str(segundos)
                else:
                    segundos = "0" + str(segundos)
                return horas + minutos + segundos
            else:
                minutos = Tiempo // 60
                segundos = Tiempo - (minutos * 60)

                if minutos > 9:
                    minutos = str(minutos) + ":"
                else:
                    minutos = "0" + str(minutos) + ":"

                if segundos == 60 or segundos == 0:
                    segundos = "00"
                elif segundos > 9:
                    segundos = str(segundos)
                else:
                    segundos = "0" + str(segundos)
                return "00:" + minutos + segundos
        else:
            if Tiempo == 60:
                return "00:01:00"
            elif Tiempo > 9 and Tiempo < 60:
                Tiempo = str(Tiempo)
            else:
                Tiempo = "0" + str(Tiempo)
        return "00:00:" + Tiempo

    # Calcula el tiempo transcurrido e

if __name__ == '__main__':
    aplicacion = QApplication(sys.argv)
    ui = V_Ppal()
    ui.show()
    sys.exit(aplicacion.exec_())