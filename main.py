from classes import register
from tabulate import tabulate
# ================ FUNCTION ================ #
def scrMaxMin(vList, days, hours):
    maxTemp = -100
    maxHdm  = -100
    maxPres = -100
    minTemp =  100
    minHdm  =  100
    minPres =  100

    for i in range(days):
        for j in range(hours):
            # ====== Temperature ====== #
            if vList[i][j].getTemperature() > maxTemp:
                maxTemp = vList[i][j].getTemperature()
            if vList[i][j].getTemperature() < minTemp:
                minTemp = vList[i][j].getTemperature()

            # ====== Humidity ====== #
            if vList[i][j].getHumidity() > maxHdm:
                maxHdm = vList[i][j].getHumidity()
            if vList[i][j].getHumidity() < minHdm:
                minHdm = vList[i][j].getHumidity()

            # ====== Pressure ====== #
            if vList[i][j].getPressure() > maxPres:
                maxPres = vList[i][j].getPressure()
            if vList[i][j].getPressure() < minPres:
                minPres = vList[i][j].getPressure()

    return maxTemp, maxHdm, maxPres, minTemp, minHdm, minPres

def scrAverage(vList, days, hours):
    hourNum = days * hours
    addition = 0
    for i in range(days):
        for j in range(hours):
            addition += vList[i][j].getTemperature()
    
    average = addition / hourNum

    return average


# ================ MAIN ================ #
if __name__ == "__main__":
    dataList = []
    for i in range(30):
        dataList.append([])
        for j in range(24):
            dataList[i].append(None)
    
    with open("data.txt") as archive:
        for line in archive:
            data = line.strip().split(",")

            tempObj = register(int(data[2]), int(data[3]), int(data[4]))
            i = int(data[0]) - 1
            j = int(data[1])
            # print(f"I = {i} J = {j}")
            dataList[i][j] = tempObj

    while True:
        option = input("""
        Seleccione a opcion que desee:
        A: Mostrar dia de extremos
        B: Mostrar promedio de temperatura
        C: Ingresar dia y recibir datos por cada hora
        D: Salir
        """)
        option.lower()
        if option == "a":
            # Metodo
            maxTemp, maxHdm, maxPres, minTemp, minHdm, minPres = scrMaxMin(dataList, 30, 24)
            print(f"""
            Dias de maximo valor
            Temperatura: {maxTemp}
            Humedad: {maxHdm}
            Presion atmosferica: {maxPres}

            Dias de minimo valor
            Temperatura: {minTemp}
            Humedad: {minHdm}
            Presion atmosferica: {minPres}
            """)
        elif option == "b":
            average = scrAverage(dataList, 30, 24)
            print(f"La temperatura promedio del mes es: {average}")
        elif option == "c":
            while True:
                i = input("Ingrese el dia: ")
                if i.isdigit():
                    i = int(i)
                    break
                else: print("No es un numero valido (Ingrese un digito del 1 al 30)")
                
            title = ["Hora", "Temperatura", "Humedad", "Presion"]
            table = []
            for j in range(24):
                inst = dataList[i-1][i]

                table.append([f"{j}:00", inst.getTemperature(), inst.getHumidity(), inst.getPressure()])

            print(tabulate(table, headers=title))
        elif option == "d":
            print("Espero haber sido util. By Lucifer")
            break