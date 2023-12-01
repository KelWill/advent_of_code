import math
class Vector:
  def __init__(self, *args):
    self.loc = list(args)
  
  def __add__ (self, other):
    self._assert_same_dimensions(other)
    updated = []
    for i in range(len(self.loc)):
      updated.append(self.loc[i] + other.loc[i])
    return Vector(*updated)
  
  def __iter__ (self):
    for v in self.loc:
      yield v

  def __sub__ (self, other):
    self._assert_same_dimensions(other)
    updated = []
    for i in range(len(self.loc)):
      updated.append(self.loc[i] - other.loc[i])
    return Vector(*updated)

  def __str__ (self):
    return str(self.loc)

  def _assert_same_dimensions(self, other):
    if len(other.loc) != len(self.loc):
      raise Evception(f"cannot do operations on {self.loc} and {other.loc} because they don't have the same dimensions")

  def chess_distance (self, other):
    self._assert_same_dimensions(other)
    return max([abs(self.loc[i] - other.loc[i]) for i in range(len(self.loc))])

  def distance (self, other):
    vec = self - other
    return math.sqrt(sum(v**2 for v in vec))