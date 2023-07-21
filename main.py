#!/usr/bin/env python3
"""
This is a simple visualization of the infamous MU puzzle from Douglas Hofstadter's book, 
"Godel, Escher, Bach: An Eternal Golden Braid".
"""

import graphviz

class AdjacencyList:
    def __init__(self, key):
        self.hashmap = {
            key: []
        }
    
    def add(self, key, value):
        """
        Add a new node to the adjacency list.
        """
        if key not in self.hashmap:
            self.hashmap[key] = [value]
        else:
            self.hashmap[key].append(value)

    def get(self, value):
        """
        Get the adjacent nodes given node's value.
        """
        return self.hashmap[value]

def main():
    # start with the string "MI"
    mi_graph = AdjacencyList("MI")
    mi_graph.add("MI", "MII")
    mi_graph.add("MI", "MIU")

    # bfs queue
    queue = ["MI"]

    # visited set
    visited = set()

    # while queue is not empty (bfs)
    # (for loop for now)
    for i in range(8):
        print(mi_graph.hashmap)

        # dequeue
        node = queue.pop(0)

        # if node is not in visited set
        if node not in visited:
            # add node to visited set
            visited.add(node)

            # get adjacent nodes
            adjacent_nodes = mi_graph.get(node)

            # for each adjacent node
            for adjacent_node in adjacent_nodes:
                # if adjacent node is not in visited set
                if adjacent_node not in visited:
                    # enqueue adjacent node
                    queue.append(adjacent_node)
                    
                    # replace that last "I" with "IU"
                    if adjacent_node[-1] == "I":
                        mi_graph.add(adjacent_node, adjacent_node + "U")

                    # replace all instances of "III" with "U"
                    for i in range(len(adjacent_node) - 2):
                        if adjacent_node[i:i+3] == "III":
                            mi_graph.add(adjacent_node, adjacent_node[:i] + "U" + adjacent_node[i+3:])

                    # delete "UU" from the string
                    for i in range(len(adjacent_node) - 1):
                        if adjacent_node[i:i+2] == "UU":
                            mi_graph.add(adjacent_node, adjacent_node[:i] + adjacent_node[i+2:])

                    mi_graph.add(adjacent_node, adjacent_node + adjacent_node[1:])

    graph = graphviz.Digraph('MuSualizer')

    for k, v in mi_graph.hashmap.items():
        for i in v:
            graph.edge(k, i)
    
    graph.format = 'png'
    graph.render('MuSualizer', view=True)

if __name__ == '__main__':
    main()