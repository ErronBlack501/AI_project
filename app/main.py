from app.extraction.pdf_extractor import extract_text_pdf
from app.preprocessing.cleaner import clean_text

PDF_PATH = "data/test/cv_test.pdf"

def main():
    # Extraction
    raw_text = extract_text_pdf(PDF_PATH)
    print("=" * 50)
    print("Texte extrait du CV :")
    print("=" * 50)
    print(raw_text)

    # Nettoyage
    cleaned_text = clean_text(raw_text)
    print("\n")
    print("=" * 50)
    print("Texte nettoyé du CV :")
    print("=" * 50)
    print(cleaned_text)

if __name__ == "__main__":
    main()