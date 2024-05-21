# Decomposition

Decomposition refers to the process of breaking down a complex problem into smaller, simpler sub-problems. The idea is to solve each subproblem independently 
and then combine the solutions to obtain a solution to the original problem. This allows for the creation of more efficient and manageable algorithm by 
reducing the complexity of the problem and making it easier to identify and solve individual parts. Equally, this makes your code more reusable as each function 
solves a smaller issue which may be reusable elsewhere. 

When breaking the problem down it can be helpful to first of all identify the 
* starting point
    * what input do you have
    * what are the initial conditions
* end point. 
    * what output would you ultimately want
    * what is the end goal 

You can then start to fill in the gaps in between. Through the process of building your algorithm you may find that your start point isn't actually the start point, you need to go further back in the process. Similarly you might find your end goal needs to be redefined.

For example in our tube navigation example crucially we are starting at Paddington TUBE Station, but our passenger is at Paddington RAIL station. Our algorithm is meaningless is they can't get to the TUBE station, so we need to add an additional step to navigate from the TRAIN station to the TUBE station. It is important to remember, that your computer knows absolutely nothing at the beginning of a new program you need to tell it everything. 

![toEdgware](images/directions.jpg)

## Activity: Caesar cypher 

In cryptography, a Caesar cipher is a very simple encryption technique in which each letter in the plain text is replaced by a letter some fixed number of positions down the alphabet. For example, with a shift of 3, A would be replaced by D, B would become E, and so on. The method is named after Julius Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13 places") is a widely used example of a Caesar cipher where the shift is 13. 

Your task in this exercise is to design the algorithm that a computer would need to follow to encode/decode a message using ROT-13.  How does the idea of decomposition apply here? What would you do to implement this? 

It might be helpful to think through how you would manually decode the following message:

```
Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
```



Credits: [Torbjorn Lager](https://www.gu.se/en/about/find-staff/torbjornlager)

Note: Because there are 26 letters (2×13) in the basic Latin alphabet, ROT13 is its own inverse; that is, to undo ROT13, the same algorithm is applied, so the same action can be used for encoding and decoding.

