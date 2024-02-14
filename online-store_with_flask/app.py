from flask import Flask, render_template, request
from product.views import product_blueprint

app = Flask(__name__)
app.register_blueprint(product_blueprint)


@app.route('/')
@app.route('/hello')
def hello_world():
    user = request.args.get('user', 'Shamil')
    return render_template('index.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)
