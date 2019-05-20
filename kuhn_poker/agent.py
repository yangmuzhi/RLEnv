"""
agents for kuhn poker
"""


# type: terminate, decision node
#
def TREE():
    return defaultdict(lambda:{"type": None,
                            "value": 0,
                            "action": [],
                            "child": [],
                            "parent": [],
                            "value_history":[]
                            })

def tree_search(node):
    """
    往后看一步
    Args:
        node 节点
    """
    def _tree_search_recursive(node):
        value = None
        if node['type'] == 'terminate':
            next_node = None
            value = node['value']
            return value
        else:
            next_node = node['child']
            if next_node:
                return _tree_search_recursive(next_node)
            else:
                return None

class Agent:
    """
    每个agent自己要根据比赛记录生成一棵树
    """

    def __init__(self, name, actions, init_tree=None):
        self.name = name
        if init_tree:
            self.Tree = init_tree
        else:
            self.Tree = self._build_tree()

    def _build_tree(self):
        return TREE()

    def growing_tree(self, h_dict):
        h = list(h_dict.values())[-1]

    def choose_action(self, state):
        """
        根据 child
        """

    def update(self):
        pass
