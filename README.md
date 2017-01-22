# Scurry-Challenge
[![Build Status](https://travis-ci.org/josecolella/Scurri-Challenge.svg?branch=master)](https://travis-ci.org/josecolella/Scurri-Challenge)



##Challenge 1: A bright spot

`Tell us about one thing you are proud of in your career. It could be a difficult technical problem you had to solve in your work or a personal project. There is no need to go into details; a short paragraph explaining the problem and why you are proud of it would be fine.`

If I had to choose on proud moment of a technical problem that I have had to solve for a work or personal project, I would choose the navigation implementation of a retro survival game created for an artificial intelligence course in university. The game was programmed in Python,
The technical problem presented was to find a way to efficient implementation for the movement of the characters. Each character has unique sprite images for moving east, north, south, and west, and it needs to look natural to the player that the character was moving. I ended up utilizing a circular iterator with the different images. The use of the iterator allowes for space and time saving as the results are yielded when called, and the use of a circular structure satisfied the requirement to successively load sprite images making it seemless for the player. Below is a sample of the implementation that was utilized for the game.
I'm really proud of this solution as knowledge of data structures provided a solution to a real problem for an application that was to be used by many users. I also am proud of the use of iterators, as we are not loading everything in memory, just using the sprite images as needed.

```python3
self.walking_west_images = itertools.cycle(
    (self.imgPath+'w_walk_l.png',
     self.imgPath+'w.png',
     self.imgPath+'w_walk_r.png'
     )
)
self.walking_east_images = itertools.cycle(
    (self.imgPath+'e_walk_l.png',
     self.imgPath+'e.png',
     self.imgPath+'e_walk_r.png'
     )
)
self.walking_north_images = itertools.cycle(
    (self.imgPath+'n_walk_l.png',
     self.imgPath+'n.png',
     self.imgPath+'n_walk_r.png'
     )
)
self.walking_south_images = itertools.cycle(
    (self.imgPath+'s_walk_l.png',
     self.imgPath+'s.png',
     self.imgPath+'s_walk_r.png'
     )
)
```


##Challenge 2: FizzBuzz

`Write a program that prints the numbers from 1 to 100. But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”. For numbers which are multiples of both three and five print “ThreeFive”.`

For the resolution of this question, I wanted to show my own version of solving this question. I trust that this is what the challenge rewards.

Here is an illustration of the solution that I have implemented in Python.
Here are the steps to the solution:

- Start from a set that contains the range of numbers from 1 to 100
- Create two different subsets [Filter]
    - A set that contains only numbers that are divisible by 3 **Set MultipleThree**
    - A set that contains only numbers that are divisble by 5 **Set MultipleFive**  
    - A set that takes the set difference between all numbers and the set divisible by 3 and the set divisible by 5
    - A set that is the intersection between **Set MultipleThree** and **Set MultipleFive**, resulting in a set that
    has the numbers that are multiple of 3 and 5 **Set MultipleBoth**
- Create restricted set for multiple of three and for the set of multiple of 5
    - A set that is the set difference between **Set MultipleThree** and **Set MultipleBoth**
    - A set that is the set difference between **Set MultipleFive** and **Set MultipleBoth**.
- Map a function for each of these sets to create tuple pair (int, str) with the conditions placed
    - For **Set MultipleBoth** the set is *{(15,'ThreeFive'),...}*
    - For **Set MultipleThree** the set is *{(3,'Three'),...}*
    - For **Set MultipleFive** the set is *{(5, 'Five'),...}*
    - For **Set Remaining** the set is *{(1, ''), ...}*
- These sets are chained and sorted on the int parameter.
- The result is cleaned so that only integers and string are left in the data structure.

The implementation can be found in the `solution.py` file. I have decided to utilize iterators for returning the result,
allowing for efficiency in memory and speed for large ranges, and if the user wants the fizz_buzz result for a specific
integer, the function will return an iterator with just that result.

###Requirements

- Python 3.6 # Program utilizes new typing module for type hinting

###Usage:

Run the main.py see the result of the implementation.

```sh
git clone https://github.com/josecolella/Scurri-Challenge
cd Scurri-Challenge
python3 main.py
```

The main.py outputs the result of the fizz_buzz for each number from 1 to 100.

```python
from __future__ import print_function
import solution


if __name__ == '__main__':
    beginning_index = 1
    ending_index = 100
    results = solution.fizz_buzz(beginning_index, ending_index)
    for result in results:
        print(result)
```


###Tests

To run tests execute the following

```sh
git clone https://github.com/josecolella/Scurri-Challenge
python3 tests.py -v
```

##Challenge 3: UK Postcodes

For this challenge, I decided to create a separate [repo](https://github.com/josecolella/postcode_uk).
The [README](https://github.com/josecolella/postcode_uk) contains information on the API offered by the library

[Tests](https://github.com/josecolella/postcode_uk/blob/master/tests/unit/tests.py) are also present for this library.


