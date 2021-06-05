from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from io import BytesIO
import urllib.request
import requests
from bs4 import BeautifulSoup

class mainApp(Tk):

    def __init__(self, *args, **kwargs):

        # Initialize the parent class variables (i.e. set the window size, window's title, etc)
        Tk.__init__(self, *args, **kwargs)
        self.title("MHW | Author: Min Kim")               # Set the title for the window
        self.geometry('800x800')                          # Set the size of the window
        self.resizable(False, False)                      # Prevent the window from being re-sized
        self.frames = {}                                  # Create an empty dictionary to hold frames
        self.appData = {"name": StringVar()}             # Store the user's input into the controller's dictionary
        self.enemyType = []
        self.species = []
        self.elements = []
        self.ailments = []
        self.weakness = []
        self.resistances = []
        self.addInfo = ''

        # Initialize the Frame() function
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        for F in (StartPage, StartPageJA, PageOne, PageOneJA, PageTwo, PageTwoJA):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.showFrame(StartPage)

    # Function used to raise/show the page we've specified
    def showFrame(self, page):
        frame = self.frames[page]
        frame.tkraise()

    # Function used to validate and save the user's input
    # If the user has entered an incorrect monster's name, then an error message will be displayed
    def saveUserInput(self, input, translation):
        found = 0
        userInput = input.get()
        self.appData["name"] = userInput
        if translation == "en":
            if self.appData["name"] == "Fatalis":
                 found += 1
                 self.showFrame(PageOne)
            if found != 1:
                messagebox.showwarning("Uh Oh!",
                                       "Sorry!\nWe were unable to find any information on this monster!\n"
                                       "Check your spelling and please try again!")
                return
        if translation == "ja":
            if self.appData["name"] == "Fatalis":
                found += 1
                self.showFrame(PageOneJA)
            if found != 1:
                stringToTranslate = "Sorry!\nWe were unable to find any information on this monster!\n" \
                                    "Check your spelling and please try again!"
                messagebox.showwarning(self.translator("Uh Oh!"), (self.translator(stringToTranslate)))
                return

    # Function that makes a GET request
    # Function that parses the data and updates the mainApp dictionary
    def scrapeWikiInfo(self, monsterName):
        array = []
        array2 = []
        array3 = []
        array4 = []
        array5 = []
        array6 = []
        array7 = []
        array8 = []
        URL = "https://monsterhunterworld.wiki.fextralife.com/{0}".format(monsterName)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find('tbody').get_text()
        array.append(content)
        new_array = array[0].replace("\n", " ").split()

        for item in new_array:
            if item == "Enemy":
                break
            array2.append(item)

        for item in new_array:
            if item == "Species":
                break
            array3.append(item)
            for entry in array3:
                if entry == "Type":
                    break
                array3.remove(item)
        self.enemyType = array3
        self.enemyType.pop(0)

        for item in new_array:
            if item == "Elements":
                break
            array4.append(item)
            for entry in array4:
                if entry == "Species":
                    break
                array4.remove(item)
        self.species = array4
        self.species.pop(0)

        for item in new_array:
            if item == "Ailments":
                break
            array5.append(item)
            for entry in array5:
                if entry == "Elements":
                    break
                array5.remove(item)
        self.elements = array5
        self.elements.pop(0)

        for item in new_array:
            if item == "Weakness":
                break
            array6.append(item)
            for entry in array6:
                if entry == "Ailments":
                    break
                array6.remove(item)
        self.ailments = array6
        self.ailments.pop(0)

        for item in new_array:
            if item == "Resistances":
                break
            array7.append(item)
            for entry in array7:
                if entry == "Weakness":
                    break
                array7.remove(item)
        self.weakness = array7
        self.weakness.pop(0)

        for item in new_array:
            if item == "Location(s)":
                break
            if item =="Locations":
                break
            array8.append(item)
            for entry in array8:
                if entry == "Resistances":
                    break
                array8.remove(item)
        self.resistances = array8
        self.resistances.pop(0)

    # Function that uses a microservice to translate a given string into the desired language
    def translator(self, string):
        json = {'word':string, 'cur':'en', 'dest':'ja'}
        url = 'http://flip1.engr.oregonstate.edu:1928/'
        response = requests.post(url, json=json)
        translation = response.text
        return translation

    # Function used to scrape the Wiki-article for the monster's history & folklore
    def scrapeWikiInfoMore(self, monsterName):
        array = []
        URL = "https://monsterhunterworld.wiki.fextralife.com/{0}".format(monsterName)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        content = soup.find('blockquote').get_text()
        array.append(content)
        new_array = array[0].replace("\n", " ")
        self.addInfo = new_array

    # Function used to display the different page's help message box
    def helpBox(self, helpNo):
        if helpNo == 1:
            messagebox.showinfo("Understanding the Start Page",
                                "Tips: \n\nWhen entering a monster's name, be sure that the spelling is correct."
                                "\n\nThe translation buttons below allow the user to swap between English and Japanese"
                                " translations.")
            return
        if helpNo == 2:
            messagebox.showinfo(self.translator("Understanding the Start Page"),
                                self.translator("Tips: \n\nWhen entering a monster's name, be sure that the spelling "
                                                "is correct.\n\nThe translation buttons below allow the user to swap "
                                                "between English and Japanese translations."))
            return
        if helpNo == 3:
            messagebox.showinfo("Understanding the Result Page #1",
                                "Tips: \n\nThe user can return to the main menu to search for another monster by "
                                "clicking on the 'Return to Homepage' button.\n\nThe user can find out the history"
                                " & folklore of the searched monster by clicking on the 'Click for additional info.' "
                                "button.\n\nThe translation buttons below allow the user to swap between English and "
                                "Japanese translations.")
            return
        if helpNo == 4:
            messagebox.showinfo(self.translator("Understanding the Result Page #1"),
                                self.translator("Tips: \n\nThe user can return to the main menu to search for another "
                                                "monster by clicking on the 'Return to Homepage' button.\n\nThe user "
                                                "can find out the history & folklore of the searched monster by "
                                                "clicking on the 'Click for additional info.' button.\n\nThe "
                                                "translation buttons below allow the user to swap between English "
                                                "and Japanese translations."))
            return
        if helpNo == 5:
            messagebox.showinfo("Understanding the Result Page #2",
                                "Tips: \n\nThe user can return to the main menu to search for another monster by "
                                "clicking on the 'Return to Homepage' button.\n\nThe user can go back to the Results "
                                "Page #1 by clicking on the 'Click for previous info.' button.\n\nThe translation "
                                "buttons below allow the user to swap between English and Japanese translations.")
            return
        if helpNo == 6:
            messagebox.showinfo(self.translator("Understanding the Result Page #2"),
                                self.translator("Tips: \n\nThe user can return to the main menu to search for another "
                                                "monster by clicking on the 'Return to Homepage' button.\n\nThe user "
                                                "can go back to the Results Page #1 by clicking on the 'Click for "
                                                "previous info.' button.\n\nThe translation buttons below allow the "
                                                "user to swap between English and Japanese translations."))
            return


