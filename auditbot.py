# Auditbot, an IRC bot for managing IRC communities

# import jaraco (Need to figure out the exact import semantics)

import importlib

class ab_control(irc.client):
  """The controlling event loop for auditbot, based on the client template in the python Jaraco IRC library."""
  def __init__(self):
    modules = # Not quite sure how to import auditbot components.
    self.components = []
    for module in modules:
      components.append(modules[module]())
