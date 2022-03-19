from math import floor

from Deck import Deck
from Menu import Menu
from MenuOption import MenuOption


class UserInterface():
    """  	         	  
    Provide the UserInterface for the program, which consists of the Main menu and the Deck menu  	         	  

    Also provides methods for accepting and validating user input  	         	  
    """

    def __init__(self):
        self.__m_currentDeck = None
        self.__m_menu = Menu("Main")
        self.__m_menu += MenuOption("C", "Create a new deck")
        self.__m_menu += MenuOption("X", "Exit the program")

    def run(self):
        """  	         	  
        Return None: present the main menu to the user  	         	  

        Repeatedly prompt for a valid command until good input is given, or the program is exited  	         	  
        """
        print("Welcome to the Bingo Deck Generator\n")

        while True:
            command = self.__m_menu.prompt()
            if command.upper() == "C":
                self.__create_deck()
            elif command.upper() == "X":
                break

    def __deck_menu(self):
        """  	         	  
        Return None  	         	  

        Present the deck menu to user until a valid selection is chosen  	         	  
        """
        menu = Menu("Deck")
        menu += MenuOption("P", "Print a card to the screen")
        menu += MenuOption("D", "Display the whole deck to the screen")
        menu += MenuOption("S", "Save the whole deck to a file")
        menu += MenuOption("X", "Return to the Main menu")

        while True:
            command = menu.prompt()
            if command.upper() == "P":
                self.__print_card()
            elif command.upper() == "D":
                self.__m_currentDeck.__str__()
            elif command.upper() == "S":
                self.__save_deck()
            elif command.upper() == "X":
                break

    def __create_deck(self):
        cardSizeInput = False
        while cardSizeInput == False:
            cardSize = input("Enter card size [3 - 16]: ")
            if cardSize.isdigit() == True:
                self.N = int(cardSize)
                if 3 <= self.N <= 16:
                    cardSizeInput = True
                else:
                    print(f"\nPlease provide an input [3 - 16]: ")
                    continue
            else:
                print(f"\nPlease provide an input [3 - 16]: ")
                continue

        maxNumInput = False
        while maxNumInput == False:
            self.maxNum = input(f"Enter max number [{(2 * self.N * self.N)} - {floor(3.9 * self.N * self.N)}]: ")
            if self.maxNum.isdigit() == True:
                if (2 * self.N * self.N) <= int(self.maxNum) <= floor(3.9 * self.N * self.N):
                    maxNumInput = True
                else:
                    print(f"\nPlease provide an input [{(2 * self.N * self.N)} - {floor(3.9 * self.N * self.N)}]: ")
                    continue
            else:
                print(f"\nPlease provide an input [{(2 * self.N * self.N)} - {floor(3.9 * self.N * self.N)}]: ")
                continue

        numCardsInput = False
        while numCardsInput == False:
            self.numCards = input("Enter number of cards [2 - 8192]: ")
            if self.numCards.isdigit() == True:
                if 2 <= int(self.numCards) <= 8192:
                    numCardsInput = True
                else:
                    print(f"\nPlease provide an input [2 - 8192]: ")
                    continue
            else:
                print(f"\nPlease provide an input [2 - 8192]: ")
                continue

        self.__m_currentDeck = Deck(self.N, self.numCards, self.maxNum)
        return self.__deck_menu()

    def __print_card(self):

        validInput = False
        while validInput == False:
            cardID = input(f"ID of card to print [1 - {self.numCards}]: ")
            if cardID.isdigit() == True:
                if 1 <= int(cardID) <= int(self.numCards):
                    validInput = True
                    print(self.__m_currentDeck.card(cardID))
                else:
                    print(f"\nPlease provide an input [1 - {self.numCards}]: ")
                    continue
            else:
                print(f"\nPlease provide an input [1 - {self.numCards}]: ")
                continue



    def __save_deck(self):
        validInput = False
        while validInput == False:
            fileName = input("Enter output file name: ")
            if fileName != '':
                with open(fileName, 'x') as file:
                    file.write(str(self.__m_currentDeck))
                    print(f"Deck saved to '{fileName}'!")
                    validInput = True
                file.close()
            else:
                print("Please provide a valid file name.\n")
        pass
