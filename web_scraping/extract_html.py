
import requests
from bs4 import BeautifulSoup

# URL of the website you want to extract
url = "your webpage link"

# Send a GET request to the URL
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    html_content = response.text

    # Optionally parse the HTML (e.g., to extract only text or clean tags)
    soup = BeautifulSoup(html_content, "html.parser")

    # Save full HTML to a file
    with open("output.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    print("HTML content extracted and saved to 'output.html'")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
