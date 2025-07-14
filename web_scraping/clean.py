from bs4 import BeautifulSoup

# Load the HTML file
with open("output.html", "r", encoding="utf-8") as f:
    html = f.read()

# Parse the HTML content
soup = BeautifulSoup(html, "html.parser")

# Remove scripts and style elements
for tag in soup(["script", "style", "noscript", "header", "footer", "nav", "aside"]):
    tag.decompose()

# Extract visible text
text = soup.get_text(separator="\n", strip=True)

# Optional: Save to a text file
with open("clean_text.txt", "w", encoding="utf-8") as f:
    f.write(text)

print("Extracted clean text saved to 'clean_text.txt'")
