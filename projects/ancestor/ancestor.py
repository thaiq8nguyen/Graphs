
import os
import sys
sys.path.append("../graph")
from graph import Graph




def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for v in range(1, 12):
        g.add_vertex(v)
    for a in ancestors:
        g.add_edge(a[0], a[1])

    paths = []

    for a in g.vertices:
        if g.dfs_recursive(a, starting_node) is not None and\
                len(g.dfs_recursive(a, starting_node)) > 0:
            paths.append(g.dfs_recursive(a, starting_node))

    if len(paths) == 1:
        return -1

    ret_path = paths[0]
    for p in paths:
        if len(p) > len(ret_path) or\
                (len(p) == len(ret_path) and p[0] < ret_path[0]):
            ret_path = p

    return ret_path[0]
