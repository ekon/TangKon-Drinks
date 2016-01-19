import operator

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
my_pantry = [Gin.beefeater, W.buffalo_bourbon, R.goslings, L.cointreau, L.luxardo, L.grand_marnier, L.st_germain, Amari.campari, V.dolin_dry,
V.dolin_blanc, O.egg_white, O.egg_yolk, O.club_soda, O.dry_champagne, G.lemon, G.lime, G.orange, J.lemon, J.lime, J.orange,  B.a,
B.o, B.p, O.simple_syrup, O.ginger_syrup]
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


# TODO: would be nice to have the drink_name as a flag
drink_name = "French 75" #"Dark and Stormy"
missing_ingredients = FindMissingIngredients(drink_name, my_pantry)
print "Missing ingredients for {0} are: {1}".format(drink_name, missing_ingredients)


def PrintIngredients(recipe_name):
  recipe = book.GetRecipe(recipe_name)
  if not recipe:
    return "Error: Could not find recipe name in book."
  print "Ingredients for {0} are: {1}".format(recipe_name, recipe._ingredients)


PrintIngredients(drink_name)

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

PrintMostUsedIngredients()

