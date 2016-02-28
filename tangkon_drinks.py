import argparse
import operator
import sys

from ingredients import *
from recipe_book import *


"""Returns True if can make given recipe.

TODO: add logic about what type of substitutions I can actually do.

Args:
  existing_ingredients: List of ingredients that I have.
  subs_allowed: True if substitutions are allowed.
  num_subs_allowed: If substitutions are allowed, number of ingredients that can be substituted.
  recipe_ingredients: Ingredients needed to make a given recipe.

Returns:
  True if can make recipe.
"""
def CanMakeRecipe(existing_ingredients, subs_allowed, num_subs_allowed, recipe_ingredients):
  # thought about using set differences but with subsitutions it's not really any less code anyway
  subs_made = 0
  for ingredient in recipe_ingredients:
    if ingredient not in existing_ingredients:
      if not subs_allowed or subs_made == num_subs_allowed:
        return False
      subs_made += 1
  return True


"""Returns list of recipes that I can make.

Args:
  existing_ingredients: List of ingredients that I have.
  subs_allowed: True if substitutions are allowed.
  num_subs_allowed: If substitutions are allowed, number of ingredients that can be substituted.

Returns:
  List of recipes that can be made.
"""
def WhatCanIMake(existing_ingredients, subs_allowed, num_subs_allowed):
  recipes_can_make = []
  for recipe in book._recipes:
    if CanMakeRecipe(existing_ingredients, subs_allowed, num_subs_allowed, recipe._ingredients):
      recipes_can_make.append(recipe)
  return recipes_can_make

"""Prints recipes that I can make."""
def PrintWhatICanMake():
  i_can_make = WhatCanIMake(my_pantry, False, 0)
  print "I can make {0} recipes: {1}".format(len(i_can_make), i_can_make)


"""Given a recipe name, find ingredients not in my pantry.

Args:
  recipe_name: String recipe name. Comparison is case-insensitive.
  existing_ingredients: List of ingredients I already have.

Returns:
  List of missing ingredients.
""" 
def FindMissingIngredients(recipe_name, existing_ingredients):
  recipe = book.GetRecipe(recipe_name)
  if not recipe:
    return "Error: Could not find recipe name in book."
  missing_ingredients = []
  for ingredient in recipe._ingredients:
    if ingredient not in existing_ingredients:
      missing_ingredients.append(ingredient)
  return missing_ingredients

"""Prints missing ingredients.

Args:
  recipe_name: String recipe name. Comarison is case-insensitive.
"""
def PrintMissingIngredients(recipe_name):
  missing_ingredients = FindMissingIngredients(recipe_name, my_pantry)
  print "Missing ingredients for {0} are: {1}".format(recipe_name, missing_ingredients)

"""Prints ingredients needed for a given recipe.

Args:
  recipe_name: String recipe name. Comparision is case-insensitive.
"""
def PrintIngredients(recipe_name):
  recipe = book.GetRecipe(recipe_name)
  if not recipe:
    return "Error: Could not find recipe name in book."
  print "Ingredients for {0} are: {1}".format(recipe_name, recipe._ingredients)


"""Prints a sorted map of ingredient to # recipes used in in order of most-used first.

TODO: This function is a decent approximation for what ingredients I want, but isn't good enough.
This doesn't optimize for actually being able to make more drinks. What I really want is a
function that will tell me which ingredient I should buy that will let me make the most number of
new drinks given my existing ingredients. For example, tiki drinks require multiple rums, if I
only get the most used rum in all of the drinks that will not be enough for me to be able to make
those drinks, unless I also have those other rums, or want to do substitutions.
"""
def PrintMostUsedIngredients():
  ingredient_frequency = {}
  for recipe in book._recipes:
    for ingredient in recipe._ingredients:
      if ingredient in ingredient_frequency:
        ingredient_frequency[ingredient] += 1
      else:
        ingredient_frequency[ingredient] = 1
  ingredients_sorted_by_freq = sorted(ingredient_frequency.items(), key=operator.itemgetter(1),
  reverse=True)
  print "Most used ingredients are: {0}".format(str(ingredients_sorted_by_freq))


