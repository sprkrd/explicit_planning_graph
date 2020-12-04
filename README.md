# Explicit generation of planning graphs

Just a simple tool to generate explicit planning graphs from PDDL domain/problem pairs.

Mind that this repository has submodules. To clone it properly, please use:

```
git clone --recurse-submodules https://github.com/sprkrd/explicit_planning_graph.git
```

If you've already cloned the repository and you want to fetch the submodules too, use

```
git submodule update --init --recursive
```

If you only want to load and use the pregenerated graphs, the submodules are
not necessary and you can get away if you don't clone it.

You can find pregenerated graphs in the `pkl_graph` folder. Check out
`example_loading.py` to get a feel on how to load and use the generated
graphs.

You can also check the `pdf_graphs` folder for renders of the graphs.

The `graphgen.py` script generates a new graph from a PDDL domain file
and a PDDL problem file. Just invoke it without arguments (or with the -h)
argument to learn about its usage:

```
./graphgen.py -h
```

## Dependencies

This project runs in Python3. Python2 is not supported, but basic support can
be provided if needed (at least for using the Graph class defined in
`graph.py`).

There are no dependencies aside from `graphviz`, and even this is not necessary
if you don't plan on rendering PDF files for the graphs). The rest is already
included (provided you clone the submodules appropriately).

To install graphviz

```
pip install graphviz
```

Feel free to install it in a virtual environment or in the user space if you
want to (although, again, it is not needed if you don't ever call the
`render_graph` function in `graph.py`).

