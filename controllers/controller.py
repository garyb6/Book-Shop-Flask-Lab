from app import app
from flask import render_template
from models.order import orders

@app.route('/orders')
def order_list():
    return render_template('index.html', title="Home", orders=orders)

@app.route('/orders/<index>')
def order_details(index):
    # chosen_order= orders[int(index)]
    return render_template ('bookorders.html', title="Order Details", order=int(index), orders=orders)