"""Prints most-used ingredients that, if I got any single one, would allow to me to make more recipes.

Args:
  existing_ingredients: List if existing ingredients (e.g. my_pantry).

Returns:
  List of "ingredient name" to number of new recipes it would "unlock".
"""
def PrintOneAdditionalIngredient(existing_ingredients):
  pantry = set(existing_ingredients)

  # Map from ingredient name -> list of recipes that could be made if I had this one additional
  # ingredient.
  ingredient_frequency = {}
  for recipe in book._recipes:
    missing_ingredients = set(recipe._ingredients) - pantry
    if len(missing_ingredients) == 1:
      missing_ingredient = missing_ingredients.pop()
      if missing_ingredient in ingredient_frequency:
        ingredient_frequency[missing_ingredient].append(recipe._name)
      else:
        ingredient_frequency[missing_ingredient] = [recipe._name]

  ingredients_sorted_by_freq = sorted(ingredient_frequency.items(), key=lambda entry: len(entry[1]),
  reverse=True)
  print "Most used one-additional-ingredients are: {0}".format(str(ingredients_sorted_by_freq))


"""Given an ingredient, print the recipes that can be made with it.

Args:
   ingredient: Ingredient from ingredients.py.
"""
def GetRecipesForIngredient(ingredient):
  recipes = []
  for recipe in book._recipes:
    for recipe_ingredient in recipe._ingredients:
      if recipe_ingredient == ingredient:
        recipes.append(recipe)
  print "\n Recipes that can be made with {0}: {1}".format(str(ingredient), str(recipes))
 
#GetRecipesForIngredient(Amari.fernet_branca)


book = RecipeBook()
my_pantry = [Gin.beefeater, W.buffalo_bourbon, W.rittenhouse_rye, R.goslings, L.cointreau, L.luxardo, L.grand_marnier, L.st_germain, Amari.fernet_branca, Amari.campari, V.dolin_dry, V.dolin_blanc, O.egg_white, O.egg_yolk, O.club_soda, O.dry_champagne, G.lemon, G.lime, G.orange, G.brandied_cherry, G.cherry, J.lemon, J.lime, J.orange,  B.a, B.o, B.p, O.simple_syrup, O.ginger_syrup]


def main(argv):
  arg_parser = argparse.ArgumentParser(description="TangKon Drinks. Your online, friendly bar helper.")
  arg_parser.add_argument("--get_recipes_for_ingredient", help="Get recipes that could be created with the given ingredient, regardless of pantry availability.")
  arg_parser.add_argument("--print_most_used_ingredients", help="Prints out a list of ingredients sorted by most used in the recipes.", action="store_true")
  arg_parser.add_argument("--print_one_additional_ingredient", help="Prints which recipes I can make if I had just one additional ingredient, in order of ingredients that would allow me to make the most new recipes.", action="store_true")
  arg_parser.add_argument("--print_what_i_can_make", help="Prints which recipes I can make with the items in my pantry.", action="store_true")
  arg_parser.add_argument("--print_ingredients", help="Prints ingredients for a given recipe name")
  arg_parser.add_argument("--print_missing_ingredients", help="Prints missing ingredients for a given recipe name")
  args = arg_parser.parse_args()

  if args.get_recipes_for_ingredient:
    print "TODO: convert between string and class/member name."
  if args.print_most_used_ingredients:
    PrintMostUsedIngredients()
  if args.print_one_additional_ingredient:
    PrintOneAdditionalIngredient(my_pantry)
  if args.print_what_i_can_make:
    PrintWhatICanMake()
  if args.print_ingredients:
    PrintIngredients(args.print_ingredients)
  if args.print_missing_ingredients:
    PrintMissingIngredients(args.print_missing_ingredients)

if __name__ == "__main__": main(sys.argv[1:])
