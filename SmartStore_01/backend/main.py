from flask import Flask
from backend.api import bp as api_bp
import os

app = Flask(
    __name__,
    static_folder="../../frontend_module/web_ui/static",
    template_folder="../../frontend_module/web_ui/templates"
)

# 注册蓝图
app.register_blueprint(api_bp, url_prefix='/api')

@app.route('/')
def index():
    return "Smart Store Backend is running!"

if __name__ == '__main__':
    app.run(debug=True)
