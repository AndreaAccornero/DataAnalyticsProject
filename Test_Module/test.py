
####################################################### Metodi da implementare #######################################################

"""
    Funzione che restituisce un identificativo dello studente o del gruppo     
    
    -- OUTPUT:
    Stringa identificativa della consegna
"""
def getName():
    return "Andrea Accornero, Alessandro Tocco"

"""
    Funzione che effettua il pre-processing dei dati di test forniti in input. Il metodo deve caricare i parametri determinati durante 
    la fase di TRAINING, per le tecniche di preprocessing scelte.
    
    -- INPUT:
        - Dataframe Pandas contenente i dati di TEST. I dati hanno la stessa struttura (numero e nomi attributi) di quelli usati per 
        il TRAINING.
        - clfName: stringa che identifica la tecnica di ML da utilizzare, e che può assumere i valori indicati nella slide successiva
    
    -- OUTPUT:
        Dataframe Pandas ottenuto come risultato del pre-processamento.
"""
def preprocess(df, clfName):
    return

"""
    Funzione che istanzia la tecnica di ML con nome clfName
    
    -- INPUT:
        clfName: stringa che identifica la tecnica di ML da utilizzare, e che può assumere i valori indicati
    
    -- OUTPUT:
        Oggetto Python relativo all’istanza dell’algoritmo di ML, con iper-parametri determinati durante la fase di TRAINING. 
        Se l’algoritmo non è stato implementato, deve restituire un valore None. 
"""
def load(clfName):
    return
    

"""
Funzione che esegue il modello ML (oggetto clf) sui dati di TEST preprocessati (df)

-- INPUT:
    - df: dataframe di TEST, ottenuto come output del metodo di preprocess descritta precedentemente
    - clfName: stringa che identifica la tecnica di ML da utilizzare
    - clf: istanza dell’algoritmo di ML, ottenuto come output del metodo di load descritto precedentemente

-- OUTPUT:
    Dizionario Python contenente i valori di prestazioni dell’algoritmo di ML quando eseguito sui dati di TEST preprocessati 
"""
def predict(df, clfName, clf):
    return

#####################################################################################################################################