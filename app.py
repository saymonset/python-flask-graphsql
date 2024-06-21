# from flask import Flask
# from dotenv import load_dotenv
# from flask_cors import CORS
# import os
# from config.mongodb import mongo
# from routes import blueprint
# from flask_jwt_extended import JWTManager
 


# load_dotenv()
# app = Flask(__name__)
# app.config['MONGO_URI'] = os.getenv('MONGO_URI')
# app.config['RESTPLUS_MASK_SWAGGER'] = False
# app.config["JWT_SECRET_KEY"] = os.getenv('JWT_SECRET')
# CORS(app, resources={r"*": {"origins": "*"}})  # Ajusta según tus rutas y necesidades
 
# jwt = JWTManager(app)
# mongo.init_app(app)
# app.register_blueprint(blueprint)

 