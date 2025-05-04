import pandas as pd
from datetime import datetime

# Pfad zur CSV-Datei
dateipfad = "urlaub.csv"

# CSV einlesen
def lade_urlaube():
    try:
        df = pd.read_csv(dateipfad, parse_dates=["Startdatum", "Enddatum"])
        print("Urlaubsanträge geladen:\n")
        print(df)
        return df
    except FileNotFoundError:
        print("Keine Datei gefunden, es wird eine neue erstellt.")
        df = pd.DataFrame(columns=["Name", "Startdatum", "Enddatum", "Status"])
        df.to_csv(dateipfad, index=False)
        return df

# Neue Anfrage hinzufügen
def neuer_antrag(df):
    print("\n--- Neuen Urlaubsantrag hinzufügen ---")
    name = input("Name: ")
    start = input("Startdatum (YYYY-MM-DD): ")
    ende = input("Enddatum (YYYY-MM-DD): ")
    status = input("Status (offen/genehmigt/abgelehnt): ").lower()

    # Datum validieren
    try:
        start_dt = pd.to_datetime(start)
        ende_dt = pd.to_datetime(ende)
        if start_dt > ende_dt:
            print("Fehler: Startdatum liegt nach dem Enddatum.")
            return df
    except ValueError:
        print("Fehler: Ungültiges Datum.")
        return df

    # Konfliktprüfung
    konflikte = df[
        (df["Status"].str.lower() == "genehmigt") &
        (((start_dt <= df["Enddatum"]) & (ende_dt >= df["Startdatum"])))
        ]

    if not konflikte.empty:
        print("\n⚠️  Achtung: Es gibt Konflikte mit bestehenden genehmigten Urlaubsanträgen:")
        print(konflikte[["Name", "Startdatum", "Enddatum"]])
    else:
        print("\n✅ Keine Konflikte mit genehmigten Anträgen gefunden.")

    # Neuen Eintrag erstellen
    neuer_eintrag = {
        "Name": name,
        "Startdatum": start_dt,
        "Enddatum": ende_dt,
        "Status": status
    }

    # Anhängen mit pd.concat (statt append)
    df_neuer_antrag = pd.DataFrame([neuer_eintrag])
    df = pd.concat([df, df_neuer_antrag], ignore_index=True)
    df.to_csv(dateipfad, index=False)
    print("\nAntrag gespeichert. Aktuelle Übersicht:\n")
    print(df)
    return df

# Hauptcode, der geladen und hinzugefügt wird
urlaube = lade_urlaube()

while True:
    print("\nNeuen Urlaubsantrag hinzufügen? (j/n)")
    antwort = input("> ").lower()

    if antwort == "j":
        urlaube = neuer_antrag(urlaube)
    elif antwort == "n":
        print("Beendet. Datei wurde gespeichert.")
        break
    else:
        print("Bitte 'j' oder 'n' eingeben.")
