from flask import Flask, request
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from

app = Flask(__name__)
app.json_encoder = LazyJSONEncoder

swagger_template = dict(
info = {
    'title': LazyString(lambda: 'My first Swagger UI document'),
    'version': LazyString(lambda: '0.1'),
    'description': LazyString(lambda: 'This document depicts a      sample Swagger UI document and implements Hello World functionality after executing GET.'),
    },
    host = LazyString(lambda: request.host)
)
swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'anoboy_online',
            "route": '/anoboy_online.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        },
        {
            "endpoint": 'kaasi',
            "route": '/kaasi.json',
            "rule_filter": lambda rule: True,
            "model_filter": lambda tag: True,
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}
swagger = Swagger(app, template=swagger_template,             
                  config=swagger_config)

@swag_from("get_data.yml", methods=['GET'])
@app.route("/get-anime")
def get_anime():
    return "some anime"

@swag_from("get_data.yml", methods=['GET'])
@app.route("/get-episode")
def get_episode():
    return "episode link"

@swag_from("get_data.yml", methods=['GET'])
@app.route("/get-video")
def get_video():
    return "video link"

if __name__ == '__main__':
    app.run()