# This is a bare-bones version of recipe_book.py without any actual recipes filled in.
# The filled-in version is stored privately outside of git.

from ingredients import *
from setup import *


# SN = Source Names
class SN(object):
  death_co_name = "Death & Co"
  internet = "Internet"
  ekon = "ekon" # recipes I made up


class RecipeBook(object):

  def __init__(self):
    no_comments = Comments(False, "", "", "")

    self._recipes = [
      Recipe("No name", BookSource(SN.death_co_name, 0), [], no_comments),
                   ]

  def __repr__(self):
      return "RecipeBook [recipes: {0}]".format(str(self._recipes))

  """Returns recipe in book, if exists. Otherwise, returns None.
 
  Args:
    recipe_name: String recipe name. Comparison is case-insensitive.

  Returns:
    Recipe object, if exists in book, otherwise None.
  """
  def GetRecipe(self, recipe_name):
    for recipe in self._recipes:
      # Using lower() for case-insensitive comaprison. This doesn't always work for unicode. But good enough for English string comparisons.
      if recipe_name.lower() == recipe._name.lower():
        return recipe
    return None
