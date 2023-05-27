import streamlit as st
import pandas as pd
from PIL import Image
from recommender_sys import RecSys
from Cleaning_Data import ingredient_parser
import nltk

def make_clickable(name, link):
    return f'<a target="_blank" href="{link}">{name}</a>'

def replace(text, link):
    return st.markdown(make_clickable(text, link), unsafe_allow_html=True)

image = Image.open("Data/cook-jd-640x230.jpg")
st.image(image)
st.markdown("# *What's Cooking?*")

st.markdown("## Given a list of ingredients, what different recipes can I make?")
st.markdown("For example, what recipes can you make with the ingredients you have?")
st.markdown("My web app will look through over 4500 recipes to find matches for you.")

st.text("")
st.write("For more details and to explore further, check out this [link](https://github.com/Nourshosharah/Chef_Recommendation_sys)")

ingredients = st.text_input("Enter ingredients you would like to cook with (separate ingredients with a comma)",
                            "onion, chorizo, chicken thighs, paella rice, frozen peas, prawns")

if st.button("Give me recommendations!"):
    col1, col2, col3 = st.beta_columns([1, 6, 1])
    with col2:
        gif_runner = st.image("Data/gitrunner.gif")
    
    recipe = RecSys(ingredients)
    gif_runner.empty()

    # Add the hyperlink to the recipe URLs
    recipe["url"] = recipe.apply(lambda row: make_clickable(row["recipe"], row["url"]), axis=1)

    recipe_display = recipe[["recipe", "ingredients", "url"]]
    recipe_display = recipe_display.to_html(escape=False)

    st.write(recipe_display, unsafe_allow_html=True)