class StartPage(Frame):

    def __init__(self, parent, controller):

        # Initialize the child frame with the parent's
        Frame.__init__(self, parent)
        self.controller = controller

        # Set the title of the software
        title = Label(self, text="The Hunter's\nHandbook", width=25, height=3, font=("Arial Bold", 40))
        title.grid(column=5, row=0)

        # Create a canvas and upload an image to use below the title of the software
        img = ImageTk.PhotoImage(Image.open("Logo4.jpg"))
        canvas = Canvas(self, width = 250, height = 250)
        canvas.image = img
        canvas.create_image(125, 125, anchor="center", image=img)
        canvas.grid(column=5, row=1)

        # Create a divider to provide space between the title image and the input prompt
        divider1 = Label(self, width=10, height=2)
        divider1.grid(column=5, row=2)

        # Set the prompt for getting an input from the user
        inputPrompt = Label(self, text="Enter a monster's name")
        inputPrompt.grid(column=5, row=3)

        # Create an input line for the user
        input = Entry(self, textvariable=self.controller.appData["name"], width=40)
        input.grid(column=5, row=4)

        # Create the search button for the user's input
        searchButton = Button(self, text="Search", bd=8, bg="lightblue", fg="black",
                              font=("Arial Bold", 15), command=lambda: controller.saveUserInput(input, "en"))
        searchButton.grid(column=5, row=5, pady=4)

        # Create a divider to provide space between the Search button and Translation buttons
        divider2 = Label(self, width=10, height=4)
        divider2.grid(column=5, row=6)

        # Create the English translation button
        englishButton = Button(self, text="English Translation", bd=3, bg="lightblue", fg="black",
                               font=("Arial Bold", 10), command=lambda: controller.showFrame(StartPage))
        englishButton.grid(column=5, row=10, pady=5, ipadx=8)

        # Create the Japanese translation button
        japaneseButton = Button(self, text="日本語 Translation", bd=3, bg="lightblue", fg="black",
                                font=("Arial Bold", 10), command=lambda: controller.showFrame(StartPageJA))
        japaneseButton.grid(column=5, row=11, ipadx=12)

        # Create the Help button
        helpButton = Button(self, text="?", bd=3, bg="lavender", fg="black",
                            font=("Arial Bold", 15), command=lambda: controller.helpBox(1))
        helpButton.grid(column=5, row=12, pady=10, ipadx=5)

