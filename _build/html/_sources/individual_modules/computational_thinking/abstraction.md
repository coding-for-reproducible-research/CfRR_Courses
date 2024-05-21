# Abstraction

Abstraction is about simplifying problems, making them easier to solve. The idea is to identify and then ignore information that is not essential.

A great example of abstraction in practice is the London tube map. The problem the tube map is designed to solve is to help people navigate the underground system in London. The essential information to complete this task is:

1. the name of each station
2. which lines each station is on
3. the order of the stations on each line
4. which stations are intersections between lines
5. which stations have onward connections to other transport modes (e.g. National Rail)
6. which stations have step free access

Information that is not essential to this problem is the geographical relativity of each station to each other. This information has been deliberately excluded, as it does not help solve the specific problem of how to navigate London by tube. The tube map would not be appropriate to navigate between the stations above ground by foot, bike or road. 

## Relation to programming

Abstraction is an approach that helps solve problems both computational and otherwise. A core component of programming is about creating and composing abstractions, using objects and functions to represent and define the solution. 

Abstraction works by establishing a level of complexity at which a person interacts with a system, suppressing the more complex details below the current level. Abstraction allows programmers to define objects and functions that can interact with each other in a predictable way without having to understand the underlying details of their implementation. 

If you see a simple interface covering a more complex implementation, this is abstraction. 

For example:
* The interface of a car is simple; a steering wheel, accelerator, brake and gear stick. However, these cover a much more complex machine. You learn that pressing the accelerator makes the car go faster but you are not taught how the acceleration actually works - because the details of this are not important for you to drive the car.

### Activity: Tour Guide

Imagine that you are a hotel tour guide. Tourists staying in your hotel expect to be taken on a tour visiting all the city’s attractions. Using the below map showing locations of all the attractions and how you can get from one to another, you must work out a route that starts from the hotel and takes your tour group to every tourist site. The tourists will be unhappy if they pass through the same place twice. They also want to end up back at their hotel that evening. How would you solve this? What is the minimal amount of information you need to extract from the map to solve it?

![tourguide](images/tour_guide.png)

### Activity: Knight's Tour

On the cross shaped board below, a chess Knight can move two spaces in one direction and then move one square at right angles, or vice versa, as it moves in a chess game. It jumps to the new square without visiting any in between, and must always land on a square on the board. Find a sequence of moves that starts from Square 1, visits every square exactly once and finishes where it started.

![knightstour](images/knights_tour.png)

Are these problems similar? How might you represent the Knight's Tour in a different way to simplify finding a solution?

Abstraction can be incredibly powerful. In the face of a complex problem,  the ability to separate what aspects of a problem are important for solving it, and what are spurious details really helps to design a computational solution.

Abstraction not only makes a problem easier to solve, it should also lead to a more efficient solution as you are not spending time processing information that does not help you get to the solution. 