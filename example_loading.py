#!/usr/bin/env python3


import pickle as pkl
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pklpath", help="path to the pkl file",
            default="pkl_graphs/imagine_104_states.pkl")
    args = parser.parse_args()

    with open(args.pklpath, "rb") as f:
        graph = pkl.load(f)

    # Getting the number of nodes and edges is straightforward enough
    print("Number of nodes:", graph.get_number_of_nodes())
    print("Number of edges:", graph.get_number_of_nodes())
    
    # Nodes have associated information. In the graphs I'm storing, this
    # information is just a string representation of the state
    print("State 0:", graph.get_node_info(0))

    # Same for edges. If you happen to know there's an edge from u to v,
    # then the edge information can be queried by graph.get_edge_info(u, v).
    # In the graphs I'm storing, edge information is a tuple in which the first
    # element is a string representation of the action that causes the transition,
    # and the second element is the cost of the action (or, in graph terminology,
    # the edge weight).

    # Normally, you won't know before hand whether there's an edge between
    # u, v. The graph is stored as an adjacency list, so you can query the
    # get_adjacency method with a node index u, and this will tell you which
    # nodes can be reached via an outgoing edge from v. These nodes are
    # returned as a list of tuples. The first element of the tuple is the
    # edge information, and the second element of the tuple is the destination
    # node. See the next example:
    for u in range(graph.get_number_of_nodes()):
        for edge_info, v in graph.get_adjacency(u):
            label, cost = edge_info
            print(f"Edge between {u} and {v}: label={label}, cost={cost}")

    # That should be enough to use the graph objects!


if __name__ == "__main__":
    main()

