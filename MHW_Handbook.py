from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

class mainApp(Tk):

    def __init__(self, *args, **kwargs):

        # Initialize the parent class variables (i.e. set the window size, window's title, etc)
        Tk.__init__(self, *args, **kwargs)
        self.title("MHW | Author: Min Kim")               # Set the title for the window
        self.geometry('800x800')                          # Set the size of the window
        self.resizable(False, False)                      # Prevent the window from being re-sized
        self.frames = {}                                  # Create an empty dictionary to hold frames

        # Initialize the Frame() function
        container = Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    # Function used to raise/show the page we've specified
    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class StartPage(Frame):

    def __init__(self, parent, controller):

        # Initialize the child frame with the parent's
        Frame.__init__(self, parent)

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
        input = Entry(self, width=40)
        input.grid(column=5, row=4)

        # Function used to display an error message to the user when monster name does not exist
        def clicked():
            messagebox.showwarning('Uh Oh!', 'Sorry!\nWe were unable to find any information on this monster!\nPlease try again!')

        # Create the search button for the user's input
        searchButton = Button(self, text="Search", bd=8, bg="lightblue", fg="black", font=("Arial Bold", 15), command=lambda: controller.show_frame(PageOne))
        searchButton.grid(column=5, row=5, pady=4)

        # Create a divider to provide space between the Search button and Translation buttons
        divider2 = Label(self, width=10, height=6)
        divider2.grid(column=5, row=6)

        # Create the English translation button
        englishButton = Button(self, text="English Translation", bd=3, bg="lightblue", fg="black", font=("Arial Bold", 10))
        englishButton.grid(column=5, row=10, pady=5, ipadx=8)

        # Create the Japanese translation button
        japaneseButton = Button(self, text="日本語 Translation", bd=3, bg="lightblue", fg="black", font=("Arial Bold", 10))
        japaneseButton.grid(column=5, row=11, ipadx=12)

