# Interpolazione Dati Vicon - Action Cam
Permette il confronto tra dati provenienti da videocamere diverse

## Utilizzi

Il problema che si presentava era quello di avere un numero di dati diverso, in quanto alcune videocamere riprendevano a 200FPS (VICON)
mentre altre riprendevano a 120FPS (Action Cam), rendendo cosi impossibile un confronto nel tempo dei vari dati.
Il progetto quindi permette di prendere i dati relativi ad un marker e di "comprimere" i dati provenienti dalle videocamere a 200FPS in
modo che risultino confrontabili con i dati provenienti dalle altre videocamere.
Siccome nel codice non si fa mai riferimento al numero di frame è possibile confrontare dati provenienti da registrazioni a diversi FPS

### Come impostare i dati

All'interno del progetto si trova un file denominato 'dati.xls' all'interno del quale troviamo 4 colonne che rappresentano corrispettivamente il tempo e le coordinate del marker analizzando il video della videocamera con meno FPS ed il tempo e coordinate del marker analizzando il video a maggiori FPS.
Per impostare i dati incollare al di sotto di ogni indicazione i propri dati 

### Come funziona il programma
Il programma mette in relazione i dati della videocamera con maggiori FPS ai tempi dettati dalla videocamera con meno FPS. Va quindi a 
trovare i due istanti di tempo più vicini al tempo dettato e tramite una interpolazione lineare restituisce una coordinata questa volta 
relativa ad un tempo comune per entrambe le videocamere.

### Output del programma
Le nuove coordinate si trovano nel file denominato 'nuove_coordinate.xls' nella prima colonna
N.B. La prima riga non è da considerare, le coordinate partono dalla seconda riga



