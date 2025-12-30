from flask import Flask, jsonify

def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/healthz")
    def healthz():
        return jsonify(status="ok")

    @app.get("/")
    def root():
        return jsonify(message="golden pipeline template")

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=8080)