class StartPageJA(Frame):

    def __init__(self, parent, controller):

        # Initialize the child frame with the parent's
        Frame.__init__(self, parent)

        self.controller = controller

        # Set the title of the software
        title = Label(self, text=self.controller.translator("The Hunter's\nHandbook"),
                      width=25, height=3, font=("Arial Bold", 40))
        title.grid(column=5, row=0)

        # Create a canvas and upload an image to use below the title of the software
        img = ImageTk.PhotoImage(Image.open("Logo4.jpg"))
        canvas = Canvas(self, width = 250, height = 250)
        canvas.image = img
        canvas.create_image(125, 125, anchor="center", image=img)
        canvas.grid(column=5, row=1)

        # Create a divider to provide space between the title image and the input prompt
        divider1 = Label(self, width=10, height=2)
        divider1.grid(column=5, row=2)

        # Set the prompt for getting an input from the user
        inputPrompt = Label(self, text=self.controller.translator("Enter a monster's name"))
        inputPrompt.grid(column=5, row=3)

        # Create an input line for the user
        input = Entry(self, textvariable=self.controller.appData["name"], width=40)
        input.grid(column=5, row=4)

        # Create the search button for the user's input
        searchButton = Button(self, text=self.controller.translator("Search"), bd=8, bg="lightblue", fg="black",
                              font=("Arial Bold", 15), command=lambda: controller.saveUserInput(input, "ja"))
        searchButton.grid(column=5, row=5, pady=4)

        # Create a divider to provide space between the Search button and Translation buttons
        divider2 = Label(self, width=10, height=4)
        divider2.grid(column=5, row=6)

        # Create the English translation button
        englishButton = Button(self, text="English Translation", bd=3, bg="lightblue", fg="black",
                               font=("Arial Bold", 10), command=lambda: controller.showFrame(StartPage))
        englishButton.grid(column=5, row=10, pady=5, ipadx=8)

        # Create the Japanese translation button
        japaneseButton = Button(self, text="日本語 Translation", bd=3, bg="lightblue", fg="black",
                                font=("Arial Bold", 10), command=lambda: controller.showFrame(StartPageJA))
        japaneseButton.grid(column=5, row=11, ipadx=12)

        # Create the Help button
        helpButton = Button(self, text="?", bd=3, bg="lavender", fg="black",
                            font=("Arial Bold", 15), command=lambda: controller.helpBox(2))
        helpButton.grid(column=5, row=12, pady=10, ipadx=5)

