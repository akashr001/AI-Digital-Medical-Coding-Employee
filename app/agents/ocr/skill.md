# Sarvam Vision OCR Agent

Purpose:

Convert PDFs, images, scans and medical documents into structured markdown text.

Input:

state["document_path"]

Output:

state["ocr_text"]

Responsibilities:

- Upload document
- Run Sarvam Vision OCR
- Extract markdown output
- Preserve tables and layout
- Pass text to Extraction Agent