class PageOne(Frame):

    def __init__(self, parent, controller):

        # Initialize the child frame with the parent's
        Frame.__init__(self, parent)

        # Display the name of the searched monster
        displayName = Label(self, text="Monster Name", height=2, font=("Times New Roman Bold", 40))
        displayName.grid(column=0, row=0, padx=20, sticky="W")

        # Create the return to Homepage button
        homepageButton = Button(self, text="Return to \nHomepage", bd=10, bg="pink", fg="black", font=("Impact", 20), command=lambda: controller.show_frame(StartPage))
        homepageButton.grid(column=0, row=0, ipadx=12, padx=75, sticky="SE")

        # Display the searched monster's scraped image
        titleImage = Label(self, text="Image Placeholder", fg="white", bg="black", width=40, height=15)
        titleImage.grid(column=0, row=1, padx=50, sticky="W")

        # Create a divider to provide space between the monster's image and the body text
        divider1 = Label(self, width=10, height=2)
        divider1.grid(column=0, row=2)

        # Create the additional info button
        additionalInfoButton = Button(self, text="Click for additional info.", bd=3, bg="lightblue", fg="black", font=("Arial Bold", 10), command=lambda: controller.show_frame(PageTwo))
        additionalInfoButton.grid(column=0, row=2, ipadx=12, padx=50, sticky="E")

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=3, sticky="W")

        # Display the body text (Enemy type)
        enemyTypeHeader = Message(self, text="Enemy Type: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        enemyTypeHeader.grid(column=0, row=4, padx=15, sticky="W")
        enemyTypeInfo = Message(self, text="Large Monsters", bd=4, width=500, font=("Times New Roman", 15))
        enemyTypeInfo.grid(column=0, row=4, padx=200)

        # Display the body text (Species)
        speciesHeader = Message(self, text="Species: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        speciesHeader.grid(column=0, row=5, padx=15, sticky="W")
        speciesInfo = Message(self, text="Elder Dragon", bd=4, width=500, font=("Times New Roman", 15))
        speciesInfo.grid(column=0, row=5, padx=200)

        # Display the body text (Elements)
        elementsHeader = Message(self, text="Elements: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        elementsHeader.grid(column=0, row=6, padx=15, sticky="W")
        elementsInfo = Message(self, text="Fire, Ice, Water, Thunder", bd=4, width=500, font=("Times New Roman", 15))
        elementsInfo.grid(column=0, row=6, padx=200)

        # Display the body text (Ailments)
        ailmentsHeader = Message(self, text="Ailments: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        ailmentsHeader.grid(column=0, row=7, padx=15, sticky="W")
        ailmentsInfo = Message(self, text="Fireblight, Waterblight, Dragonblight, Thunderblight", bd=4, width=500, font=("Times New Roman", 15))
        ailmentsInfo.grid(column=0, row=7, padx=200)

        # Display the body text (Weaknesses)
        weaknessHeader = Message(self, text="Weakness: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        weaknessHeader.grid(column=0, row=8, padx=15, sticky="W")
        weaknessInfo = Message(self, text="Dragon(3), Fire(2)", bd=4, width=500, font=("Times New Roman", 15))
        weaknessInfo.grid(column=0, row=8, padx=200)

        # Display the body text (Resistances)
        resistancesHeader = Message(self, text="Resistances: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        resistancesHeader.grid(column=0, row=9, padx=15, sticky="W")
        resistancesInfo = Message(self, text="Water(1), Thunder(1), Ice(1)", bd=4, width=500, font=("Times New Roman", 15))
        resistancesInfo.grid(column=0, row=9, padx=200)

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=10, sticky="W")

        # Create a divider to provide space between the body info and Translation buttons
        divider1 = Label(self, width=10, height=2)
        divider1.grid(column=0, row=11)

        # Create the English translation button
        englishButton = Button(self, text="English Translation", bd=3, bg="lightblue", fg="black", font=("Arial Bold", 10))
        englishButton.grid(column=0, row=12, pady=5, ipadx=8)

        # Create the Japanese translation button
        japaneseButton = Button(self, text="日本語 Translation", bd=3, bg="lightblue", fg="black", font=("Arial Bold", 10))
        japaneseButton.grid(column=0, row=13, ipadx=12)


class PageTwo(Frame):

    def __init__(self, parent, controller):

        # Initialize the child frame using the parent's
        Frame.__init__(self, parent)

        # Display the name of the searched monster
        displayName = Label(self, text="Monster Name", height=2, font=("Times New Roman Bold", 40))
        displayName.grid(column=0, row=0, padx=20, sticky="W")

        # Create the return to Homepage button
        homepageButton = Button(self, text="Return to \nHomepage", bd=10, bg="pink", fg="black", font=("Impact", 20), command=lambda: controller.show_frame(StartPage))
        homepageButton.grid(column=0, row=0, ipadx=12, padx=36, sticky="SE")

        # Create the return to previous information button
        homepageButton = Button(self, text="Click for previous info.", bd=3, bg="pink", fg="black", font=("Arial Bold", 10), command=lambda: controller.show_frame(PageOne))
        homepageButton.grid(column=0, row=1, ipadx=10, padx=7, pady=5, sticky="SW")

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=3, sticky="W")

        # Display the body text (Found In)
        foundInHeader = Message(self, text="Found in: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        foundInHeader.grid(column=0, row=4, padx=15, sticky="W")
        foundInInfo = Message(self, text="Castle Schrade", bd=4, width=500, font=("Times New Roman", 15))
        foundInInfo.grid(column=0, row=4, padx=200)

        # Display the body text (Target of Quests)
        questsHeader = Message(self, text="Target of Quests: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        questsHeader.grid(column=0, row=5, padx=15, sticky="W")
        questsInfo = Message(self, text="The Black Dragon, Fade to Black", bd=4, width=500, font=("Times New Roman", 15))
        questsInfo.grid(column=0, row=5, padx=200)

        # Display the body text (HP)
        healthHeader = Message(self, text="HP: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        healthHeader.grid(column=0, row=6, padx=15, sticky="W")
        healthInfo = Message(self, text="~66,000 Solo, 116k Duo, 171k Three or more", bd=4, width=500, font=("Times New Roman", 15))
        healthInfo.grid(column=0, row=6, padx=200)

        # Display the body text (Combat Info)
        combatHeader = Message(self, text="Combat Info: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        combatHeader.grid(column=0, row=7, padx=15, sticky="W")
        combatInfo = Message(self, text="The chest, wings, and head are breakable", bd=4, width=500, font=("Times New Roman", 15))
        combatInfo.grid(column=0, row=7, padx=200)

        # Display the body text (Recommended Skills)
        skillsHeader = Message(self, text="Recommended Skills: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        skillsHeader.grid(column=0, row=8, padx=15, sticky="W")
        skillsInfo = Message(self, text="Make sure to take Divine Blessing 5", bd=4, width=500, font=("Times New Roman", 15))
        skillsInfo.grid(column=0, row=8, padx=200)

        # Display the body text (Rewards)
        rewardsHeader = Message(self, text="Rewards: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        rewardsHeader.grid(column=0, row=9, padx=15, sticky="W")
        rewardsInfo = Message(self, text="Just a bunch of feystones", bd=4, width=500, font=("Times New Roman", 15))
        rewardsInfo.grid(column=0, row=9, padx=200)

        # Display the body text (Weapons & Armor)
        weaponArmorHeader = Message(self, text="Weapons & Armor: ", bd=4, relief = RIDGE, width=500, font=("Times New Roman Bold", 15))
        weaponArmorHeader.grid(column=0, row=9, padx=15, sticky="W")
        weaponArmorInfo = Message(self, text="Monster sword and shield, insect glaive, etc", bd=4, width=500, font=("Times New Roman", 15))
        weaponArmorInfo.grid(column=0, row=9, padx=200)

        # Draw a line to separate the body info and Translation buttons
        dividerLine = Canvas(self, width=795, height=2, bg="black")
        dividerLine.grid(column=0, row=10, sticky="W")

        # Create a divider to provide space between the body info and Translation buttons
        divider1 = Label(self, width=10, height=2)
        divider1.grid(column=0, row=11)

        # Create the English translation button
        englishButton = Button(self, text="English Translation", bd=3, bg="lightblue", fg="black", font=("Arial Bold", 10))
        englishButton.grid(column=0, row=12, pady=5, ipadx=8)

        # Create the Japanese translation button
        japaneseButton = Button(self, text="日本語 Translation", bd=3, bg="lightblue", fg="black", font=("Arial Bold", 10))
        japaneseButton.grid(column=0, row=13, ipadx=12)

# Used to run the software until forcefully exited
window = mainApp()
window.mainloop()