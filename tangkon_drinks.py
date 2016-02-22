import argparse
import operator
import sys

from ingredients import *
from recipe_book import *


# TODO: add logic about what type of substitutions I can actually do.
def CanMakeRecipe(existing_ingredients, subs_allowed, num_missing_allowed, recipe_ingredients):
  # thought about using set differences but with subsitutions it's not really any less code anyway
  subs_made = 0
  for ingredient in recipe_ingredients:
    if ingredient not in existing_ingredients:
      if not subs_allowed or subs_made == num_missing_allowed:
        return False
      subs_made += 1
  return True


# ingredients = list of ingredients that I have
# subs_allowed = bool, true = allowed to make substitutions. TODO: define substitution rules
# num_missing_allowed = int, number of allowed ingredients to be missing
def WhatCanIMake(existing_ingredients, subs_allowed, num_missing_allowed):
  recipes_can_make = []
  for recipe in book._recipes:
    if CanMakeRecipe(existing_ingredients, subs_allowed, num_missing_allowed, recipe._ingredients):
      recipes_can_make.append(recipe)
  return recipes_can_make


book = RecipeBook()
my_pantry = [Gin.beefeater, W.buffalo_bourbon, W.rittenhouse_rye, R.goslings, L.cointreau, L.luxardo, L.grand_marnier, L.st_germain, Amari.fernet_branca, Amari.campari, V.dolin_dry, V.dolin_blanc, O.egg_white, O.egg_yolk, O.club_soda, O.dry_champagne, G.lemon, G.lime, G.orange, G.brandied_cherry, G.cherry, J.lemon, J.lime, J.orange,  B.a, B.o, B.p, O.simple_syrup, O.ginger_syrup]


def PrintWhatICanMake():
  i_can_make = WhatCanIMake(my_pantry, False, 0)
  print "I can make {0} recipes: {1}".format(len(i_can_make), i_can_make)



# Given a recipe name, find ingredients not in my pantry.
#
# TODO: would be good to not have to have an exact name on the drink name (e.g. regex, lower case
# all).
#
# Args:
#  recipe_name: string, must exactly match string names of recipes in RecipeBook.
#  existing_ingredients: list of ingredients I already have
def FindMissingIngredients(recipe_name, existing_ingredients):
  recipe = book.GetRecipe(recipe_name)
  if not recipe:
    return "Error: Could not find recipe name in book."
  missing_ingredients = []
  for ingredient in recipe._ingredients:
    if ingredient not in existing_ingredients:
      missing_ingredients.append(ingredient)
  return missing_ingredients

# TODO: make case-insensitive.
def PrintMissingIngredients(recipe_name):
  missing_ingredients = FindMissingIngredients(recipe_name, my_pantry)
  print "Missing ingredients for {0} are: {1}".format(recipe_name, missing_ingredients)

# TODO: make case-insensitive.
def PrintIngredients(recipe_name):
  recipe = book.GetRecipe(recipe_name)
  if not recipe:
    return "Error: Could not find recipe name in book."
  print "Ingredients for {0} are: {1}".format(recipe_name, recipe._ingredients)


#PrintIngredients(drink_name)

# Prints a sorted map of ingredient to # recipes used in in order of most-used first.
# TODO: right now it prints in reverse order, fix that.
# TODO: This function is a decent approximation for what ingredients I want, but isn't good enough.
# This doesn't optimize for actually being able to make more drinks. What I really want is a
# function that will tell me which ingredient I should buy that will let me make the most number of
# new drinks given my existing ingredients. For example, tiki drinks require multiple rums, if I
# only get the most used rum in all of the drinks that will not be enough for me to be able to make
# those drinks, unless I also have those other rums, or want to do substitutions.
def PrintMostUsedIngredients():
  ingredient_frequency = {}
  for recipe in book._recipes:
    for ingredient in recipe._ingredients:
      if ingredient in ingredient_frequency:
        ingredient_frequency[ingredient] += 1
      else:
        ingredient_frequency[ingredient] = 1
  ingredients_sorted_by_freq = sorted(ingredient_frequency.items(), key=operator.itemgetter(1))
  print "Most used ingredients are: {0}".format(str(ingredients_sorted_by_freq))

#PrintMostUsedIngredients()

# Given an ingredient, list the recipes that can be made with it.
#
# Args:
#   ingredient: ingredient from ingredients.py
def GetRecipesForIngredient(ingredient):
  recipes = []
  for recipe in book._recipes:
    for recipe_ingredient in recipe._ingredients:
      if recipe_ingredient == ingredient:
        recipes.append(recipe)
  print "\n Recipes that can be made with {0}: {1}".format(str(ingredient), str(recipes))
 
#GetRecipesForIngredient(Amari.fernet_branca)

def main(argv):
  arg_parser = argparse.ArgumentParser(description="TangKon Drinks. Your online, friendly bar helper.")
  arg_parser.add_argument("--get_recipes_for_ingredient", help="Get recipes that could be created with the given ingredient, regardless of pantry availability.")
  arg_parser.add_argument("--print_most_used_ingredients", help="Prints out a list of ingredients sorted by most used in the recipes.", action="store_true")
  arg_parser.add_argument("--print_what_i_can_make", help="Prints which recipes I can make with the items in my pantry.", action="store_true")
  arg_parser.add_argument("--print_ingredients", help="Prints ingredients for a given recipe name")
  arg_parser.add_argument("--print_missing_ingredients", help="Prints missing ingredients for a given recipe name")
  args = arg_parser.parse_args()

  if args.get_recipes_for_ingredient:
    print "TODO: convert between string and class/member name."
  if args.print_most_used_ingredients:
    PrintMostUsedIngredients()
  if args.print_what_i_can_make:
    PrintWhatICanMake()
  if args.print_ingredients:
    PrintIngredients(args.print_ingredients)
  if args.print_missing_ingredients:
    PrintMissingIngredients(args.print_missing_ingredients)

if __name__ == "__main__": main(sys.argv[1:])
