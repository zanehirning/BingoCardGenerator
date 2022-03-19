# Software Development Plan
 

**Deliver:**

###What the program aims to solve:
* This program aims to make Bingo cards that can be anywhere from a 3x3 to 16x16.
* The Bingo cards increase in value from columns left to right.
* They can be stored into a deck and also stored onto a file.
* A good solution will not crash when bad input is given, nor will it have repeating numbers.
* If the nxn card is odd (i.e. 3x3, 7x7, etc.) then the middle spot will be a "Free" spot.

###What I already know:
* How to make a range of numbers
* How to take input from the user and manipulate that input

###What I don't know:
* How to format the Bingo cards and place the numbers in correct spots
* How to take the output and store it into a file


## Phase 1: System Analysis *(10%)*

**Deliver:**

* Input will be provided by the user via the REPL.
* It will ask if the user wants to create a deck, then to print the card, save, display the whole deck, or exit.
* The output will take form depending on what the user wants. Whether this is to print the card, display the deck, etc.
* This program will use some sort of "file" commands to save the decks, formatting formula, if statements, etc.


## Phase 2: Design *(30%)*

**Deliver:**

```
class Card():
    This class will create a Bingo card
    It will intialize an ID number for the Bingo card
    It can provide the length of the Bingo card, what numbers are in certain spots, and return a formatted Bingo card.
    
class Deck():
    This class will create a deck that stores Bingo cards from the Card class
    It can provide how many cards are in the deck, retrieve a certain card from the deck, and display the entire deck.
    
class UserInterface():
    The UserInterface class will take input from the user and use that input to perform different tasks.
    These tasks include printing the card, saving the deck, displaying a whole deck, or exitting.
    It will take input and prompt the user to provide valid input, as well as including a range for the user to give valid input.
    If bad input is given, nothing will happen, but the prompt will be reprinted as well as some sort of error message.
    
class RandNumberSet():
    This class is almost finished, however there is a bug that causes numbers to repeat themselves sometimes.
    This bug will need to be located and fixed.

The rest of the classes are already complete and I do not plan on changing them much (or at all), unless I need to.

```

## Phase 3: Implementation *(15%)*

**Deliver:**

