#!/usr/bin/env python3

import argparse
import warnings
import pickle as pkl

from planning_toolbox.parser import parse_file
from graph import Graph, render_graph

# warnings.simplefilter("ignore")


def edge_fmt(u, v, info):
    return f"{info[0]} ({info[1]})"


def state_label(state):
    return "{" + ", ".join(sorted(map(str,state.predicates))) + "}"


def generate_graph(problem):
    graph = Graph()
    visited_states = set()
    initial_state = problem.get_initial_state()
    state_to_index = {initial_state: graph.add_node(state_label(initial_state))}
    stack = [problem.get_initial_state()]
    i = 0
    while stack:
        if (i%100 == 0):
            print("checkpoint", len(stack), graph.get_number_of_nodes(), graph.get_number_of_edges())
        state = stack.pop()
        if state not in visited_states:
            visited_states.add(state)
            state_index = state_to_index[state]
            for a in state.applicable_actions():
                edge_info = (a.short_str(), a.get_cost(state))
                next_state = a.apply(state)
                try:
                    next_state_index = state_to_index[next_state]
                except KeyError:
                    next_state_index = graph.add_node(state_label(next_state))
                    state_to_index[next_state] = next_state_index
                graph.add_edge(state_index, next_state_index, edge_info)
                stack.append(next_state)
        i += 1
    return graph

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("domainpath", help="Filepath to LISP-like text file")
    parser.add_argument("problempath", help="Filepath to LISP-like text file")
    parser.add_argument("out", help="out pickle file (without file extension)")
    parser.add_argument("--output_render", help="output file (wo file extension) to render the graph (leave unset if no render is needed)")
    args = parser.parse_args()

    domain = parse_file(args.domainpath, "domain")
    problem = parse_file(args.problempath, "problem", domain)

    graph = generate_graph(problem)
    print("Number of nodes: ", graph.get_number_of_nodes())
    print("Number of edges: ", graph.get_number_of_edges())

    print("Storing pkl...")
    with open(args.out+".pkl", "wb") as f:
        pkl.dump(graph, f)

    if args.output_render:
        print("Storing pdf...")
        render_graph(graph, args.output_render, view=True, cleanup=True, edge_fmt=edge_fmt)


if __name__ == "__main__":
    main()

