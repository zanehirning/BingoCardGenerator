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
*   Function signatures that include:
    *   Descriptive names.
    *   Parameter lists.
    *   Documentation strings that explain the purpose, inputs and outputs.
*   Pseudocode that captures how each function works.
    *   Pseudocode != source code.  Do not paste your finished source code into this part of the plan.
    *   Explain what happens in the face of good and bad input.
    *   Write a few specific examples that occurred to you.


## Phase 3: Implementation *(15%)*

**Deliver:**

```python

class Card():  	         	  
    COLUMN_NAMES = list("BINGODARLYZEMPUX")  	         	  

    def __init__(self, idnum, ns):  	         	  
        """  	         	  
        Initialize a Bingo! card  	         	  
        """  	         	  
        pass  	         	  

    def id(self):  	         	  
        """  	         	  
        Return an integer: the ID number of the card  	         	  
        """  	         	  
        pass  	         	  

    def number_at(self, row, col):  	         	  
        """  	         	  
        Return an integer or a string: the value in the Bingo square at (row, col)  	         	  
        """  	         	  
        pass  	         	  

    def __len__(self):  	         	  
        """  	         	  
        Return an integer: the length of one dimension of the card.  	         	  
        For a 3x3 card return 3, for a 5x5 return 5, etc.  	         	  
        """  	         	  
        pass  	         	  

    def __str__(self):  	         	  
        """  	         	  
        Return a string: a neatly formatted, square bingo card  	         	  
        """  	         	  
        pass  	         	  

    

``` 
*   (More or less) working code.
*   Note any relevant and interesting events that happened while you wrote the code.
    *   e.g. things you learned, things that didn't go according to plan


## Phase 4: Testing & Debugging *(30%)*

**Deliver:**

*   A set of test cases that you have personally run on your computer.
    *   Include a description of what happened for each test case.
    *   For any bugs discovered, describe their cause and remedy.
*   Write your test cases in plain language such that a non-coder could run them and replicate your experience.


## Phase 5: Deployment *(5%)*

**Deliver:**

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

*   Write brief and honest answers to these questions: *(Note: do this before you complete **Phase 5: Deployment**)*
    *   What parts of your program are sloppily written and hard to understand?
        *   Are there parts of your program which you aren't quite sure how/why they work?
        *   If a bug is reported in a few months, how long would it take you to find the cause?
    *   Will your documentation make sense to...
        *   ...anybody besides yourself?
        *   ...yourself in six month's time?
    *   How easy will it be to add a new feature to this program in a year?
    *   Will your program continue to work after upgrading...
        *   ...your computer's hardware?
        *   ...the operating system?
        *   ...to the next version of Python?
*   Fill out the Assignment Reflection on Canvas.
