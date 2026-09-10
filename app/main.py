from app.extraction.pdf_extractor import extract_text_pdf
from app.preprocessing.cleaner import clean_text
from app.nlp.section_parser import parse_sections

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

    # Regroupement par section
    sections = parse_sections(cleaned_text)
    print("\n")
    print("=" * 50)
    print("Sections du CV :")
    print("=" * 50)
    for section, content in sections.items():
        print(f"\n[{section.upper()}]")
        for line in content:
            print(f"  - {line}")

if __name__ == "__main__":
    main()