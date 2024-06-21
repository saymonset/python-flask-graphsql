import os
from dotenv import load_dotenv
from flask_cors import CORS
from config.mongodb import mongo
from flask import Flask
from strawberry.flask.views import  GraphQLView
from flaskr.strawberrygraphql import schema  
from flask_jwt_extended import JWTManager
from routes import blueprint


# Cargar las variables de entorno desde el archivo .env

load_dotenv()

def create_app(test_config=None):

    

    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app, resources={r"/api/*": {"origins": "*"}})  # Ajusta según tus rutas y necesidades
    app.config['MONGO_URI'] = os.getenv('MONGO_URI')
    app.config['RESTPLUS_MASK_SWAGGER'] = False
    app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET')
    jwt = JWTManager(app)
    mongo.init_app(app)
    app.register_blueprint(blueprint)  

    
    

    

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)
        
  

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # from . import db
    # db.init_app(app)
    
    # from . import auth
    # app.register_blueprint(auth.bp)
    
    # Agrega la vista de GraphQL a tu aplicación Flask
    app.add_url_rule("/graphql" , view_func=GraphQLView.as_view( "graphql" , schema=schema))
    CORS(app, resources={r"/*": {"origins": "*"}})  # Ajusta según tus rutas y necesidades
    return app