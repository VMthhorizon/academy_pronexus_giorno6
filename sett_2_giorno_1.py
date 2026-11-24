import numpy as np
import pandas as pd
import csv
import psycopg2
import os

from dotenv import load_dotenv
from psycopg2 import Error

load_dotenv()


def connect_db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
    )


def csv_dipartimenti():
    try:
        connessione = connect_db()

        cursore = connessione.cursor()

        query = "SELECT * FROM dipartimento"

        cursore.execute(query)

        result_set = cursore.fetchall()
        intestazione_dipartimenti = [col[0] for col in cursore.description]

        cursore.close()

    except Error as errore:
        print(f"Errore nella connessione al DB: {errore}")

    finally:
        if "connessione" in locals() and connessione:
            connessione.close()
            print("Connessione al DB chiusa")

    if result_set:

        try:

            with open("dipartimenti.csv", "w", newline="", encoding="utf-8") as file:

                writer = csv.writer(file)
                writer.writerow(intestazione_dipartimenti)
                writer.writerows(result_set)

        except OSError as e:
            print(f"ERRORE nel file csv: {e}")


"""
intestatione_dipendenti = ["id_dipendente","Nome","Cognome","Email","Data di Assunzione","Stipendio","id_dipartimento"]
lista_dipendenti = []

try:
    connessione = connect_db()

    cursore = connessione.cursor()

    query = "SELECT * FROM Dipendente;"

    cursore.execute(query)
    result_set = cursore.fetchall()

    if result_set:
        for riga in result_set:
            lista_dipendenti.append(riga)
    else:
        print("Nessun risultato trovato")

except Error as errore:
    print(f"Connessione Fallita : {errore}")

finally:
     if "connessione" in locals() and connessione:
          connessione.close()
          print("Connessione chiusa")

if lista_dipendenti:
     
    try:
        with open("dipendenti.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(intestatione_dipendenti)
                writer.writerows(lista_dipendenti)

    except OSError as e:
        print(f"ERRORE: {e}")"""
