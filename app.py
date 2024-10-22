from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load the cleaned data
data = pd.read_csv('cleaned_customer_squad_data.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']
    search_results = data[(data['Market'].str.contains(search_term, case=False)) |
                          (data['ASEAN Market'].str.contains(search_term, case=False))]
    return render_template('index.html', tables=[search_results.to_html(classes='data')], search_term=search_term)

# Necessary for vercel deployment
if __name__ == "__main__":
    app.run(debug=True)
