from flask import Flask, jsonify, request
import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Cleaning_Data import ingredient_parser
import config  # Assuming you have a separate config.py file
import recommender_sys

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello():
    return "Please add some ingredients to the URL to receive recipe recommendations"


@app.route('/recipe', methods=["GET"])
def recommend_recipe():
    ingredients = request.args.get('ingredients')

    # Assuming the RecSys class is defined in recommender_sys module
    recipe = recommender_sys.RecSys(ingredients)

    response = {}
    count = 0
    for index, row in recipe.iterrows():
        response[count] = {
            'recipe': str(row['recipe']),
            'score': str(row['score']),
            'ingredients': str(row['ingredients']),
            'url': str(row['url'])
        }
        count += 1
    return jsonify(response)


if __name__ == "__main__":
    app.run()
