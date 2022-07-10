#Defino librerias a utilizar
import csv
import datetime as dt
#Se definen constantes y variables
opciones = """
Bienvenido al programa de control de cheques
--------------------------------------------
Por favor seleccione una opcion
1. Ingreso de datos
2. Salir
"""
cheques = []
runtime = True
datetime = dt.date.today()

#Defino funciones
def readFile(urlfile):
    file = open(urlfile+".csv", "r")
    csvfile = csv.reader(file)
    for row in csvfile:
        if row !=[]:
            data = {"NroCheque":row[0],"CodigoBanco":row[1],"CodigoScurusal":row[2],
                    "NumeroCuentaOrigen":row[3],"NumeroCuentaDestino":row[4],
                    "Valor":row[5],"FechaOrigen":row[6],"FechaPago":row[7],
                    "DNI":row[8],"Tipo":row[9],"Estado":row[10]}
            cheques.append(data)
    file.close()
    return cheques

def buscarPorDni(dni, tipo):
    busqueda = []
    cantidad = 0
    cheques = readFile(urlfile)
    for cheque in cheques:
        if cheque["DNI"] == dni and cheque["Tipo"] == tipo:
            cantidad += 1
            busqueda.append(cheque)
    print(f"Se encontraron {cantidad} de cheques")
    repetidos = []
    for che in busqueda:
        for che2 in busqueda:
            if che["NroCheque"] == che2["NroCheque"]:
                repetidos.append(che)
            repetidos.append(cheque["NroCheque"])
    if repetidos == []:
        print("Se encontraron repetidos")
        return "ERROR Se encontraron repetidos"
    else:
        return busqueda
    
  
def grabarCSV(dni, busqueda):
    print(dni, busqueda)
    file = open(str(dni)+"_"+str(datetime)+".csv", "w")
    csvfile = csv.writer(file)
    for row in busqueda:
        csvfile.writerow(
            [row["NumeroCuentaOrigen"], row["Valor"], row["FechaOrigen"], row["FechaPago"]])
    file.close()
    print("Se grabo el archivo CSV")   
    
#Defino metodo principal
if __name__ == '__main__':
    while runtime:
        print(opciones)
        op = input()
        if op == "1":
            urlfile = input("Ingrese el nombre del archivo que contiene los cheques: \n")
            dni = input("Ingrese el DNI del usuario a consultar: \n")
            tipo = input("Seleccione el tipo de cheque a buscar EMITIDO o DEPOSITADO: \n")
            salida = input("Elija si desea recibir la salida por PANTALLA o CSV: \n")
            try:
                resultado = buscarPorDni(dni, tipo)
                if salida == "PANTALLA":
                    print(resultado)
                elif salida == "CSV":
                    grabarCSV(resultado)
            except:
                print("Ingreso un dato erroneo")
            continue
        else:
            runtime = False