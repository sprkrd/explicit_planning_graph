

class Graph:

    def __init__(self):
        self._graph_data = []
        self._number_of_edges = 0

    def add_node(self, info):
        self._graph_data.append( (info,[]) )
        return len(self._graph_data) - 1

    def add_edge(self, u, v, info):
        _,adjacency = self._graph_data[u]
        adjacency.append( (info,v) )
        self._number_of_edges += 1

    def get_node_info(self, u):
        if u < 0 or u >= len(self._graph_data):
            return None
        info,_ = self._graph_data[u]
        return info

    def get_edge_info(self, u, v):
        _,adjacency = self._graph_data[u]
        for info,v_ in adjacency:
            if v_ == v:
                return info
        return None

    def get_adjacency(self, u):
        _,adjacency = self._graph_data[u]
        return adjacency

    def get_number_of_nodes(self):
        return len(self._graph_data)

    def get_number_of_edges(self):
        return self._number_of_edges


def default_node_formatter(index, info):
    return str(index)


def default_edge_formatter(u, v, info):
    return ""


def render_graph(graph, outpath, view=False, cleanup=True, node_fmt=default_node_formatter, edge_fmt=default_edge_formatter):
    import graphviz as gv
    g = gv.Digraph("g")
    g.attr("node", shape="circle") 
    for u in range(graph.get_number_of_nodes()):
        info = graph.get_node_info(u)
        g.node(str(u), label=node_fmt(u, info))
    for u in range(graph.get_number_of_nodes()):
        for info, v in graph.get_adjacency(u):
            g.edge(str(u), str(v), label=edge_fmt(u, v, info))
    g.render(outpath, view=view, cleanup=cleanup)


