from flask import Flask
from flask_login import LoginManager
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from sqlalchemy import create_engine


# Setup of key Flask object (app)
app = Flask(__name__)

# Initialize Flask-Login object
login_manager = LoginManager()
login_manager.init_app(app)

# Allowed servers for cross-origin resource sharing (CORS), these are GitHub Pages and localhost for GitHub Pages testing
cors = CORS(app, supports_credentials=True, origins=['http://localhost:4100', 'http://127.0.0.1:4100', 'https://nighthawkcoders.github.io'])

# Secret key for session handling and CSRF protection
SECRET_KEY = os.environ.get('SECRET_KEY') or 'SECRET_KEY'
SESSION_COOKIE_NAME = os.environ.get('SESSION_COOKIE_NAME') or 'sess_python_flask'
JWT_TOKEN_NAME = os.environ.get('JWT_TOKEN_NAME') or 'jwt_python_flask'
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SESSION_COOKIE_NAME'] = SESSION_COOKIE_NAME 
app.config['JWT_TOKEN_NAME'] = JWT_TOKEN_NAME 

# Setup SQLAlchemy object and properties for the database (db)
# Local SQLite database within the instance folder
# dbURI = 'sqlite:///volumes/sqlite.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
# db = SQLAlchemy()
# db.init_app(app)  # Ensure this line is present
# Migrate(app, db)

DB_USERNAME = 'kasm_admin'
DB_PASSWORD = 'pZTXfhhcvuqkF2vEy27x'
DB_HOST = 'kasm-student-db-instance.ctenoof0kzic.us-east-2.rds.amazonaws.com'
DB_PORT = '3306'  # Default port for MySQL
DB_NAME = 'user_management_db'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
db = SQLAlchemy(app)

# engine = create_engine(dbURI)


# Migrate(app, db)

# Images storage settings and location
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # maximum size of uploaded content
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']  # supported file types
app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, 'uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
