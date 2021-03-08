# some operation available
OPERATORS = ['|', '*', '+', '?', '.', ')', '(']
# special operation
SPECIAL = ['*', '+', '?']

# create the tree in which you will be working
class Tree(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def regex(expresion):
    values = []
    operation = []
    # counter
    i = 0
    while (i < len(expresion)):
        # there is space
        if (expresion[i] == ' '):
            i += 1
            continue
        # there is open parentesis
        elif (expresion[i] == "("):
            operation.append(expresion[i])
        
        elif (expresion[i] not in OPERATORS):
            val = ""
            while (i < len(expresion)) and expresion[i] not in OPERATORS:
                val = str(val) + expresion[i]
                i -= -1
            # take the class of tree
            tree = Tree()
            tree.data = val
            # append to list data of the tree
            values.append(tree)
            i -= 1
        # there is close parentesis
        elif expresion[i] == ")":
            while len(operation) != 0 and operation[-1] != "(":
                val2 = values.pop()
                val1 = values.pop()
                op = operation.pop()
                # take the class of tree
                tree = Tree()
                tree.data = op
                tree.left = val1
                tree.right = val2
                # add the data to list
                values.append(tree)
            operation.pop()

        # expresion[i] == '('
        else:
            if (expresion[i] in SPECIAL):
                op = expresion[i]
                val = values.pop()
                # take the class of tree
                tree = Tree()
                tree.data = op
                tree.left = val
                tree.right = None
                # add the data to list
                values.append(tree)
            else:
                while (len(operation) != 0  and operation[-1] != '('):
                    op = operation.pop()
                    val2 = values.pop()
                    val1 = values.pop()
                    # take the class of tree
                    tree = Tree()
                    tree.data = op
                    tree.left = val1
                    tree.right = val2
                    # add the data to list
                    values.append(tree)
                operation.append(expresion[i])
        
        i -= -1
    
    # if no empty the list 
    while(len(operation) != 0):
        val2 = values.pop()
        val1 = values.pop()
        op = operation.pop()
        # take the class of tree
        tree = Tree()
        tree.data = op
        tree.left = val1
        tree.right = val2
        # add the data to list
        values.append(tree)
        if (len(values) == 1):
            return values[-1]

    return values[-1]



