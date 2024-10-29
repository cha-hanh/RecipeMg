import json

# Function to load recipe data from file
def load_recipes():
    try:
        with open('recipes.json', 'r') as file:
            recipes = json.load(file)
    except FileNotFoundError:
        recipes = []
    return recipes

# Function to save recipe data to file
def save_recipes(recipes):
    with open('recipes.json', 'w') as file:
        json.dump(recipes, file, indent=4)

# Function to add a recipe
def add_recipe():
    recipes = load_recipes()
    recipe_name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    instructions = input("Enter instructions: ")

    recipe = {
        'name': recipe_name,
        'ingredients': ingredients,
        'instructions': instructions
    }

    recipes.append(recipe)
    save_recipes(recipes)
    print(f"Recipe '{recipe_name}' added successfully!\n")

# Function to view all recipes
def view_recipes():
    recipes = load_recipes()
    if not recipes:
        print("No recipes found.\n")
    else:
        print("---- All Recipes ----")
        for idx, recipe in enumerate(recipes, start=1):
            print(f"Recipe {idx}:")
            print(f"Name: {recipe['name']}")
            print("Ingredients:", ', '.join(recipe['ingredients']))
            print("Instructions:", recipe['instructions'])
            print()
        print()

# Main function
def main():
    print("Welcome to the Recipe Manager!")
    while True:
        print("Select an option:")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")
        print()

        if choice == '1':
            add_recipe()
        elif choice == '2':
            view_recipes()
        elif choice == '3':
            print("Exiting the Recipe Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()
