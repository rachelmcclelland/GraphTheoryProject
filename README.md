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

