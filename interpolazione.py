import pandas as pd
import statistics

file_excel = 'dati.xls'

def crea_liste(excelFile): #crea le liste dei tempi e delle cordinate
    t_Action = pd.read_excel(excelFile, index_col=None, na_values=['NA'], usecols = "A").dropna().to_numpy()
    x_Action = pd.read_excel(excelFile, index_col=None, na_values=['NA'], usecols = "B").dropna().to_numpy()
    t_Vicon = pd.read_excel(excelFile, index_col=None, na_values=['NA'], usecols = "C").to_numpy()
    x_Vicon = pd.read_excel(excelFile, index_col=None, na_values=['NA'], usecols = "D").to_numpy()
    return t_Action, x_Action, t_Vicon, x_Vicon

def istantiVicini(tempo_action, t_vicon, x_vicon ):
    distanze = []
    x_vicine = []
    print(tempo_action)
    t_vicon = t_vicon.flatten()
    x_vicon = x_vicon.flatten()

    for element in t_vicon:
        distanze.append(abs(element - tempo_action))

    posizione_minima = distanze.index(min(distanze))
    x_vicine.append(x_vicon[posizione_minima])
    #print("prima ", t_vicon[posizione_minima:])

    distanza_prima = abs(t_vicon[posizione_minima - 1] - tempo_action)

    if posizione_minima + 1 < len(t_vicon):
        distanza_dopo = abs(t_vicon[posizione_minima + 1] - tempo_action)
    else:
        distanza_dopo = distanza_prima

    if distanza_prima <= distanza_dopo:
        print("tempi Vicon vicini trovati :", t_vicon[posizione_minima - 1], t_vicon[posizione_minima])
        x_vicine.append(x_vicon[posizione_minima - 1])
        x_vicine.reverse()
    else:
        print("tempi Vicon vicini trovati :", t_vicon[posizione_minima], t_vicon[posizione_minima + 1])
        if posizione_minima + 1 < len(t_vicon):
            x_vicine.append(x_vicon[posizione_minima + 1])
        else:
            x_vicine.append(x_vicon[posizione_minima - 1])
            x_vicine.reverse()

    print(x_vicine)
    return x_vicine



t_Action, x_Action, t_Vicon, x_Vicon = crea_liste(file_excel)
coordinate = []

"""for tempo in t_Action[0:4]:
    x_vicini = istantiVicini(tempo, t_Vicon, x_Vicon)
    #print(len(x_vicini))

    #print("primo elemento di x_vicini = ", x_vicini[0], "secondo elemento: ", x_vicini[1], "media =", statistics.median(x_vicini))
    coordinate.append(statistics.median(x_vicini))"""

for tempo in t_Action:
    x_vicini = istantiVicini(tempo, t_Vicon, x_Vicon)

    coordinate.append(statistics.median(x_vicini))






output = 'nuove_coordinate.xls'
df = pd.DataFrame(coordinate)
df.to_excel(output, index=False)

print(coordinate)
print("ci sono ", len(coordinate), " elementi interpolati e ", len(x_Action), " coordinate di Action Cam")



