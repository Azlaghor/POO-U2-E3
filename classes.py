class register:
    __temperature = 0
    __humidity = 0
    __pressure = 0.0

    # ========== INIT ========== #
    def __init__(self, temp, hdm, press):
        self.__temperature = temp
        self.__humidity = hdm
        self.__pressure = press

    # ========== SETTERS ========== #
    def setTemperature(self, v):
        self.__temperature = v

    def setHumidity(self, v):
        self.__humidity = v

    def setPressure(self, v):
        self.__pressure = v

    # ========== GETTERS ========== #
    def getTemperature(self):
        return self.__temperature

    def getHumidity(self):
        return self.__humidity
    
    def getPressure(self):
        return self.__pressure