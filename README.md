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
    -> This links has detailed lecture notes on Thompsons construction. It uses a step by guide on
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

state class
This class represents a state with two arrows labelled by the variable label.

nfa class
An NFA is represented by its initial and accept states. This class contains a constructor which represents the current instance of the class. 

compileToNFA function
This function passes in the postfix that was creted in the convertToPostfix function. It compiles a postfix regular expression into an NFA. It begins with creating an empty array for the nfastack
For every character in the postfix, it checks to see what it is. 
If it is a . (concantenate), it pops two characters of the stack. It connects the first NFA's accept state to the second NFA's inital state and then push the new NFA back onto the stack.
If it is a | (or), it also pops two NFA's of the stack. This time it creates a new initial state and connects it to the intial states of the two NFA's that were popped from the stack. It then creates a new accept state, connecting the accept states of the two NFA's popped from the stack to the new state created and then pushes the new nfa back onto the stack.
If the character is a * (zero or more), it pops only one NFA from the stack and creates a new initial and accept state. Then it joins the new inital state to the NFA's inital state  and the new accept state which is then pushed back onto the stack.
If the character is a + ( one or more), one NFA is popped from the stack. It joins the new inital state to the NFA's inital state. The old accept state is joined to the ew accept state and the NFA's intial state. The NFA's intial state and the accept state is used to create a new NFA which is then pushed to the stack.
If the character is a ?(zero or one), one NFA is popped of the stack. A new state for initial is created. The new initial state is joined up the the NFA's inital state. A new accept state is then created. The NFA's accept state is joined with this accept state and the initial state is joined with the accept state aswell. The initial state and the accept state are used to create a new NFA and pushed to the stack.
If none of the above options are true, a new accept and inital state are created. The inital state is joined to the accep state using an arrow labelled c. A new NFA is created with the inital and accept states and pushed back onto the stack.