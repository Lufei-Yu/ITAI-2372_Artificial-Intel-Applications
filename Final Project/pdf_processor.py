from io import BytesIO
from PyPDF2 import PdfReader


def extract_text_from_pdf(uploaded_file) -> str:
    """Extract selectable text from an uploaded PDF file."""
    try:
        reader = PdfReader(BytesIO(uploaded_file.getvalue()))

        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception as exc:
                raise ValueError("This PDF is password-protected.") from exc

        pages = []
        for page_number, page in enumerate(reader.pages, start=1):
            page_text = page.extract_text() or ""
            if page_text.strip():
                pages.append(f"Page {page_number}\n{page_text}")

        extracted = "\n\n".join(pages).strip()
        if not extracted:
            raise ValueError(
                "No selectable text was found. This may be a scanned PDF; "
                "OCR support is not included in this starter version."
            )
        return extracted
    except ValueError:
        raise
    except Exception as exc:
        raise ValueError(f"PDF extraction failed: {exc}") from exc
