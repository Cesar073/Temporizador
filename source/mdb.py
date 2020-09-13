#Biblioteca para conectarse a base de datos SQLite
import sqlite3
import calendar
from datetime import date, datetime

'''
FUNCIONES PARA EL MANEJO DE LA BASE DE DATOS

    Tabla: Actividades
    Parámetros:
        Seguimiento: Indica la manera en que se va a controlar el tiempo.
            0= Sólo contabilizamos el tiempo
            1= Controlamos que cumpla la exigencia diaria
            2= Controlamos que cumpla la exigencia semanal
            3= Controlamos que cumpla la exigencia mensual
        Nombre:
        Activo: Con 0 o 1 determinamos si se tiene en cuenta o no la actividad.
        Orden: Es el órden en que queremos que aparezca en la lista.
        Obj_Dia-Sem-Mes= Objetivo en float en función al tiempo que deseamos alcanzar.
    
    Tabla: Tiempos
    Contiene el acumulado para los tiempos del día, semana y mes. Luego mediantes 0 y 1, se indica qué días se deben tener en cuenta.
    Las columnas que hay son: ID, T_Dia, T_Sem, T_Mes, Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo
'''
BaseDeDatos = "./source/tiempos.db"

# Nuevo Registro
def Agrega_Registro(Seguimiento, Nombre, Activo_V_F = False, Orden = 0, Obj_Dia = 0.0, Obj_Sem = 0.0, Obj_Mes = 0.0,Lunes = 0, Martes = 0, Miercoles = 0, Jueves = 0, Viernes = 0, Sabado = 0, Domingo = 0, Dia_Inicio = 0.0):
    Add_Registro_Actividades(Seguimiento, Nombre, Activo_V_F, Orden, Obj_Dia, Obj_Sem, Obj_Mes)
    Add_Registro_Tiempos(Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo, Dia_Inicio)
def Add_Registro_Actividades(Seguimiento, Nombre, Activo_V_F = False, Orden = 0, Obj_Dia = 0.0, Obj_Sem = 0.0, Obj_Mes = 0.0):
    Activo = 0
    if Activo_V_F == True:
        Act_Valores_Config(True)
        Activo = 1
    sql = 'INSERT INTO Actividades VALUES(NULL, ?, ?, ?, ?, ?, ?, ?)'
    parametros = (Seguimiento, Activo, Orden, Nombre, Obj_Dia, Obj_Sem, Obj_Mes)
    Realiza_consulta(sql,parametros)
def Add_Registro_Tiempos(Lunes = 0, Martes = 0, Miercoles = 0, Jueves = 0, Viernes = 0, Sabado = 0, Domingo = 0, Dia_Inicio = 0.0):
    sql = 'INSERT INTO Tiempos VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    Tiempo = 0.0
    parametros = (Tiempo, Tiempo, Tiempo, Lunes, Martes, Miercoles, Jueves, Viernes, Sabado, Domingo, Dia_Inicio)
    Realiza_consulta(sql,parametros)
def Act_Valores_Config(Activo_V_F):
    valor = Dev_Cant_Actividades()
    valor += 1
    sql = 'UPDATE Config Set Valor = {} WHERE ID = 1'.format(valor)
    Realiza_consulta(sql)

    if Activo_V_F == True:
        valor = Dev_Cant_Activos()
        valor += 1
        sql = 'UPDATE Config Set Valor = {} WHERE ID = 2'.format(valor)
        Realiza_consulta(sql)

# Actualiza los valores acumulados en la base de datos
def Act_Tiempos(Actividad, Tiempo):
    '''
    acumDia = Dev_Tiempo_Acum_Dia(Actividad)
    acumDia += Tiempo
    acumSem = Dev_Tiempo_Acum_Sem(Actividad)
    acumSem += Tiempo
    acumMes = Dev_Tiempo_Acum_Mes(Actividad)
    acumMes += Tiempo
    '''
    Act_Tiempo(Actividad, Tiempo, Tiempo, Tiempo)

# Suministra los datos
def Dev_Cant_Activos():
    sql = 'SELECT Valor FROM Config WHERE ID = 2'
    reg = Realiza_consulta(sql)
    aux = 0
    for i in reg:
        aux = i[0]
    return aux
def Dev_Cant_Actividades():
    sql = 'SELECT Valor FROM Config WHERE ID = 1'
    reg = Realiza_consulta(sql)
    aux = 0
    for i in reg:
        aux = i[0]
    return aux
def Dev_Tiempo_Acum_Dia(Actividad):
    sql = 'SELECT * FROM Tiempos WHERE ID = {}'.format(Actividad)
    reg = Realiza_consulta(sql)
    aux = 0
    for i in reg:
        aux = i[1]
    return aux
def Dev_Tiempo_Acum_Sem(Actividad):
    sql = 'SELECT * FROM Tiempos WHERE ID = {}'.format(Actividad)
    reg = Realiza_consulta(sql)
    aux = 0
    for i in reg:
        aux = i[2]
    return aux