class PageOne(Frame):

    def __init__(self, parent, controller):

        # Initialize the child frame with the parent's
        Frame.__init__(self, parent)

        self.controller = controller

        try:
            name = "Fatalis"
            controller.scrapeWikiInfo(name)
        except:
            pass

        # Display the name of the searched monster
        displayName = Label(self, textvariable=self.controller.appData["name"], height=2,
                            font=("Times New Roman Bold", 40))
        displayName.grid(column=0, row=0, padx=20, sticky="W")

        # Create the return to Homepage button
        homepageButton = Button(self, text="Return to \nHomepage", bd=10, bg="pink", fg="black",
                                font=("Impact", 20), command=lambda: [controller.showFrame(StartPage)])
        homepageButton.grid(column=0, row=0, ipadx=12, padx=36, sticky="SE")

        # Display the searched monster's scraped image
        try:
            r = requests.get("http://flip1.engr.oregonstate.edu:6163/?query=Fatalis")
            URL = r.text
            u = urllib.request.urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo = ImageTk.PhotoImage(im)

            canvas = Canvas(self, width = 250, height = 250)
            canvas.image = photo
            canvas.create_image(125, 125, anchor="center", image=photo)
            canvas.grid(column=0, row=1, padx=50, sticky="W")
        except:
            pass

        # Create a divider to provide space between the monster's image and the body text
        divider1 = Label(self, width=10, height=2)
        divider1.grid(column=0, row=2)

        # Create the additional info button
        additionalInfoButton = Button(self, text="Click for additional info.", bd=3, bg="lightblue", fg="black",
                                      font=("Arial Bold", 10), command=lambda: [controller.showFrame(PageTwo)])
        additionalInfoButton.grid(column=0, row=2, ipadx=12, padx=50, sticky="E")

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=3, sticky="W")

        # Display the body text (Enemy type)
        enemyTypeHeader = Message(self, text="Enemy Type: ", bd=4, relief = RIDGE, width=500,
                                  font=("Times New Roman Bold", 15))
        enemyTypeHeader.grid(column=0, row=4, padx=15, sticky="W")
        enemyTypeInfo = Message(self, text=" ".join(self.controller.enemyType), bd=4, width=500,
                                font=("Times New Roman", 15))
        enemyTypeInfo.grid(column=0, row=4, padx=200)

        # Display the body text (Species)
        speciesHeader = Message(self, text="Species: ", bd=4, relief = RIDGE, width=500,
                                font=("Times New Roman Bold", 15))
        speciesHeader.grid(column=0, row=5, padx=15, sticky="W")
        speciesInfo = Message(self, text=" ".join(self.controller.species), bd=4, width=500,
                              font=("Times New Roman", 15))
        speciesInfo.grid(column=0, row=5, padx=200)

        # Display the body text (Elements)
        elementsHeader = Message(self, text="Elements: ", bd=4, relief = RIDGE, width=500,
                                 font=("Times New Roman Bold", 15))
        elementsHeader.grid(column=0, row=6, padx=15, sticky="W")
        elementsInfo = Message(self, text=" ".join(self.controller.elements), bd=4, width=500,
                               font=("Times New Roman", 15))
        elementsInfo.grid(column=0, row=6, padx=200)

        # Display the body text (Ailments)
        ailmentsHeader = Message(self, text="Ailments: ", bd=4, relief = RIDGE, width=500,
                                 font=("Times New Roman Bold", 15))
        ailmentsHeader.grid(column=0, row=7, padx=15, sticky="W")
        ailmentsInfo = Message(self, text=" ".join(self.controller.ailments), bd=4, width=500,
                               font=("Times New Roman", 15))
        ailmentsInfo.grid(column=0, row=7, padx=200)

        # Display the body text (Weaknesses)
        weaknessHeader = Message(self, text="Weakness: ", bd=4, relief = RIDGE, width=500,
                                 font=("Times New Roman Bold", 15))
        weaknessHeader.grid(column=0, row=8, padx=15, sticky="W")
        weaknessInfo = Message(self, text=" ".join(self.controller.weakness), bd=4, width=500,
                               font=("Times New Roman", 15))
        weaknessInfo.grid(column=0, row=8, padx=200)

        # Display the body text (Resistances)
        resistancesHeader = Message(self, text="Resistances: ", bd=4, relief = RIDGE, width=500,
                                    font=("Times New Roman Bold", 15))
        resistancesHeader.grid(column=0, row=9, padx=15, sticky="W")
        resistancesInfo = Message(self, text=" ".join(self.controller.resistances), bd=4, width=500,
                                  font=("Times New Roman", 15))
        resistancesInfo.grid(column=0, row=9, padx=200)

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=10, sticky="W")

        # Create a divider to provide space between the body info and Translation buttons
        divider1 = Label(self, width=10, height=2)
        divider1.grid(column=0, row=11)

        # Create the English translation button
        englishButton = Button(self, text="English Translation", bd=3, bg="lightblue", fg="black",
                               font=("Arial Bold", 10), command=lambda: controller.showFrame(PageOne))
        englishButton.grid(column=0, row=12, pady=5, ipadx=8)

        # Create the Japanese translation button
        japaneseButton = Button(self, text="日本語 Translation", bd=3, bg="lightblue", fg="black",
                                font=("Arial Bold", 10), command=lambda: controller.showFrame(PageOneJA))
        japaneseButton.grid(column=0, row=13, ipadx=12)

        # Create the Help button
        helpButton = Button(self, text="?", bd=3, bg="lavender", fg="black",
                            font=("Arial Bold", 15), command=lambda: controller.helpBox(3))
        helpButton.grid(column=0, row=13, padx=10, ipadx=5, sticky="W")

