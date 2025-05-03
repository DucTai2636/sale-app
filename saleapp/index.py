
from flask import render_template, request, redirect
from saleapp import app
import utils, uuid,os
from saleapp.utils import get_new_product_id


@app.route("/")
def home():
    cates = utils.load_categories()
    return render_template('index.html',
                            categories=cates,)

@app.route("/products")
def product_list():
    cate_id = request.args.get("category_id")

    kw = request.args.get("keyword")
    from_price = request.args.get("from_price")
    to_price = request.args.get("to_price")
    products = utils.load_products(cate_id=cate_id,
                                    kw = kw,
                                    from_price= from_price,
                                    to_price = to_price)


    return render_template('products.html',
                            products=products)

@app.route('/addnews',methods=['POST', 'GET'])
def add_products():
    if request.method == 'POST':
        new_id = utils.get_new_product_id()
        name = request.form['name']
        description = request.form['discription']
        price = request.form['price']
        category_id = int(request.form['category_id'])

        image_file = request.files['image']

        if image_file and image_file.filename != '':
            filename = f"{new_id}.jpg"
            image_path = os.path.join('static/images', filename)
            image_file.save(image_path)

            image = f"images/{filename}"
        else:
            image = None

        utils.add_products(str(new_id),name,description,price,image,category_id)
        return redirect('/')
    new_id = utils.get_new_product_id()
    cates = utils.load_categories()
    return render_template('add_news.html',
                            categories = cates,
                            product_id = new_id)    ###check again

@app.route("/products/<int:product_id>")
def products_detail(product_id):
    products = utils.load_products()  # Load full list
    product = None

    for p in products:
        if int(p['id']) == product_id:
            product = p
            break

    if product is None:
        return "Không có sản phẩm", 404

    return render_template('details.html',
                           product=product)


if __name__ == "__main__":
    app.run(debug=True)