from flask import Flask, render_template_string
import requests
from bs4 import BeautifulSoup

app = Flask(_name_)

@app.route('/')
def scrape_and_display():
    url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    products = []
    for item in soup.select('.thumbnail'):
        name = item.select_one('.title').get_text(strip=True)
        price = item.select_one('.price').get_text(strip=True)
        rating = len(item.select('.ratings span[class="glyphicon glyphicon-star"]'))
        products.append({'name': name, 'price': price, 'rating': f"{rating}/5"})

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Scraped Products</title>
        <style>
            body {
                font-family: 'Trebuchet MS', sans-serif;
                background: linear-gradient(to right, #fdfcfb, #e2d1c3);
                padding: 20px;
                color: #333;
            }
            h1 {
                text-align: center;
                color: #34495e;
            }
            table {
                width: 90%;
                margin: 0 auto;
                border-collapse: collapse;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                background-color: #ffffff;
                border-radius: 10px;
                overflow: hidden;
            }
            th, td {
                padding: 15px;
                text-align: center;
                border-bottom: 1px solid #ccc;
            }
            th {
                background-color: #2c3e50;
                color: #ecf0f1;
                font-size: 18px;
            }
            tr:hover {
                background-color: #f9f9f9;
            }
            td {
                font-size: 16px;
            }
        </style>
    </head>
    <body>
        <h1>Scraped Product Information</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>Price</th>
                <th>Rating</th>
            </tr>
            {% for product in products %}
            <tr>
                <td>{{ product.name }}</td>
                <td>{{ product.price }}</td>
                <td>{{ product.rating }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """
    return render_template_string(html, products=products)

if _name_ == '_main_':
    app.run(debug=True)
        
          
          