class PageOneJA(Frame):

    def __init__(self, parent, controller):

        # Initialize the child frame with the parent's
        Frame.__init__(self, parent)

        self.controller = controller

        try:
            name = "Fatalis"
            controller.scrapeWikiInfo(name)
        except:
            pass

        # Display the name of the searched monster
        displayName = Label(self, textvariable=self.controller.appData["name"], height=2,
                            font=("Times New Roman Bold", 40))
        displayName.grid(column=0, row=0, padx=20, sticky="W")

        # Create the return to Homepage button
        homepageButton = Button(self, text=self.controller.translator("Return to \nHomepage"), bd=10, bg="pink",
                                fg="black", font=("Impact", 20), command=lambda: [controller.showFrame(StartPageJA)])
        homepageButton.grid(column=0, row=0, ipadx=12, padx=36, sticky="SE")

        # Display the searched monster's scraped image
        try:
            r = requests.get("http://flip1.engr.oregonstate.edu:6163/?query=Fatalis")
            URL = r.text
            u = urllib.request.urlopen(URL)
            raw_data = u.read()
            u.close()

            im = Image.open(BytesIO(raw_data))
            photo = ImageTk.PhotoImage(im)

            canvas = Canvas(self, width = 250, height = 250)
            canvas.image = photo
            canvas.create_image(125, 125, anchor="center", image=photo)
            canvas.grid(column=0, row=1, padx=50, sticky="W")
        except:
            pass

        # Create a divider to provide space between the monster's image and the body text
        divider1 = Label(self, width=10, height=2)
        divider1.grid(column=0, row=2)

        # Create the additional info button
        additionalInfoButton = Button(self, text=self.controller.translator("Click for additional info."),
                                      bd=3, bg="lightblue", fg="black", font=("Arial Bold", 10),
                                      command=lambda: [controller.showFrame(PageTwoJA)])
        additionalInfoButton.grid(column=0, row=2, ipadx=12, padx=50, sticky="E")

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=3, sticky="W")

        # Display the body text (Enemy type)
        enemyTypeHeader = Message(self, text=self.controller.translator("Enemy Type: "), bd=4, relief = RIDGE,
                                  width=500, font=("Times New Roman Bold", 15))
        enemyTypeHeader.grid(column=0, row=4, padx=15, sticky="W")
        enemyTypeInfo = Message(self, text=self.controller.translator(" ".join(self.controller.enemyType)),
                                bd=4, width=500, font=("Times New Roman", 15))
        enemyTypeInfo.grid(column=0, row=4, padx=200)

        # Display the body text (Species)
        speciesHeader = Message(self, text=self.controller.translator("Species: "), bd=4, relief = RIDGE,
                                width=500, font=("Times New Roman Bold", 15))
        speciesHeader.grid(column=0, row=5, padx=15, sticky="W")
        speciesInfo = Message(self, text=self.controller.translator(" ".join(self.controller.species)),
                              bd=4, width=500, font=("Times New Roman", 15))
        speciesInfo.grid(column=0, row=5, padx=200)

        # Display the body text (Elements)
        elementsHeader = Message(self, text=self.controller.translator("Elements: "), bd=4, relief = RIDGE,
                                 width=500, font=("Times New Roman Bold", 15))
        elementsHeader.grid(column=0, row=6, padx=15, sticky="W")
        elementsInfo = Message(self, text=self.controller.translator(" ".join(self.controller.elements)),
                               bd=4, width=500, font=("Times New Roman", 15))
        elementsInfo.grid(column=0, row=6, padx=200)

        # Display the body text (Ailments)
        ailmentsHeader = Message(self, text=self.controller.translator("Ailments: "), bd=4, relief = RIDGE,
                                 width=500, font=("Times New Roman Bold", 15))
        ailmentsHeader.grid(column=0, row=7, padx=15, sticky="W")
        ailmentsInfo = Message(self, text=self.controller.translator(" ".join(self.controller.ailments)),
                               bd=4, width=500, font=("Times New Roman", 15))
        ailmentsInfo.grid(column=0, row=7, padx=200)

        # Display the body text (Weaknesses)
        weaknessHeader = Message(self, text=self.controller.translator("Weakness: "), bd=4, relief = RIDGE,
                                 width=500, font=("Times New Roman Bold", 15))
        weaknessHeader.grid(column=0, row=8, padx=15, sticky="W")
        weaknessInfo = Message(self, text=self.controller.translator(" ".join(self.controller.weakness)),
                               bd=4, width=500, font=("Times New Roman", 15))
        weaknessInfo.grid(column=0, row=8, padx=200)

        # Display the body text (Resistances)
        resistancesHeader = Message(self, text=self.controller.translator("Resistances: "), bd=4, relief = RIDGE,
                                    width=500, font=("Times New Roman Bold", 15))
        resistancesHeader.grid(column=0, row=9, padx=15, sticky="W")
        resistancesInfo = Message(self, text=self.controller.translator(" ".join(self.controller.resistances)),
                                  bd=4, width=500, font=("Times New Roman", 15))
        resistancesInfo.grid(column=0, row=9, padx=200)

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=10, sticky="W")

        # Create a divider to provide space between the body info and Translation buttons
        divider1 = Label(self, width=10, height=2)
        divider1.grid(column=0, row=11)

        # Create the English translation button
        englishButton = Button(self, text="English Translation", bd=3, bg="lightblue", fg="black",
                               font=("Arial Bold", 10), command=lambda: controller.showFrame(PageOne))
        englishButton.grid(column=0, row=12, pady=5, ipadx=8)

        # Create the Japanese translation button
        japaneseButton = Button(self, text="日本語 Translation", bd=3, bg="lightblue", fg="black",
                                font=("Arial Bold", 10), command=lambda: controller.showFrame(PageOneJA))
        japaneseButton.grid(column=0, row=13, ipadx=12)

        # Create the Help button
        helpButton = Button(self, text="?", bd=3, bg="lavender", fg="black",
                            font=("Arial Bold", 15), command=lambda: controller.helpBox(4))
        helpButton.grid(column=0, row=13, padx=10, ipadx=5, sticky="W")

