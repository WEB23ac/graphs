

def get_parent(ancestors, current_node):
    for (parent, child) in ancestors:
        if child == current_node:
            return parent


def earliest_ancestor(ancestors, starting_node, counter=-1):

    # * returns parent or None
    parent = get_parent(ancestors, starting_node)
# * if no parent, check counter to determine returning -1 or current-earliest ancestor
    if parent is None:
        if counter == -1:
            return counter
        else:
            return starting_node
# * If a parent is found, call e_a function recursively with parent and incremented counter
    else:
        counter += 1
        return earliest_ancestor(ancestors, parent, counter)
