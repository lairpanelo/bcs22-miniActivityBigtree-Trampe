from bigtree import Node

pathDict = {
    "a": {"name": "RM"},
    "a/b": {"name": "Jin"},
    "a/c": {"name": "JHope"},
    "a/b/d": {"name": "Jungkook"},
    "a/b/e": {"name": "V"},
    "a/c/f": {"name": "Suga"},
    "a/c/f/g": {"name": "Jimin"}
}

created_nodes = {"a": Node("RM", data=dict["a"])}

for path, node_data in dict.items():
    if path != "a":
        nodes = path.split("/")
        current_node = created_nodes[nodes[0]]
        for node in nodes[1:]:
            if node not in created_nodes:
                created_nodes[nodes] = Node(node_data["name"], parent=current_node, data=dict[path])
            current_node = created_nodes[node]
created_nodes["a"].show(attr_list=["name"])
