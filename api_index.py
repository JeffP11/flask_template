from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Ok"

import api_service
app.register_blueprint(api_service.bp)
 
if __name__ == '__main__':
    app.run()