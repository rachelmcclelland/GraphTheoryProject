# Graph Theory Project 2019.
#Rachel McClelland
#G00337231

def convertToPostfix(infix):
    
    # pick any number but pick a higher number for the * as
    # it has higher precidence
    # specials is a dictionary
    specials = {'*': 50, '.': 40, '|': 30, '+': 20 } 

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

# Represents a state with the two arrows, labelled by label.
# Use None for a label representing "e" arrows
class state:
    label = None # None is similar to null variable
    edge1 = None
    edge2 = None

# An NFA is represented by its initial and accept states
class nfa:
    initial = None
    accept = None

    # Constructor for nfa class
    # Must include an initial argument to a class 'self'
    # Represents the currrent instance of the class
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compileToNFA(pofix):
    """ Complies a postfix regular expression into an NFA"""
    nfastack = []

    for c in pofix:
        if c == '.':
            # Pop two NFA's off the stack
            nfa2 = nfastack.pop() # take last element out of the array and return into nfa2
            nfa1 = nfastack.pop() # originally the first thing that was put onto the stack
            
            # Connect first NFA's accpet state to the second's intial
            nfa1.accept.edge1 = nfa2.initial

            # Push NFA to the stack
            newnfa = nfa(nfa1.initial, nfa2.accept)
            nfastack.append(newnfa)
        elif c == '|':
            # Pop two NFA's off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()

            # Create a new initial state, connect it to initial states of the two NFA's
            # popped from the stack
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial

            # Create a new accept state, connectin the accept states of the two 
            # NFA's popped from the stack, to the new state
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge1 = accept

            # Push the new NFA to the stack
            nfastack.append(nfa(initial, accept))
        elif c == '*':
            # Pop a single NFA from the stack
            nfa1 = nfastack.pop()

            # Create new initial and accpet states
            initial, accept= state(), state()

            # Join the new initial state to nfa1's inital state and the new accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept

            # Join the old accept state to the new accept state and nfa1's initial state
            nfa1.accept.edge1 = nfa.initial
            nfa1.accept.edge2 = accept

            # Push the new NFA to the stack
            nfastack.append(nfa(initial, accept))          
        else:    
            # Create new initial and accept states
            accept = state() # create a new state for the accept state
            initial = state() # create a new state for the initial state

            # Join the initial state to the accept state using an arrow labelled c
            initial.label = c # the arrow labeled by the characted
            initial.edge1 = accept # point edge1 to the accept state

            # Push new NFA to the stack
            nfastack.append(nfa(initial, accept)) # new instance of nfa stack
    # nfastack should only have a single nfa on it at this point
    return nfastack.pop()

def followEdges(state):
    # Helper function
    """Return the set of states that can be reached from state following
    e arrows."""
    # Create a new set, with state as its only member
    states = set()
    states.add(state)

    # Check if state has arrows labelled e from it
    if state.label is None:
        # Check if edge1 is a state
        if state.edge1 is not None:
            # If there's an edge, follow it
            states |= followEdges(state.edge1)  # Same as states = states | followEdges(state.edge1)
        #Check if edge2 is a state
        if state.edge2 is not None:
            # If there's an edge2, follow it
            states |= followEdges(state.edge2)

    # Return the set of states
    return states

def match(infix, string):
    """Matches the string to the infix regular expression"""
    
    postfix = convertToPostfix(infix)
    nfa = compileToNFA(postfix)

    # The current set of states and the next set of states
    current = set()
    next = set()

    # Add the initial state to the current set.
    current |= followEdges(nfa.initial)
    
    # Loop through each character in the string
    for s in string:
        # Loop through the current set of states
        for c in current:
            # Check if that state is labelled s.
            if c.label == s:
                #Add the edge1 state to the next set.
                next |= followEdges(c.edge1)
        # Set current to next, and clear out next
        current = next
        next = set()

    # Check it the accept state is in the set of current states.
    return (nfa.accept in current)
infixes = ["a.b.c*", "a.(b|d).c*", "(a.(b|d))*", "a.(b.b)*.c", "(a.b)|(c*.d)"]
strings = ["", "abc", "abbc", "abcc", "abad", "abbbc"]

#have it so the user gets a choice of whether they have a infix, or postfix 
#and what they want to do with it

for i in infixes:
    print(convertToPostfix(i))