def Dev_Tiempo_Acum_Mes(Actividad):
    sql = 'SELECT * FROM Tiempos WHERE ID = {}'.format(Actividad)
    reg = Realiza_consulta(sql)
    aux = 0
    for i in reg:
        aux = i[3]
    return aux

# Actualiza tiempos.
    # Coloca el tiempo que debe haber en cada momento (dia, sem, mes), pero también calcula si hay que reinciarlo y lo ejecuta.
    # Si por ejemplo una semana debe cumplir 20 horas, no se reinicia el contador hasta que se hayan cumplido esas 20 horas. De ésta manera mantenemos los datos en la db hasta
    # que el usuario cumpla con su cuota, que puede producirse a la semana siguiente por ejemplo.
def Act_Tiempo(Actividad, T_Dia = 0, T_Sem = 0, T_Mes = 0):
    if T_Dia > 0:
        # Averiguamos si hay que reiniciar los valores para el día. Se dá cuando se supera el tiempo estimado para un día.
        diaSem = datetime.weekday(date.today()) + 1
        if Dev_Act_Diaria(Actividad, diaSem) == 1:
            Segundos = Dev_Corresponde_Dia(Actividad)
            if T_Dia > Segundos:
                T_Dia -= Segundos
        sql = 'UPDATE Tiempos SET T_Dia = {} WHERE ID = {}'.format(T_Dia, Actividad)
        Realiza_consulta(sql)
    if T_Sem > 0:
        # Averiguamos si hay que reiniciar los valores para la semana. Se dá cuando se supera el tiempo estimado para la semana.
        valor = Dev_Corresponde_Sem(Actividad)
        if T_Sem > valor:
            T_Sem -= valor
        sql = 'UPDATE Tiempos SET T_Sem = {} WHERE ID = {}'.format(T_Sem, Actividad)
        Realiza_consulta(sql)
    if T_Mes > 0:
        sql = 'UPDATE Tiempos SET T_Mes = {} WHERE ID = {}'.format(T_Mes, Actividad)
        Realiza_consulta(sql)

# Devuelve 0 o 1 si en el día indicado por parámetro hay que reiniciar los datos
def Dev_Act_Diaria(Actividad, Dia):
    sql = 'SELECT * FROM Tiempos WHERE ID = {}'.format(Actividad)
    reg = Realiza_consulta(sql)
    aux = 0
    for i in reg:
        aux = i[3 + Dia]
    return aux

# Devuelve la cantidad de días por semana, y una lista con los días indicados
def Dev_Datos_Semana(Actividad):
    sql = 'SELECT * FROM Tiempos WHERE ID = {}'.format(Actividad)
    reg = Realiza_consulta(sql)
    aux = 0
    lista = [0,0,0,0,0,0,0]
    for i in reg:
        cont = 4
        while cont < 11:
            aux += i[cont]
            if i[cont] == 1:
                lista[cont-4] = 1
            cont += 1
    return aux, lista

# Calcula lo que corresponde hacer en el día actual. Teniendo en cuenta que a ésta función se la llama sólo si el día de hoy está configurado como activo
def Dev_Corresponde_Dia(Actividad):
    sql = 'SELECT * FROM Actividades WHERE ID = {}'.format(Actividad)
    reg = Realiza_consulta(sql)
    auxD = 0
    auxS = 0
    auxM = 0
    for i in reg:
        auxD = i[5]
        auxS = i[6]
        auxM = i[7]
    
    if auxD == 0:
        cantDias, Dias = Dev_Datos_Semana(Actividad)
        if auxS == 0:
            today = date.today()
            mes = today.month()
            anio = today.year()
            MesCompleto = calendar.monthcalendar(anio, mes)
            contador = 0
            for Semana in MesCompleto:
                cuentaDia = 0
                while cuentaDia < 7:
                    if Semana[cuentaDia] > 0 and Dias[cuentaDia] == 1:
                        contador += 1
                    cuentaDia += 1
            return auxM // contador
        else:
            return auxS // cantDias
    else:
        return auxD

# Devuelve el valor correspondiente a una semana
def Dev_Corresponde_Sem(Actividad):
    sql = 'SELECT * FROM Actividades WHERE ID = {}'.format(Actividad)
    reg = Realiza_consulta(sql)
    auxS = 0
    for i in reg:
        auxS = i[6]
    return auxS

# DEVUELVE UN REGISTRO BUSCADO SEGÚN UN DATO EN PARTICULAR
def Reg_Un_param(BaseDeDatos, Tabla, Columna, DatoCoincide):
    sql = 'SELECT * FROM {} WHERE {} = {}' .format( Tabla, Columna, DatoCoincide)
    Resultado = Realiza_consulta(BaseDeDatos,sql)
    return Resultado

