# Author: Louie Mølgaard Hessellund <hessellundlouie@gmail.com>

from typing import Dict, Tuple

from pyhgf.typing import AdjacencyLists, Edges
from pyhgf.utils import add_edges


def add_parent(
<<<<<<< HEAD
<<<<<<< HEAD
    attributes: Dict, edges: Edges, index: int, coupling_type: str, mean: float
) -> Tuple[Dict, Edges]:
    r"""Add a new continuous-state parent node to the attributes and edges of an
    existing network.
=======
    attributes: Dict, edges: Edges, index: int, coupling_type: str
) -> Tuple[Dict, Edges]:
    r"""Add new continuous-state parent node to the attributes and edges of an existing
    network.
>>>>>>> ab94860 (latent_update function moved to updates.structure.py. Renamed to add_parent)
=======
    attributes: Dict, edges: Edges, index: int, coupling_type: str, mean: float
) -> Tuple[Dict, Edges]:
    r"""Add a new continuous-state parent node to the attributes and edges of an
    existing network.
>>>>>>> 1f7b8c2 (initial update for-loop added to notebook. Mean of new parent node added to add_parent function)

    Parameters
    ----------
    attributes :
        The attributes of the existing network.
    edges :
        The edges of the existing network.
    index :
        The index of the node you want to connect a new parent node to.
    coupling_type :
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 1f7b8c2 (initial update for-loop added to notebook. Mean of new parent node added to add_parent function)
        The type of coupling you want between the existing node and it's new parent.
        Can be either "value" or "volatility".
    mean :
        The mean value of the new parent node.
<<<<<<< HEAD
=======
        The type of coupling you want between the existing node and it's new parent. Can
        be either "value" or "volatility".
>>>>>>> ab94860 (latent_update function moved to updates.structure.py. Renamed to add_parent)
=======
>>>>>>> 1f7b8c2 (initial update for-loop added to notebook. Mean of new parent node added to add_parent function)

    Returns
    -------
    attributes :
        The updated attributes of the existing network.
    edges :
        The updated edges of the existing network.

    """
    # Get index for node to be added
    new_node_idx = len(edges)

    # Add new node to attributes
    attributes[new_node_idx] = {
<<<<<<< HEAD
<<<<<<< HEAD
        "mean": mean,
        "expected_mean": mean,
=======
        "mean": 0.0,
        "expected_mean": 0.0,
>>>>>>> ab94860 (latent_update function moved to updates.structure.py. Renamed to add_parent)
=======
        "mean": mean,
        "expected_mean": mean,
>>>>>>> 1f7b8c2 (initial update for-loop added to notebook. Mean of new parent node added to add_parent function)
        "precision": 1.0,
        "expected_precision": 1.0,
        "volatility_coupling_children": None,
        "volatility_coupling_parents": None,
        "value_coupling_children": None,
        "value_coupling_parents": None,
        "tonic_volatility": -4.0,
        "tonic_drift": 0.0,
        "autoconnection_strength": 1.0,
        "observed": 1,
        "temp": {
            "effective_precision": 0.0,
            "value_prediction_error": 0.0,
            "volatility_prediction_error": 0.0,
        },
    }

    # Add new AdjacencyList with empty values, to Edges tuple
    new_adj_list = AdjacencyLists(
        node_type=2,
        value_parents=None,
        volatility_parents=None,
        value_children=None,
        volatility_children=None,
        coupling_fn=(None,),
    )
    edges = edges + (new_adj_list,)

    # Use add_edges to integrate the altered attributes and edges
    attributes, edges = add_edges(
        attributes=attributes,
        edges=edges,
        kind=coupling_type,
        parent_idxs=new_node_idx,
        children_idxs=index,
    )

    # Return new attributes and edges
    return attributes, edges
