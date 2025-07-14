# Webpage Text Extractor & Summarizer using Gemini Pro

This Python project extracts visible text from any webpage, removes unnecessary HTML elements (like scripts, styles, headers, etc.), and then summarizes the cleaned content using Google’s Gemini Pro (via the `google-generativeai` API).

---

## Files Included

- `output.html` → Raw HTML content from the webpage  
- `clean_text.txt` → Cleaned, readable text extracted from HTML  
- `output_from_genai.txt` → AI-generated summary of the cleaned text  
- `README.md` → Project documentation

---
## Steps
- `extract_html.py` → is used to extract the html code from the webpage
- `clean.py` → This will clean all the headers, body, html tags etc
- `genai_clean.py` → This will give you the clean, structured data of the webpage

## Requirements

Install the required Python libraries:

```bash
pip install requests beautifulsoup4 google-generativeai
