from flask import Flask, request, jsonify
from flasgger import Swagger, LazyString, LazyJSONEncoder
from flasgger import swag_from
from function import webScrapper
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
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/apidocs/"
}
swagger = Swagger(app, template=swagger_template,             
                  config=swagger_config)

@swag_from("API/search_anime.yml", methods=['GET'])
@app.route("/search-anime/<query>")
def get_anime(query):
    return 

@swag_from("API/get_anime.yml", methods=['GET'])
@app.route("/get-episode/<anime>")
def get_episode():
    return "episode link"

@swag_from("API/get_video_uservideo.yml", methods=['GET'])
@app.route("/get-video-uservideo/<episode>")
def get_video():
    return "video link"

if __name__ == '__main__':
    app.run()