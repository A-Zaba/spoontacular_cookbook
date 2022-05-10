from SearchRecipes_Flask import app, forms
from flask import request, render_template


@app.route('/')
@app.route('/search', methods=["GET", "POST"])
def search():
    search_form = forms.SearchForRecipes(request.form)

    if request.method == 'POST':
        # Assign user input to variables
        meal = request.form['meal']
        include = request.form['include']
        exclude = request.form['exclude']

        # Pass the variables above as arguments to the get_data function and assign the return value to recipes
        recipes = forms.get_data(meal, include, exclude)

        # accessing the list available in the json:
        recipe_list = recipes["videos"]
        return render_template('recipes_results.html', form=search_form, meal=meal, include=include,
                               exclude=exclude, recipes=recipe_list)
    return render_template('recipes_search.html', form=search_form)
