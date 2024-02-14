from flask import Flask, render_template, request
from product.views import product_blueprint
import ccy

app = Flask(__name__)
app.register_blueprint(product_blueprint)


@app.route('/')
@app.route('/hello')
def hello_world():
    user = request.args.get('user', 'Shamil')
    return render_template('index.html', user=user)


@app.template_filter('format_currency')
def format_currency_filter(amount):
    currency_code = ccy.countryccy(request.accept_languages.best[-2:])
    return '{0} {1}'.format(currency_code, amount)



if __name__ == '__main__':
    app.run(debug=True)
