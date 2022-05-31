from flask import Flask
<<<<<<< HEAD
app = Flask(__name__)
from app import routes
=======

app = Flask(__name__)

from app import routes

>>>>>>> aac459b611dfbcaa35759cf0268ebce050a75da7
app.run(debug=True)