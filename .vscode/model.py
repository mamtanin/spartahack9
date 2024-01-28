import os
import base64
import requests
from openai import OpenAI
from fastapi import FastAPI

app = FastAPI()

# Open AI API setup
key = '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'
client = OpenAI(api_key=key)
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {key}"
}


ingredients = {}
recipes = {}

recycling = {'Composting':''}

#Encodes image for GPT interpretation
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

#Tells gpt was to act like, tells the prompt
def prompt(system: str, text: str):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": system},
            {"role": "user", "content": text}
        ]
    )

    return completion.choices[0].message.content


#Src is image. MUST BE ENCODED, prompt to analyze image
def vision(src, text: str):

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": text
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{src}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }
    ans = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload).json()
    return ans['choices'][0]['message']['content']


def recycle():
    recycling['Composting'] = prompt('You are an expert on food waste and a hobbyist that likes to turn leftover food into compost and use other methods in recycling food waste sustainably.', 'Tell me how to reuse this leftover food in a sustainable manner. Tell me how to turn this into compost and which of my ingredients are good for composting and which are not. Tell me the steps in numerical order. Ingredients: ' + ','.join(ingredients.keys()))
    with open("./static/composting.txt", "w") as recycle_file:
        recycle_file.write(recycling['Composting'])
    print(recycling['Composting'])


def read_ingredients():
    # Storage of images to upload
    
    script_dir = os.path.dirname(os.path.realpath(__file__))

    folder_name = 'images_storage'

    # Get the path of the folder
    path = os.path.join(script_dir, folder_name)
    print(path)
    # Get a list of all files in the folder
    images = os.listdir(path)
    for image in images[1:]:
        base64_image = encode_image(path + '/' + image)
        ingredient = vision(base64_image,"Tell me what item of food this is as simply as possible. Only state the food itself, no extra words").strip('.').title()
        ingredients[ingredient] = path + '/' + image
    

    ingredients_str = ','.join(ingredients.keys())
    print(ingredients_str)

    recipe = prompt('You are a chef that is capable of crafting recipes from a list of ingredients.',
                    'Create a recipe using only the following list of ingredients and common spices found in a household. You do not have to use all ingredients, just make a complete recipe: ' + ingredients_str +
                    '. Re-list the ingredients and amounts. Then list the steps to cook step by step. List the title of within closed paranthesis like (Recipe Name Goes Here).  Start the ingredients section with (Ingredients)'
                    'Start the steps section with (Steps)')

    print(recipe)
    with open("./static/recipe.txt", "w") as recipe_file:
        recipe_file.write(recipe)
    
    recipes[recipe[recipe.find('(') + 1:recipe.find(')')]] = '' + recipe[recipe.find('(Ingredients)'):].strip('()')
    '''
    
    '''
    recipe = prompt('You are a chef that is capable of crafting recipes from a list of ingredients.',
                    'Create a recipe using only the following list of ingredients and common spices found in a household. You do not have to use all ingredients, just make a complete recipe. It has to be significantly different from' + list(recipes.keys())[0] + ': ' + ingredients_str +
                    '. Re-list the ingredients and amounts. Then list the steps to cook step by step. List the title of within closed paranthesis like (Recipe Name Goes Here).  Start the ingredients section with (Ingredients)'
                    'Start the steps section with (Steps)')

    print(recipe)
    with open("./static/recipe1.txt", "w") as recipe_file:
        recipe_file.write(recipe)

    recipes[recipe[recipe.find('(') + 1:recipe.find(')')]] = '' + recipe[recipe.find('(Ingredients)'):].strip('()')


@app.get("/")
def read_root():
    return "Hi"


@app.get("/ingredients")
def read_food():
    return ingredients


@app.get("/recipes")
def read_recipes():
    return recipes


@app.get("/recycling")
def read_recycling():
    return recycling


read_ingredients()
recycle()