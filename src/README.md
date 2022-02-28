# Bingo Deck Generator

The main entry point to this program is `bingo.py`.  Run this script to make a Deck of Bingo Cards.


## Unit Tests

You may run all of the unit test suites through PyCharm or by running the `runTests.py` script from your shell.

The starter code consists of 13 test cases, 7 of which pass.

```
$ python runTests.py

test_freeSquares (Testing.testCard.TestCard)
Ensure that odd-numbered cards have 1 "Free!" square in the center ... FAIL
test_id (Testing.testCard.TestCard)
Assert that card ID number is as expected ... FAIL

...

======================================================================
FAIL: test_card (Testing.testDeck.TestDeck)
Ensure that Cards can be accessed from within a Deck
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/fadein/school/Sp22/cs1440/Assn/3-Bingo/starter/src/Testing/testDeck.py", line 30, in test_card
    self.assertIsNotNone(self.deck2.card(1))
AssertionError: unexpectedly None

----------------------------------------------------------------------
Ran 13 tests in 0.015s

FAILED (failures=4, errors=2)
```

You may also run an individual unit test suite like this:

```
$ python -m unittest Testing/testMenu.py
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