class PageTwo(Frame):

    def __init__(self, parent, controller):

        self.controller = controller

        # Initialize the child frame using the parent's
        Frame.__init__(self, parent)

        try:
            name = "Fatalis"
            controller.scrapeWikiInfoMore(name)
        except:
            pass

        # Display the name of the searched monster
        displayName = Label(self, textvariable=self.controller.appData["name"], height=2,
                            font=("Times New Roman Bold", 40))
        displayName.grid(column=0, row=0, padx=20, sticky="W")

        # Create the return to Homepage button
        homepageButton = Button(self, text="Return to \nHomepage", bd=10, bg="pink", fg="black",
                                font=("Impact", 20), command=lambda: controller.showFrame(StartPage))
        homepageButton.grid(column=0, row=0, ipadx=12, padx=36, sticky="SE")

        # Create the return to previous information button
        previousButton = Button(self, text="Click for previous info.", bd=3, bg="pink", fg="black",
                                font=("Arial Bold", 10), command=lambda: self.controller.showFrame(PageOne))
        previousButton.grid(column=0, row=1, ipadx=10, padx=7, pady=5, sticky="SW")

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=3, sticky="W")

        # Display the body text (History & Folklore)
        historyHeader = Message(self, text="History and Folklore: ", bd=4, relief = RIDGE, width=500,
                                font=("Times New Roman Bold", 15))
        historyHeader.grid(column=0, row=4, padx=15, sticky="W")
        historyInfo = Message(self, text=self.controller.addInfo, bd=4, width=500, font=("Times New Roman", 20))
        historyInfo.grid(column=0, row=5)

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=10, sticky="W")

        # Create a divider to provide space between the body info and Translation buttons
        divider1 = Label(self, width=10, height=2)
        divider1.grid(column=0, row=11)

        # Create the English translation button
        englishButton = Button(self, text="English Translation", bd=3, bg="lightblue", fg="black",
                               font=("Arial Bold", 10), command=lambda: controller.showFrame(PageTwo))
        englishButton.grid(column=0, row=12, pady=5, ipadx=8)

        # Create the Japanese translation button
        japaneseButton = Button(self, text="日本語 Translation", bd=3, bg="lightblue", fg="black",
                                font=("Arial Bold", 10), command=lambda: controller.showFrame(PageTwoJA))
        japaneseButton.grid(column=0, row=13, ipadx=12)

        # Create the Help button
        helpButton = Button(self, text="?", bd=3, bg="lavender", fg="black",
                            font=("Arial Bold", 15), command=lambda: controller.helpBox(5))
        helpButton.grid(column=0, row=14, pady=10, ipadx=5)

