from flask import Flask
from config import Config

app = Flask(__name__)

# 환경변수 셋팅
app.config.from_object(Config)


if __name__ == "__main__" :
    app.run()