from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Ok"

import servicio
app.register_blueprint(servicio.bp)
 
if __name__ == '__main__':
    app.run()