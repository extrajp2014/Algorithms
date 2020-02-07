#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
    for i in recipe.keys():
        if i not in ingredients:
            ingredients[i] = 0
        ingredients[i] -= recipe[i]
        if ingredients[i] < 0:
            ingredients[i] += recipe[i]
            return 0
    return recipe_batches(recipe, ingredients) + 1

if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 232, 'butter': 100, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
