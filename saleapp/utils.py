import json,os
from saleapp import app


def read_json(path):
    with open(path, "r", encoding='UTF-8') as file:
        data = json.load(file)

        return data


def load_categories():
    # return read_json('data/categories.json') #tương đối
    return read_json(os.path.join(app.root_path,'data/categories.json'))  #tuyệt đối

def load_products(cate_id = None, kw = None, from_price = None, to_price = None):
    products = read_json(os.path.join(app.root_path,'data/products.json'))  #tuyệt đối

    if cate_id:
        products = [p for p in products if p['category_id'] == int(cate_id)]

    if kw:
        products = [p for p in products if p['name'].lower().find(kw.lower()) >= 0]


    if from_price:
        products = [p for p in products if p['price'] >= float(from_price)]

    if to_price:
        products = [p for p in products if p['price'] <= float(to_price)]

    return products

def save_products(products):
    os.makedirs(os.path.dirname(os.path.join(app.root_path, 'data', 'products.json')), exist_ok=True)
    with open(os.path.join(app.root_path, 'data/products.json'), 'w', encoding='utf-8') as f:
        json.dump(products, f, indent=4, ensure_ascii=False)

def add_products(id,name,description,price,image,category_id):
    products = load_products()
    if not image:
        image = "image/default.png"
    new_products = {
        "id":str(id),
        "name": name,
        "description": description,
        "price": float(price),
        "image": image,
        "category_id": int(category_id),
    }
    products.append(new_products)
    save_products(products)



def get_products_id(product_id):
    products = read_json(os.path.join(app.root_path,'data/products.json'))  #tuyệt đối

    for p in products:
        if p['id'] == product_id:
            return p

def get_new_product_id():
    products = load_products()
    if not products:
        return 1
    else:
        return max(int(p['id']) for p in products) + 1


# thêm phần thêm phân loại sản phẩm