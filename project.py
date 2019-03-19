# Graph Theory Project 2019.
#Rachel McClelland
#G00337231

def convertToPostfix(infix):
    
    # pick any number but pick a higher number for the * as
    # it has higher precidence
    # specials is a dictionary
    specials = {'*': 50, '.': 40, '|': 30 } 

    pofix = ""
    stack = ""

    # Loop through the string a charactet at a time
    for c in infix:
        # If an open bracekt, push to the stack
        if c == '(':
            stack = stack + c
        # If a closing bracket, pop from the stack, push to output until open bracket
        elif c ==')':
            while  stack[-1] != '(':
                pofix = pofix + stack[-1] #top of stack
                stack = stack[:-1] #get rid of that element from the stack
            stack = stack[:-1] # then take the open bracket of the top of stack aswell
        # If it's an operator, push to stack after popping lower or equal precedence
        # operators from top of stack into outpt
        elif c in specials:
            #if anything is on the stack and if c is in special ( if not return 0) is of lower precidence that last one on the stack
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix + stack[-1], stack[:-1]
            stack = stack + c
        # Regular characters are pushed immediatelt to the output
        else:
            # if not any of above. take character and put into pofix
            pofix = pofix + c
     # if there is anything else left on the stack at the end
     #push all that onto the profix
    while  stack: 
        pofix, stack = pofix + stack[-1], stack[:-1] # same code as above, just looks different
    return pofix

infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c", "(a.b)|(c*.d)"]

for i in infixes:
    print(convertToPostfix(i))