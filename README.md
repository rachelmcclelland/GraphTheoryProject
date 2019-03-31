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

https://www.quora.com/What-is-the-shunting-yard-algorithm
This website explains what the shunting algorithm does and how it works.

THOMPSONS CONSTRUCTION
https://en.wikipedia.org/wiki/Thompson%27s_construction
The first link I got when I googled Thompsons construction was for the Wikipedia page.
It has a very detailed description of what this algorithm is and how it can be used. Wikipedia says that
Thompson's construction is a method of transforming a regular expression into an equivalent 
nondeterministic finite automaton (NFA). It says that this NFA can then be used to match strings against
the regular expression and that this algorithm is credited to Ken Thompson.

https://swtch.com/~rsc/regexp/regexp1.html
This website helped me figure out how to add the + operator and the ? operator into the compileToNFA function.

https://www.cs.york.ac.uk/fp/lsa/lectures/REToC.pdf
    -> This links has detailed lecture notes on Thompsons construction. It uses a step by guide on
    how the algorithm is used and it is also easy to follow

convertToPostfix function
This function uses the Shunting Yard Algorithm for converting from infix to postfix.
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
This function passes in the postfix that was created in the convertToPostfix function. It compiles a postfix regular expression into an NFA. It begins with creating an empty array for the nfastack
For every character in the postfix, it checks to see what it is. 
If it is a . (concatenate), it pops two characters of the stack. It connects the first NFA's accept state to the second NFA's initial state and then push the new NFA back onto the stack.
If it is a | (or), it also pops two NFA's of the stack. This time it creates a new initial state and connects it to the initial states of the two NFA's that were popped from the stack. It then creates a new accept state, connecting the accept states of the two NFA's popped from the stack to the new state created and then pushes the new nfa back onto the stack.
If the character is a * (zero or more), it pops only one NFA from the stack and creates a new initial and accept state. Then it joins the new initial state to the NFA's initial state and the new accept state which is then pushed back onto the stack.
If the character is a + (one or more), one NFA is popped from the stack. It joins the new initial state to the NFA's inital state. The old accept state is joined to the new accept state and the NFA's initial state. The NFA's initial state and the accept state is used to create a new NFA which is then pushed to the stack.
If the character is a ?(zero or one), one NFA is popped of the stack. A new state for initial is created. The new initial state is joined up to the NFA's initial state. A new accept state is then created. The NFA's accept state is joined with this accept state and the initial state is joined with the accept state as well. The initial state and the accept state are used to create a new NFA and pushed to the stack.
If none of the above options are true, a new accept and initial state are created. The initial state is joined to the accept state using an arrow labelled c. A new NFA is created with the initial and accept states and pushed back onto the stack.

followEdges function
This is a helper function. It returns the set of states that can be reached from the state following the edge arrows.
It begins by creating a new set called states and have the state that was passed in as its only member. It checks if the state has any arrows labelled e from it. If the first edge is a state, check if there is an edge and follow it by recalling the same function and do the same for the second edge. Return the state when it is finished.

match function
This function takes in the infix and a string which matches the string to the infix regular expression and return where the accept state in the set of current states. First it uses the infix and calls the convertToPostfix function and assigns it to the postfix variable. Postfix is then passed into the complieToNfa function. A set is created for the current set of states and the next set of states. The initial state is added to current. For every character in the string, the current set of states are looped through. If the state has a labelled of the character in the string, the first edge of the current state is added to next. Current is then set to next and next is created as a new set.

When the project is first ran, the user is asked how many infix notations they would like to parse into postfix notation. The user is then asked to enter in each infix. They are then asked how many strings they want to use for the matching algorithm and then prompted to enter each string. The infixes and strings are both looped around in an inner loop and each passed into the match function.