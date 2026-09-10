from app.extraction.pdf_extractor import extract_text_pdf

PDF_PATH = "data/test/cv_test.pdf"

def main():
    text = extract_text_pdf(PDF_PATH)

    print("=" * 50)
    print("Texte extrait du CV :")
    print("=" * 50)
    print(text)

if __name__ == "__main__":
    main()