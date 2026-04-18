# Web Scraping Project 
# Website Title & Headings Scraper 

import requests
from bs4 import BeautifulSoup

# Website URL to scrape
url = "https://techcrunch.com/category/artificial-intelligence/"  

# Get website content
response = requests.get(url) 

# Parse HTML 
soup = BeautifulSoup(response.text, "html.parser")  

# Get page Title 
title = soup.titletext

# Get all H1 Headings 
headings = soup.find_all("h1") 

# Save data to file 
with open("scrapped_data.txt", "w") as file: 
    file.write("Website Title:\n") 
    file.write(f"{title}" + "\n\n") 

    file.write("H1 Headings:\n") 
    for h in headings:
        file.write(h.text + "\n")

print("✅ Data scraped and saved successfully!") 



