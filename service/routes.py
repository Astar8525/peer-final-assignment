@app.route("/products", methods=["GET"])
def list_products():
    ...

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    ...

@app.route("/products", methods=["POST"])
def create_product():
    ...

@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    ...

@app.route("/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    ...

@app.route("/products/name/<string:name>", methods=["GET"])
def search_by_name(name):
    ...

# Repeat for category and availability