# INSERTA UN REGISTRO EN LA BASE DE DATOS
def Reg_Add( Tabla, Activo = 1, Codigo = '', Concepto = '', Marca = '', Detalle = '', PrecioCpa = '', PrecioVta = '', Cantidad = '', CodXBulto = '', CantXBulto = '', FechaVto = '', FechaUlt = '', AcumCpra = '', AcumVendido = '',Clasificacion = ''):
    sql = 'INSERT INTO Productos VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
    parametros = (Activo, Codigo, Concepto, Marca, Detalle, PrecioCpa, PrecioVta, Cantidad, CodXBulto, CantXBulto, FechaVto, FechaUlt, AcumCpra, AcumVdido, Clasificacion)
    Realiza_consulta(BaseDeDatos, sql, parametros)


# ACTUALIZA LA BASE DE DATOS
def Act_Reg(BaseDeDatos, Tabla, ID, Activo, Codigo, Concepto, Marca, Detalle, PrecioCpa, PrecioVta, Cantidad, CodXBulto, CantXBulto, FechaVto, Clasificacion):
    query = 'UPDATE Productos SET Activo = ?, Codigo = ?, Concepto = ?, Marca = ?, Detalle = ?, PrecioCpa = ?, PrecioVta = ?, Cantidad = ?, CodXBulto = ?, CantXBulto = ?, FechaVto = ?, Clasificacion = ? WHERE ID = ?'
    parameters = (Activo, Codigo, Concepto, Marca, Detalle, PrecioCpa, PrecioVta, Cantidad, CodXBulto, CantXBulto, FechaVto, Clasificacion, ID)
    Realiza_consulta(BaseDeDatos, query, parameters)


#CONECTA CON LA BD, Y RETORNA LOS DATOS SOLICITADOS
# Los pasos para trabajar en la bd, son: Conectarse, realizar la consulta, cargarla en una variable y desconectarse
# query será el parámetro que traiga el tipo de consuta que se desea, y en caso de haber parámetros, se utilizarán, de lo contrario, la tupla queda vacía
def Realiza_consulta( query, parameters = ()):
    # Realizamos la conección y la almacenamos en la variable conn
    with sqlite3.connect(BaseDeDatos) as conn:
        # Cursor, es una propiedad que nos indica en qué posición estamos dentro de la base de datos, y lo almacenamos en la variable Cur
        Cur = conn.cursor()
        # Execute, es la función que realiza la consulta, y los resultados obtenidos serán almacenados en la variable resultado
        resultado = Cur.execute(query, parameters)
        conn.commit()
    return resultado


# BUSCA UN REGISTRO SEGÚN UN CÓDIGO. 
# DEVUELVE 3 VARIABLES:
    # VARIABLE 1:
        # 0 = Cuando no existe el código
        # 1 = Código normal
        # 2 = Código de paquete, de bulto cerrado
    # VARIABLE 2: Los datos
    # VARIABLE 3: Estado del producto (0/1/2 >>> Baja, Alta o Completo)
def Busca_Cod(BBDD, Tabla, Columna, DatoCoincide):
    
    # Buscamos el dato de la lista de códigos principal
    Registro = Reg_Un_param(BBDD, Tabla, Columna, DatoCoincide)

    # He creado primero la lista row con valores de cero(0), porque no puedo capturar la excepción en caso de que haya un error al no
        # encontrar el código en la base de datos. Entonces, la línea: for posicion in Registro: no se ejecuta cuando el valor del Registro es
        # nulo. Al no ejecutarse, row no se actualiza, por ende, deduzco si se encontró o no el Registro.
    row = [ '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    for posicion in Registro:
        row = [posicion[0], posicion[1], posicion[2], posicion[3], posicion[4], posicion[5], posicion[6], posicion[7], posicion[8], posicion[9], posicion[10], posicion[11], posicion[12], posicion[13], posicion[14], posicion[15]]

    # Con éste if, determino si se han cargado los datos o no.
    # True: NO SE ENCONTRÓ EL CODIGO EN LA BD. False: Ejecución normal
    if row[2] == '0':
        Registro = Reg_Un_param(BBDD, Tabla, 'CodXBulto', DatoCoincide)
        for posicion in Registro:
            row = [posicion[0], posicion[1], posicion[2], posicion[3], posicion[4], posicion[5], posicion[6], posicion[7], posicion[8], posicion[9], posicion[10], posicion[11], posicion[12], posicion[13], posicion[14], posicion[15]]
        if row[2] == '0':
            return 0, 0, 0
        else:
            return 2, row, posicion[1]
    else:
        return 1, row, posicion[1]

#Agrega_Registro(1, "TaeKwon-do", True, Obj_Sem = 5.0, Lunes = 1, Martes = 1, Miercoles = 1, Jueves = 1, Viernes = 1)
#print(calendar.monthcalendar(2020,9))
#print(datetime.weekday(date.today()))
#Act_Tiempo(1, 70)