```python
#Card
class Card():
    COLUMN_NAMES = list("BINGODARLYZEMPUX")

    def __init__(self, idnum, ns):
        """  	         	  
        Initialize a Bingo! card  	         	  
        """
        self.__idnum = idnum
        self.__ns = ns

    def id(self):
        """  	         	  
        Return an integer: the ID number of the card  	         	  
        """
        return self.__idnum
        pass

    def number_at(self, row, col):
        """  	         	  
        Return an integer or a string: the value in the Bingo square at (row, col)  	         	  
        """
        checkOdd = len(self.__ns) % 2
        if checkOdd != 0:
            midRow = (len(self.__ns) // 2)
            if row == midRow and col == midRow:
                return "Free!"
        return self.__ns[row][col]
        pass

    def __len__(self):
        """  	         	  
        Return an integer: the length of one dimension of the card.  	         	  
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	         	  
        """
        return len(self.__ns)

    def __str__(self):
        """  	         	  
        Return a string: a neatly formatted, square bingo card  	         	  
        """
        header = '   '
        self.colNames = Card.COLUMN_NAMES[0:len(self.__ns)]
        header += '     '.join(self.colNames)
        card = ''
        spaces = ''
        for i in range(len(self.__ns)):
            spaces += "+-----"
        spaces += "+\n"

        for r in range(len(self.__ns)):
            for c in range(len(self.__ns)):
                card += f"|{self.number_at(r, c) : ^5}"
            card += "|" + "\n" + spaces

        return header +  "\n" + spaces + card + "\n"


#Deck
from Card import Card  	         	  
from RandNumberSet import RandNumberSet  	         	  
from Card import Card  	         	  
from RandNumberSet import RandNumberSet


class Deck():  	         	  
    def __init__(self, card_size, num_cards, max_num):  	         	  
        """  	         	  
        Deck constructor  	         	  
        """
        self.card_size = int(card_size)
        self.num_cards = int(num_cards)
        self.max_num = int(max_num)
        self.__deck = []
        for i in range(self.num_cards):
            RNS = RandNumberSet(self.card_size, self.max_num)
            c = Card(i + 1, RNS)
            self.__deck.append(c)

    def __len__(self):  	         	  
        """  	         	  
        Return an integer: the number of cards in this deck  	         	  
        """
        return int(self.num_cards)


    def card(self, n):  	         	  
        """  	         	  
        Retrieve Card N from the deck  	         	  
        """
        return self.__deck[int(n)-1]


    def __str__(self):  	         	  
        """  	         	  
        Return None: Display the entire Deck as a string  	         	  
        """
        output = ""
        for i in range(self.num_cards):
            c = str(self.__deck[i])
            output += c
        print(output)
        return output


#UserInterface
from math import floor  	         	  

import Deck  	         	  
from Menu import Menu  	         	  
from MenuOption import MenuOption  	         	  


from math import floor



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

    def __create_deck(self):
        """  	         	  
        Return None: Create a new Deck  	         	  

        The Deck is stored in self.__m_currentDeck  	         	  
        """
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

        self.__m_currentDeck = Deck(self.N, self.numCards, self.maxNum).__str__()
        return self.__deck_menu()

    def __print_card(self):
        """  	         	  
        Return None: Print one Card from the Deck  	         	  

        Prompt user for a Card ID  	         	  
        """

        validInput = False
        while validInput == False:
            cardID = input(f"ID of card to print [1 - {self.numCards}]: ")
            if cardID.isdigit() == True:
                if 1 <= int(cardID) <= int(self.numCards):
                    validInput = True
                    return Deck(self.N, self.numCards, self.maxNum).card(cardID)
                else:
                    print(f"\nPlease provide an input [1 - {self.numCards}]: ")
                    continue
            else:
                print(f"\nPlease provide an input [1 - {self.numCards}]: ")
                continue

    def __save_deck(self):
        """  	         	  
        Return None: Save a Deck to a file  	         	  

        Prompt user for the name of file to write the entire Deck into  	         	  
        """
        validInput = False
        while validInput == False:
            fileName = input("Enter output file name: ")
            if fileName != '':
                with open(fileName, 'x') as file:
                    file.write(self.__m_currentDeck)
                    print(f"Deck saved to '{fileName}'!")
                    validInput = True
                file.close()
            else:
                print("Please provide a valid file name.\n")
        pass
         	  

#RandNumberSet
import random  	         	  


class RandNumberSet():  	         	  
    MIN_SIZE = 3  	         	  
    MAX_SIZE = 16  	         	  

    def __init__(self, nSize, nMax):  	         	  
        """  	         	  
        Create a RandNumberSet  	         	  

        'nSize': a parameter restricted to be in the range [3..16]  	         	  
        'nMax': a parameter restricted to be no less than `nSize*nSize`  	         	  

        Numbers are kept in separate segments so that the numbers within  	         	  
        columns on the resulting Bingo! card increase from left to right.  	         	  

        Within a column numbers are unordered.  	         	  

        A newly initialized RandNumberSet may present its numbers in  	         	  
        order.  Use .shuffle() to mix it up.  	         	  
        """  	         	  
        # sanity check on __m_nSize  	         	  
        self.__m_nSize = nSize  	         	  
        if self.__m_nSize < RandNumberSet.MIN_SIZE:  	         	  
            self.__m_nSize = RandNumberSet.MIN_SIZE  	         	  

        if self.__m_nSize > RandNumberSet.MAX_SIZE:  	         	  
            self.__m_nSize = RandNumberSet.MAX_SIZE  	         	  

        # sanity check on __m_nMax: pick the larger of `nMax` or `nSize^2 * 2`  	         	  
        self.__m_nMax = max(nMax, self.__m_nSize * self.__m_nSize * 2)  	         	  
        self.__m_nRowPos = 0  	         	  

        segments = []  	         	  
        segment_size = nMax // self.__m_nSize  # n.b. `//` operator means "integer division"  	         	  
        remainder = nMax % self.__m_nSize  	         	  
        low = 1  	         	  
        for segment in range(1, self.__m_nSize + 1):  	         	  
            high = low + segment_size  	         	  
            # When `len(RandNumberSet)` is not evenly divisible by `nSize`,  	         	  
            # there will be some numbers left over.  Distribute these extra  	         	  
            # numbers starting from segment #0, going up from there  	         	  
            if segment <= remainder:  	         	  
                high += 1  	         	  
            # XXX: I can never remember; is the endpoint of `range()` included or excluded?  	         	  
            segments.append(list(range(low, high)))  	         	  
            low = high  	         	  
        self.segments = segments  	         	  

    def __len__(self):  	         	  
        """  	         	  
        This dunder makes `len()` work on RandNumberSets  	         	  

        The length of a RandNumberSet is equal to the number of segments  	         	  
        it contains; in other words, len(RandNumberSet) == card size.  	         	  
        """  	         	  
        return self.__m_nSize  	         	  

    def __getitem__(self, n):  	         	  
        """Return the specified row of Bingo numbers, raise IndexError when out-of-bounds"""  	         	  
        if 0 <= n < self.__m_nSize:  	         	  
            row = []  	         	  
            for seg in self.segments:  	         	  
                row.append(seg[n])  	         	  
            return row  	         	  
        else:  	         	  
            raise IndexError  	         	  

    def shuffle(self):  	         	  
        """  	         	  
        Shuffle each segment and reset the current row position so that  	         	  
        next_row() will start from the top again.  	         	  
        """  	         	  
        for seg in self.segments:  	         	  
            random.shuffle(seg)  	         	  
        self.__m_nRowPos = 0  	         	  

    def next_row(self):  	         	  
        """  	         	  
        Return the next row of Bingo numbers, or None if the RandNumberSet  	         	  
        is exhausted.  	         	  

        This method automatically keeps track of which row is up next  	         	  
        """  	         	  
        if self.__m_nRowPos >= self.__m_nSize:  	         	  
            return None  	         	  
        row = []  	         	  
        for seg in self.segments:  	         	  
            row.append(seg[self.__m_nRowPos])  	         	  
        self.__m_nRowPos += 1  	         	  
        return row  	         	  

    def __str__(self):  	         	  
        strs = []  	         	  
        for seg in self.segments:  	         	  
            strs.append(str(seg))  	         	  
        return '\n'.join(strs)  	         	  

