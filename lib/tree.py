class Tree:
  def __init__(self, root = None):
    self.root = root

  def breadth_first_traversal(node):
  result = []
  nodes_to_visit = [node]

  while len(nodes_to_visit) > 0:
    # 1. Remove the first node from the `nodes_to_visit` list
    node = nodes_to_visit.pop(0)
    # 2. Add its value to the result list
    result.append(node['value'])
    # 3. Add its children (if any) to the END of the `nodes_to_visit` list
    nodes_to_visit = nodes_to_visit + node['children']

  return result

  def depth_first_traversal(node, result = []):
  # visit each node (add it to the list of results)
   result.append(node['value'])
  for child in node['children']:
    # visit each child node
    depth_first_traversal(child, result)

  return result






  def get_element_by_id(self, id):
    pass
