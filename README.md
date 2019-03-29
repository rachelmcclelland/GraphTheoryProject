SHUNTING  YARD ALGORITHM
https://brilliant.org/wiki/shunting-yard-algorithm/
This algorithm was invented by Edsger Dijkstra. It is used for parsing mathematical expressions.
It uses the use of stacks to rearrange the operators and operands into the correct for for evaluation.
The procedure used is as follows:
    ->Expressions are parsed from the left side to the right side
    ->Each time a number or an operator is read, it is pushed to the stacks
    ->If an operator comes up, we pop the required operands from the stack, perform the operations, 
    and push the result back to the stack.
    ->We are finished when the string is empty 

THOMPSONS CONSTRUCTION
https://en.wikipedia.org/wiki/Thompson%27s_construction
The first link I got when I googled Thompsons construction was for the wikipedia page.
It has a very detailed description of what this alogorithm is and how it can be used. Wikipedia says that
Thompson's construction is a method of transforming a regular expression into an equivalent 
nondeterministic finite automaton (NFA). It says that this NFA can then be used to match strings against
the regular expression and that this alogorithm is creidted to Ken Thompson
https://swtch.com/~rsc/regexp/regexp1.html
This website helped me figure out how to add the + operator into the compileToNFA function.

https://www.cs.york.ac.uk/fp/lsa/lectures/REToC.pdf
    -> This link is for detailed lecture notoes on Thompsons construction. It uses a step by guide on
    how the alogorithm is used and it is also easy to follow

convertToPostfix function
This function uses the Shunting Yard Algorithim for converting from infix to postfix.
The function starts of by declaring a dictionary of the special characters that will be in the infix.
Next, is a loop that loops through the infix that has been passed in to the function, one character at a time.
If the character is an open bracket, push it to the top of the stack. 
If the character is a closing bracket, which is the end of the grouping, we need to pop off all characters from the stack until we reach the previous opening bracket saving them into a string called pofix.
Remove these characters from the stack using [:-1] and outside the loop do this again to remove the opening bracket aswell.
If the character is in the dictionary that was declared up above, push to the stack after popping lower or equal precedence operators from top of stack into the output.
If the character is not any of the above, take the character and put it into pofix
If there is anything else left on the stack at the end, push all that onto the pofix and return it.