``` 
- While writing this code, I noticed there were functions that I did not completely understand.
- These functions included the __str__ and __int__ functions in the UI file.
- I later learned these were meant for error checking, however, this was after I had already written code that could error check.
- If I used these functions, perhaps my code would be more concise, and under different circumstances, I would rewrite my program.
- I also learned that I am not very good at formatting, and I have always struggled with understanding classes. After this assignment though, I feel more confident about using classes and formatting output.


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

- I have ran several tests regarding different card sizes as well as different file names.
- Each time I tested a different card size, the output matched similar to what I had assumed would happen.
- Each file name that I tested had worked, except for the few cases that windows does not like. (I believe it was files with ":"?)
- I discovered many bugs in my code, however, they were not due to a variety of test cases. These mostly stemmed from syntax errors, like when to return something vs printing it.


## Phase 5: Deployment *(5%)*

**Deliver:**
- My repository was pushed to GitLab, the final commit was present. Prior to pushing, I tested multiple different cases on my program to ensure that it is working correctly and will work on the grader's computer.


*   Your repository pushed to GitLab.
*   **Verify** that your final commit was received by browsing to its project page on GitLab.
    *   Ensure the project's URL is correct.
    *   Review the project to ensure that all required files are present and in correct locations.
    *   Check that unwanted files have not been included.
    *   Make any final touches to documentation, including the Sprint Signature and this Plan.
*   **Validate** that your submission is complete and correct by cloning it to a new location on your computer and re-running it.
	*	Run your program from the command line so you can see how it will behave when your grader runs it.  **Running it in PyCharm is not good enough!**
    *   Run through your test cases to avoid nasty surprises.
    *   Check that your documentation files are all present.


## Phase 6: Maintenance

**Deliver:**

###1.
- I would say my code is understandable for the most part. The error checking did get repetitive and may seem to long, but it should be easy to follow. If I had more time, I would have done the error checking in __str__ and __int__
- Most of my code is pretty understandable from my view, the code makes sense to me and how/why it works seems simple enough.
- Most of my debugging consisted of debugging after a syntax error, as well as print statement debugging. Syntax errors are easy to find and easy to fix. If a problem were to arise, I feel like I could utilize this method to resolve the bug quickly.

###2.
- This code should make sense to most people, as long as they understand how the classes function and work together to create the program.
- This code will make sense to me in six months, this code is fairly well constructed. (in my opinion)

###3.
- It depends on the implementation. If it is just adding larger cards, etc. it should be easy enough. Everything that can be implemented should be fairly simple and straightforward.

###4.
- This program should work on new hardware, and would probably work better on new hardware.
- This program should work on new or different OS's.
- As long as the next versions don't change how any functions in my program work, it should run on the next version.
