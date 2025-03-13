import requests
import pandas as pd

def get_isbn_google_books(title, author):
    """Sucht nach ISBN-10 und ISBN-13 mit der Google Books API, nur englische Bücher."""
    query = f"{title} {author}"
    url = f"https://www.googleapis.com/books/v1/volumes?q={query}&langRestrict=en"

    response = requests.get(url)
    data = response.json()

    if "items" in data:
        book = data["items"][0]["volumeInfo"]
        isbn_10, isbn_13 = None, None
        for identifier in book.get("industryIdentifiers", []):
            if identifier["type"] == "ISBN_10":
                isbn_10 = identifier["identifier"]
            if identifier["type"] == "ISBN_13":
                isbn_13 = identifier["identifier"]
        return isbn_10, isbn_13
    return None, None

# Lade die Excel-Datei
file_path = "datasets/Buecher.xlsx"
df = pd.read_excel(file_path)

if "Titel" in df.columns and "Autor" in df.columns:
    df["ISBN-10"] = None
    df["ISBN-13"] = None

    for index, row in df.iterrows():
        title, author = row["Titel"], row["Autor"]
        isbn10, isbn13 = get_isbn_google_books(title, author)
        df.at[index, "ISBN-10"] = isbn10
        df.at[index, "ISBN-13"] = isbn13
        print(f"{title} - {author}: ISBN-10: {isbn10}, ISBN-13: {isbn13}")

    # Speichere die aktualisierte Datei
    df.to_excel("datasets/Buchpreise_2009-2024xlsx", index=False)
    print("Alle ISBNs wurden gespeichert in 'Buchpreise_2009-2024.xlsx'!")

else:
    print("Fehler: Die Excel-Datei braucht Spalten 'Titel' und 'Autor'!")
