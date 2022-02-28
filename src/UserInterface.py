from math import floor  	         	  

import Deck  	         	  
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
                print(self.__m_currentDeck)  	         	  
            elif command.upper() == "S":  	         	  
                self.__save_deck()  	         	  
            elif command.upper() == "X":  	         	  
                break  	         	  

    def __get_str(self, prompt):  	         	  
        """  	         	  
        Return a string: non-empty input entered by the user  	         	  

        Take a prompt string as input  	         	  
        Repeat the prompt until a non-empty string is provided  	         	  
        """  	         	  
        pass  	         	  

    def __get_int(self, prompt, lo, hi):  	         	  
        """  	         	  
        Return an integer: validated integer input by user  	         	  

        Take a prompt string, low and high integers as input  	         	  
        Repeat the prompt until an integer that is in-range is provided  	         	  
        """  	         	  
        pass  	         	  

    def __create_deck(self):  	         	  
        """  	         	  
        Return None: Create a new Deck  	         	  

        The Deck is stored in self.__m_currentDeck  	         	  
        """  	         	  
        pass  	         	  

    def __print_card(self):  	         	  
        """  	         	  
        Return None: Print one Card from the Deck  	         	  

        Prompt user for a Card ID  	         	  
        """  	         	  
        pass  	         	  

    def __save_deck(self):  	         	  
        """  	         	  
        Return None: Save a Deck to a file  	         	  

        Prompt user for the name of file to write the entire Deck into  	         	  
        """  	         	  
        pass  	         	  
