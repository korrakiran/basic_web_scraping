# 🕸️ Webpage Text Extractor & Summarizer using Gemini Pro

This Python project extracts visible text from any webpage, removes unnecessary HTML elements (like scripts, styles, headers, etc.), and then summarizes the cleaned content using Google’s Gemini Pro (via the `google-generativeai` API).

---

## 📂 Files Included

- `output.html` → Raw HTML content from the webpage  
- `clean_text.txt` → Cleaned, readable text extracted from HTML  
- `output_from_genai.txt` → AI-generated summary of the cleaned text  
- `README.md` → Project documentation

---

## 🧰 Requirements

Install the required Python libraries:

```bash
pip install requests beautifulsoup4 google-generativeai