class PageTwoJA(Frame):

    def __init__(self, parent, controller):

        self.controller = controller

        # Initialize the child frame using the parent's
        Frame.__init__(self, parent)

        try:
            name = "Fatalis"
            controller.scrapeWikiInfoMore(name)
        except:
            pass

        # Display the name of the searched monster
        displayName = Label(self, textvariable=self.controller.appData["name"], height=2,
                            font=("Times New Roman Bold", 40))
        displayName.grid(column=0, row=0, padx=20, sticky="W")

        # Create the return to Homepage button
        homepageButton = Button(self, text=self.controller.translator("Return to \nHomepage"),
                                bd=10, bg="pink", fg="black", font=("Impact", 20),
                                command=lambda: controller.showFrame(StartPageJA))
        homepageButton.grid(column=0, row=0, ipadx=12, padx=36, sticky="SE")

        # Create the return to previous information button
        previousButton = Button(self, text=self.controller.translator("Click for previous info."),
                                bd=3, bg="pink", fg="black", font=("Arial Bold", 10),
                                command=lambda: self.controller.showFrame(PageOneJA))
        previousButton.grid(column=0, row=1, ipadx=10, padx=7, pady=5, sticky="SW")

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=3, sticky="W")

        # Display the body text (History & Folklore)
        historyHeader = Message(self, text=self.controller.translator("History and Folklore: "),
                                bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        historyHeader.grid(column=0, row=4, padx=15, sticky="W")
        historyInfo = Message(self, text=self.controller.translator(self.controller.addInfo), bd=4, width=500,
                              font=("Times New Roman", 20))
        historyInfo.grid(column=0, row=5)

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=10, sticky="W")

        # Create a divider to provide space between the body info and Translation buttons
        divider1 = Label(self, width=10, height=2)
        divider1.grid(column=0, row=11)

        # Create the English translation button
        englishButton = Button(self, text="English Translation", bd=3, bg="lightblue", fg="black",
                               font=("Arial Bold", 10), command=lambda: controller.showFrame(PageTwo))
        englishButton.grid(column=0, row=12, pady=5, ipadx=8)

        # Create the Japanese translation button
        japaneseButton = Button(self, text="日本語 Translation", bd=3, bg="lightblue", fg="black",
                                font=("Arial Bold", 10), command=lambda: controller.showFrame(PageTwoJA))
        japaneseButton.grid(column=0, row=13, ipadx=12)

        # Create the Help button
        helpButton = Button(self, text="?", bd=3, bg="lavender", fg="black",
                            font=("Arial Bold", 15), command=lambda: controller.helpBox(6))
        helpButton.grid(column=0, row=14, pady=10, ipadx=5)

# Used to run the software until forcefully exited
window = mainApp()
window.mainloop()