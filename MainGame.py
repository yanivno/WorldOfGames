from Live import load_game, welcome
from flask import Flask
from MainScores import MainScores
from utils import FLASK_IP_BIND, FLASK_PORT_BIND, FLASK_TEMPLATE_FOLDER

# app variables
app = Flask('app', template_folder=FLASK_TEMPLATE_FOLDER)

# routes
app.add_url_rule(rule="/", view_func=MainScores.score_server, methods=["GET"])

# start server
if __name__ == '__main__':
    app.run(host=FLASK_IP_BIND, port=FLASK_PORT_BIND, debug=True)

name = input("please enter your name:")
print(welcome(name))
load_game()
