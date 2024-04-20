from bs4 import BeautifulSoup
import pandas as pd

# Read the content from the saved file
with open("hanna_all_books.csv", "r") as file:
    html_content = file.read()
