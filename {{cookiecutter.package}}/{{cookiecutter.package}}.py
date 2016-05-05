from flask import Blueprint, Flask, render_template


public = Blueprint('public', __name__)


@public.route('/')
def index():
    return render_template('index.html')


def create_app(config_object=__name__):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(public)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run()
