# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import datetime

# URL of the website to scrape
url = "https://pixelford.com/blog/"

# Generate a random number to use as user-agent header (optional but recommended)
import random
random_number = random.randint(1, 99999999999)

# Send a request to the website with a user-agent header
response = requests.get(url, headers={"user-agent": f"{random_number}"})

# Get the HTML content of the response
html = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Find all the blog articles on the page
blogs = soup.find_all("article", class_="type-post")

# Iterate over each blog article
for blog in blogs:
    # Extract the title of the blog article
    title = blog.find("a", class_="entry-title-link").get_text()

    # Extract the datetime string of the blog article
    blog_datetime_string = blog.find("time", class_="entry-time").get("datetime")
    
    # Convert the datetime string to a datetime object
    blog_datetime = datetime.datetime.fromisoformat(blog_datetime_string)
    
    # Format the datetime object into a more readable format
    pretty_date = blog_datetime.strftime("%b %d %Y")
    
    # Print the formatted date and the title of the blog article
    print(f"{pretty_date} - {title}")