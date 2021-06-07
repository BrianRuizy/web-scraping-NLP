# Here is a python script that allows you to scrape a webpage and perform automated sentiment analysis.
#It is a modified version of Brian Ruizy's python script found here: https://github.com/BrianRuizy/web-scraping-NLP
#Instead of parsing an offline webpage, this script asks you programmatically for a link and automatically downloads and parses it.
#The end product is a printed out sentiment analysis and a piechart that automatically breaks-down positive and negative language graphically.
#The hope is to work with Brian Ruizy in order to further develop this project in a Flask WebPage.
#The goal is users will be able to perform sophisticated sentiment analysis of any webpage from their phone.

# Importing necessary libraries.
from bs4 import BeautifulSoup
from textblob import TextBlob
from termcolor import colored
import requests
from matplotlib import pyplot as plt
import numpy as np

# To scrape specific webpage and make it parse-able.
link = input("Insert link here: ")
html_file2 = requests.get(link)
html_file = html_file2.text

# Use BeautifulSoup to parse the html document you just scraped.
soup = BeautifulSoup(html_file, 'html.parser')

# Set boundaries on the text scraped and parsed from HTML. The algorithm will use only textual data found between HTML <p> tags.
reviews = soup.find_all('p')

# Set up sentiment analysis framework by defining the variables.
positiveCount, negativeCount = 0, 0

# For textual data in each <p> tag, a review will be formed for each "paragraph's" overall sentiment. It will add 1 to the overall piechart for each paragraph in two categories of either positive or negative.
for p in reviews:
    text = p.get_text()
    sentiment = TextBlob(text).sentiment.polarity
    sentimentStr = " "

    # if <p> tag is empty pass to next <p>.
    if len(text) == 0:
        pass
    else:
        if sentiment >= 0:
            sentimentStr = colored("+", "green")
            positiveCount += 1

        else:
            sentimentStr = colored("-", "red")
            negativeCount += 1
            
        print(sentimentStr, p.get_text())
            
print("\nTotal positive reviews: ", colored(positiveCount, "green"))
print("Total negative reviews: ", colored(negativeCount, "red"))

# Creating the pie chart plot.
data = [positiveCount, negativeCount]
labels = ["Positive language", "Negative language"]
fig, ax = plt.subplots(figsize =(10, 7))
plt.pie(data, labels = labels)

# Adding title to pie chart plot.
ax.set_title("Outrage Evaluator Results")

# Showing the pie chart plot.
plt.show()



# End of script. Should automatically open piechart in new window.
