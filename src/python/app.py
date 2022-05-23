from flask import Flask
from flask_cors import CORS

from routes import *


app = Flask(__name__)
CORS(app)
app.register_blueprint(routes)


# ----------------------------------------------------------------
### MAIN PROGRAM
# ----------------------------------------------------------------

if __name__ == '__main__':
    app.run('0.0.0.0', port = "8081")