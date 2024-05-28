import fitz  

def extract_highlighted_text_from_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    highlighted_text = []

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        annotations = page.annots()
        if annotations:
            for annot in annotations:
                if annot.type[0] == 8:  
                    rect = annot.rect  
                    text = page.get_text("text", clip=rect)  
                    highlighted_text.append(text.strip())

    pdf_document.close()
    return highlighted_text

pdf_path = "BUSTA_PAGA - 2.pdf"
highlighted_text = extract_highlighted_text_from_pdf(pdf_path)
print(highlighted_text)
