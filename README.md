# Itertool for python dictionary summary [closed]
This is an answer code to a closed question on StackOverflow - asked by Py-enthusiast

**The question**

I have a python dictionary with identical structure for all person:

```python
game_score = {
    Brian: {game1: 1, game2: 0, game3: 5, game4: 1},
    David: {game1: 2, game2: 1, game3: 0, game4: 2},
    John: {game1: 0, game2: 2, game3: 4, game4: 2},
}
```

There are two goals:

One is to generate all possible combinations of everyone's game scores by game, regardless of person, but keep track of the persons' names. The combinations could be one person, two person, or 3 person, until the total count of person in the dictionary

An example of the outcome by combining David and Brian would be:

```python
{"Brian, David": {"game1": 3, "game2": 1, "game3": 5, "game4": 3}}
```
Second goal is to limit the total game score to a maximum. For example 2. So the result for combining David and Brian would be:

```python
{"Brian, David": {"game1": 2, "game2": 1, "game3": 2, "game4": 2}}
```
Games 1, 3 and 4 are limited to a max of 2

The resulting combinations are added to a new dictionary.

I used python 'itertools' but got error message. Any advice would be greatly appreciated!


**My output**
```
Without maxima ... 
Case of 1 persons
 Brian => {'game1': 1, 'game2': 0, 'game3': 5, 'game4': 1}
 David => {'game1': 2, 'game2': 1, 'game3': 0, 'game4': 2}
 John => {'game1': 0, 'game2': 2, 'game3': 4, 'game4': 2}
Case of 2 persons
 David, John => {'game1': 2, 'game2': 3, 'game4': 4, 'game3': 4}
 Brian, John => {'game1': 1, 'game3': 9, 'game4': 3, 'game2': 2}
 Brian, David => {'game1': 3, 'game3': 5, 'game4': 3, 'game2': 1}
Case of 3 persons
 Brian, David, John => {'game1': 3, 'game3': 9, 'game4': 5, 'game2': 3}

With maxima ... 
Case of 1 persons
 Brian => {'game1': 1, 'game2': 0, 'game3': 5, 'game4': 1}
 David => {'game1': 2, 'game2': 1, 'game3': 0, 'game4': 2}
 John => {'game1': 0, 'game2': 2, 'game3': 4, 'game4': 2}
Case of 2 persons
 David, John => {'game1': 2, 'game2': 3, 'game3': 2, 'game4': 2}
 Brian, John => {'game1': 1, 'game2': 2, 'game3': 2, 'game4': 2}
 Brian, David => {'game1': 2, 'game2': 1, 'game3': 2, 'game4': 2}
Case of 3 persons
 Brian, David, John => {'game1': 2, 'game2': 3, 'game3': 2, 'game4': 2}
```

___
Source of the question: https://stackoverflow.com/questions/72787238/itertool-for-python-dictionary-summary
