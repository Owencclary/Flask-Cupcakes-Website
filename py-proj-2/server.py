from flask import Flask, render_template, url_for, redirect
from cupcakes import get_cupcakes, find_cupcake, add_cupcake

app = Flask(__name__)

# renders home page
@app.route("/")
def home():
    return render_template("cupcakes.html", cupcakes = get_cupcakes("cupcakes.csv"))

# renders the page for all the avaiable cupcakes
@app.route("/cupcakes")
def cupcakes():
    return render_template("cupcakes.html", cupcakes = get_cupcakes("cupcakes.csv"))

@app.route("/individual-cupcake/<name>")
def individual_cupcake(name):
    return render_template("individual-cupcakes.html", cupcake = find_cupcake("cupcakes.csv", name))

# renders the page for all the orders
@app.route("/order")
def order():
    return render_template("order.html", cupcakes = get_cupcakes("orders.csv"))

# appends a cupcake to the order CSV
@app.route("/add-cupcake/<name>")
def order_cupcake(name):
    cupcake = find_cupcake("cupcakes.csv", name)
    if cupcake:
        add_cupcake("orders.csv", cupcake)
        return redirect(url_for("home"))
    else:
        return "Sorry cupcake not found."

if __name__ == "__main__":
    app.env = "development"
    app.run(debug = True, port = 8000, host = "localhost")