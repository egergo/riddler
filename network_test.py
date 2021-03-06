import riddler_node as node

"""
alice = node.node("alice", "localhost")
bob = node.node("bob", "localhost", 9988)
"""
alice = node.node("alice", "panda0.personal.es.aau.dk")
relay = node.node("relay", "panda1.personal.es.aau.dk")
bob = node.node("bob", "panda2.personal.es.aau.dk")
mhu = node.node("mhu", "localhost")
"""
alice = node.node("alice", "n52")
bob = node.node("bob", "n53")
"""


alice.add_dest(bob)
bob.add_dest(alice)
bob.set_enable_ratio(True)
