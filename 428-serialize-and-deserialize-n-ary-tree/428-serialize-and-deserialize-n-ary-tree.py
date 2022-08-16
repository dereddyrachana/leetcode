"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Codec:
    def serialize(self, root: 'Node') -> str:
        if not root:
            return ""
        out = ""
        out+=str(root.val)
        for node in root.children:
            out+=","+self.serialize(node)
        out+=',#'
        return out
	
    def deserialize(self, data: str) -> 'Node':
        if len(data) == 0:
            return None
        def help(X):
            root = Node(int(X.pop(0)),children=[])
            while X[0]!='#':
                root.children.append(help(X))
            X.pop(0)
            return root
        return help(data.split(","))
        