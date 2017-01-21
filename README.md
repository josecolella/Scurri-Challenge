# Scurry-Challenge
[![Build Status](https://travis-ci.org/josecolella/Scurry-Challenge.svg?branch=master)](https://travis-ci.org/josecolella/Scurry-Challenge)


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

1. Start from a set that contains the range of numbers from 1 to 100
2. Create four different subsets [Filter]
    a. A set that contains only numbers that are divisible by both 5 and 3 *Set MultipleBoth*
    b. A set that contains only numbers that are divisible by 3 and not included in the previous set *Set MultipleThree*
    c. A set that contains only numbers that are divisble by 5 and not included in the previous two sets *Set MultipleFive*
    d. A remaining set which is the set difference between the set with all numbers and the previous three sets *Set Remaining*
3. Map a function for each of these sets to create tuple pair (int, str) with the conditions placed
    a. For *Set MultipleBoth* the set is **{(15,'ThreeFive'),...}**
    b. For *Set MultipleThree* the set is **{(3,'Three'),...}**
    c. For *Set MultipleFive* the set is **{(5, 'Five'),...}**
    d. For *Set Remaining* the set is **{(1, ''), ...}**
4. These sets are joined and sorted on the int parameter.
5. The result is cleaned so that only integers and string are left in the data structure.

![Solution Image](https://cl.ly/1q3c230m2n3F/download/Image%202017-01-21%20at%2012.39.51%20pm.png)
