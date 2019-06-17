import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression


def find_directed_paths(g, src, dest):
    def find_paths(node, path):
        path_extension = path + (node,)
        if node == dest:
            yield path_extension

        assert node not in path, "Graph has a cycle so is not a DAG: %s" % path_extension
        
        for _, child_node in g.out_edges(node):
            yield from find_paths(child_node, path_extension)

    return list(find_paths(src, tuple()))

def find_all_paths(g, src, dest):
    def find_paths(node, path):
        path_extension = path + (node,)
        if node == dest:
            yield path_extension
        elif node not in path:
            for _, child_node in g.out_edges(node):
                yield from find_paths(child_node, path_extension)

            for child_node, _ in g.in_edges(node):
                yield from find_paths(child_node, path_extension)

    return find_paths(src, tuple())

def is_collider_connection(g, nodeL, node0, nodeR):
    return {(nodeL, node0), (nodeR, node0)} <= set(g.in_edges(node0))

def d_connections(g, node1, node2, given_vars):
    raise NotImplemented()    # Needs to check that no descendants of a collider are in given_vars
    
    connected_paths = []
    for path in find_all_paths(g, node1, node2):
        is_connected = True
        for k in range(1, len(path) - 1):
            print(k, len(path), path)
            if is_collider_connection(g, path[k-1], path[k], path[k + 1]):
                if path[k] not in given_vars:
                    is_connected = False
                    break
            else:
                if path[k] in given_vars:
                    is_connected = False
                    break
        
        if is_connected:
            connected_paths.append(path)
    
    return connected_paths

def path_coefficients(df, dest, model_columns):
    xs = df[model_columns]
    ys = df[dest]
    
    model = LinearRegression().fit(xs, ys)

    return dict(zip(model_columns, [np.round(coeff, 5) for coeff in model.coef_]))

def estimated_coefficients(g, df):
    estimates = []
    for node in sorted(g.nodes):
        parents = [other for other, _ in g.in_edges(node)]

        if len(parents) > 0:
            coeffs = path_coefficients(df, node, parents)

            for parent in sorted(parents):
                estimates.append("%s %s %f" % (parent, node, coeffs[parent]))
    
    print(*sorted(estimates), sep="\n")

def actual_coefficients(local_vars):
    for k, v in sorted(local_vars.items()):
        if k.endswith("_coeff"):
            print("%s = %s" % (k, v))

def do_value_dataframe(g, dataset, fn_name, fn, num_data_elts):
    """
    Override a local function definition temporarily and generate a new dataset.
    NOTE: mocking doesn't seem to work for locally-defined functions.
    """
    from unittest import mock

    with mock.patch.dict(dataset.__dict__, {fn_name: fn}):
        data = [dataset.observation() for _ in range(num_data_elts)]
        df = pd.DataFrame(data, columns=sorted(g.nodes))

        return df

def empirical_total_effect(g, dataset, src, dest, fn1, fn2, num_data_elts=100_000):
    fn_name = "%s_value" % src
    value_1 = do_value_dataframe(g, dataset, fn_name, fn1, num_data_elts)[dest]
    value_2 = do_value_dataframe(g, dataset, fn_name, fn2, num_data_elts)[dest]
    diff = value_2 - value_1
    
    return diff.mean()
