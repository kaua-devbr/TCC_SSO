from flask import Flask

app = Flask(
    __name__,
    static_folder="templates/static",
    static_url_path="/static"
)
