import pandas as pd
import statistics
import scipy.interpolate as interpolate

class Interpolate:

    def __init__(self, excelFile):
        self.times =  pd.read_excel(excelFile, index_col=None, na_values=['NA'], usecols = "A").dropna().to_numpy()
        self.coords = pd.read_excel(excelFile, index_col=None, na_values=['NA'], usecols = "B").dropna().to_numpy()
        self.timesTointerpolate = pd.read_excel(excelFile, index_col=None, na_values=['NA'], usecols = "C").to_numpy()
        self.coordTointerpolate = pd.read_excel(excelFile, index_col=None, na_values=['NA'], usecols = "D").to_numpy()

    def istantiVicini(self, tempo_action):
        deltat = []
        x_vicine = []
        t_vicine = []

        timesTointerpolate = self.timesTointerpolate.flatten()
        coordTointerpolate = self.coordTointerpolate.flatten()
        for element in timesTointerpolate:
            deltat.append(abs(element - tempo_action))

        posizione_minima = deltat.index(min(deltat))
        x_vicine.append(coordTointerpolate[posizione_minima])
        t_vicine.append(timesTointerpolate[posizione_minima])

        deltat_prima = abs(timesTointerpolate[posizione_minima - 1] - tempo_action)

        if posizione_minima + 1 < len(timesTointerpolate):
            deltat_dopo = abs(timesTointerpolate[posizione_minima + 1] - tempo_action)
        else:
            deltat_dopo = deltat_prima

        if deltat_prima <= deltat_dopo:
            print("tempi Vicon vicini trovati :", timesTointerpolate[posizione_minima - 1], timesTointerpolate[posizione_minima])
            x_vicine.append(coordTointerpolate[posizione_minima - 1])
            x_vicine.reverse()
            t_vicine.append(timesTointerpolate[posizione_minima - 1])
            t_vicine.reverse()
        else:
            print("tempi Vicon vicini trovati :", timesTointerpolate[posizione_minima], timesTointerpolate[posizione_minima + 1])
            if posizione_minima + 1 < len(timesTointerpolate):
                x_vicine.append(coordTointerpolate[posizione_minima + 1])
                t_vicine.append(timesTointerpolate[posizione_minima + 1])
            else:
                x_vicine.append(coordTointerpolate[posizione_minima - 1])
                x_vicine.reverse()
                t_vicine.append(timesTointerpolate[posizione_minima - 1])
                t_vicine.reverse()

        print(x_vicine)
        return x_vicine, t_vicine

    def linearinterpolation(self, coords, times, actualtime):
        coordinate = ((actualtime - times[1]) * coords[0] + (actualtime - times[0]) * coords[1])  / ((actualtime - times[1]) + (actualtime - times[0]))
        return coordinate



