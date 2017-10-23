# Importing essentials

import sys
import inspect, os
import random
import glob
import networkx as nx

# Definitons

sys.path.append('./modules')
fl = glob.glob('modules/*.py')
classes = {}

# Find and list all modules
for i in range(len(fl)):
    fl[i] = fl[i].split('/')[1]
    fl[i] = fl[i][0:(len(fl[i])-3)]
    classes[fl[i]] = (getattr(__import__(fl[i]),fl[i]))

for name, obj in inspect.getmembers(sys.modules[__name__]):
    if inspect.isclass(obj):
        classes[name] = obj

# Initializing graph
G = nx.DiGraph()
for x in classes.keys():
    G.add_node(classes[x]().inp)
    G.add_node(classes[x]().out)

# Adding modules to graph
for x in classes.keys():
    if type(classes[x]().inp) == list:
        for inp in classes[x]().inp:
            G.add_edge(inp, classes[x]().out, weight=x)
    else:
        G.add_edge(classes[x]().inp, classes[x]().out, weight=x)

# Main stuff

def execute(stack, val):
    # Execute the stack
    for x in stack:
        tmp = classes[x]()
        val = tmp.do(val)
    return val

def create_program_stack(inp, out, val):
    # Improve stacker function
    shp = nx.shortest_path(G, inp, out)
    stack = []
    for x in xrange(len(shp)-1):
        i = shp[x]
        o = shp[x+1]
        stack.append(G.get_edge_data(i,o)['weight'])
    # Logging - print stack
    return execute(stack, val)
