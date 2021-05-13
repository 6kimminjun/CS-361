from bs4 import BeautifulSoup
import requests
import urllib.request

# Function to grab the image from the right hand side of the wiki-page (Normally called the "infobox")
def getImagefromInfoBox(monsterName):

    # Initialize a count to 0 (used for naming convention of consecutive images)
    count = 0

    # Create an empty array to hold all the image URL links that the image scraper will generate
    imageURL = []

    # Use the requests module to call on the specified monster's wiki-article URL
    httpCall = requests.get('https://monsterhunterworld.wiki.fextralife.com/{0}'.format(monsterName))

    # Use the BeautifulSoup module to store the HTML response into a variable
    httpContent = BeautifulSoup(httpCall.content, features="html.parser")

    # Specify and select the infobox's image sources within the wikipedia page
    httpImages = httpContent.select('div.infobox table.wiki_table img[src]')

    # Loop through all images inside the infobox
    for image in httpImages:

        # Add on the image's pathname unto the wiki-page
        completeURL = "https://monsterhunterworld.wiki.fextralife.com/" + image['src']

        # Store this image's complete URL into the declared array "imageURL"
        imageURL.append(completeURL)

        # Open this image's URL link with the urllib.request module
        resource = urllib.request.urlopen(completeURL)

        # Create a new file with the specified naming convention (i.e. Monster00.jpg, Monster01.jpg, Monster02.jpg, etc)
        output = open("{0}0{1}.jpg".format(monsterName, count),"wb")

        # Write the image into the newly created file
        output.write(resource.read())

        # Make sure to close the new file
        output.close()

        # Increment the count of images being downloaded
        count += 1

    # print(imageURL)

# Example use of the image scraper function
getImagefromInfoBox("Fatalis")