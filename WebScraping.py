# Here we introduce web scraping, which --in short-- means acquiring
# data from a website(s) html and passing it to a algorithm that will
# perform the analysis for sentiment.

# Importing BeautifulSoup lib.
from bs4 import BeautifulSoup
from textblob import TextBlob

#for colored text
from termcolor import colored

# To read the html file.
html_file = open('index.html', 'r')
page = html_file.read()

# Creating an instance of BeautifulSoup to
# parse the document.
soup = BeautifulSoup(page, 'html.parser')

# To search for all the P tags in the .html .
reviews = soup.find_all('p')

print("Here are the seller reviews...\n")

# ---------------- Sentiment analysis portion of the code below. ------------------------

positiveCount, negativeCount = 0, 0

# Loop will print every review and its respective sentimentStr value
# for each review with tag <p>, and will count the amounts for each.
for p in reviews:
    text = p.get_text()
    sentiment = TextBlob(text).sentiment.polarity
    sentimentStr = " "

    # if <p> tag is empty pass to next <p>.
    if len(text) == 0:
        pass
    else:
        if sentiment >= 0.1:
            sentimentStr = colored("+", "green")
            positiveCount += 1

        else:
            sentimentStr = colored("-", "red")
            negativeCount += 1

        print(sentimentStr, p.get_text())


print("\nTotal positive reviews: ", colored(positiveCount, "green"))
print("Total negative reviews: ", colored(negativeCount, "red"))
