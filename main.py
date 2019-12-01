from flask import Flask, request, render_template, send_from_directory
from flask_restful import Resource, Api
import gunicorn
import urllib.request

app = Flask(__name__)
app.static_folder = 'static'
api = Api(app)

@app.route('/')
def HelloWorld():
    print ('heello')
    return send_from_directory("angular/src", "index.html") 


class MyApi(Resource):
    def post(self):

        some_json = request.args
        print(some_json)

# api.add_resource(HelloWorld, '/')
api.add_resource(MyApi, '/extract_datad')

if __name__ == "__main__":
    app.run(debug = True)