Per apprendimento e test vengono utilizzati dei database contenuti nei files:
"datatraining.txt" https://archive.ics.uci.edu/ml/datasets/Occupancy+Detection+
"Roman Urdu DataSet.csv" https://archive.ics.uci.edu/ml/datasets/Roman+Urdu+Data+Set
"winequality-red.csv" https://archive.ics.uci.edu/ml/datasets/Wine+Quality
Per ognuno di questi 3 database il programma ne legge il contenuto e costruisce 2 liste,
una contenente le classi dei vari esempi, e l' altra codifica ogni esempio in base alla propria posizione
nel database originale. Vengono quindi creati altre due liste, una contenente gli esempi con classe positiva
e una con gli esempi di classe negativa, e poi vengono mischiati randomicamente gli elementi delle due liste.
Quindi, si procede alla creazione della lista corrispondente al training set e a  quella corrispondente al test set,
che vengono passate alla funzione che implementa l' algoritmo di Voted Perceptron.
Alla fine vengono stampati media e variazione standard della test accuracy.
Per ottenere i risultati basta semplicemente eseguire il file main.py

Per scrivere il codice ho preso spunto da alcuni siti, soprattutto per capire la lettura dei file .csv e .txt:
https://realpython.com/python-csv/
https://stackoverwlof.com/questions/21546739/load-data-from-txt-with-pandas
https://www.asjpython.com/python/list/python-list-of-tuples