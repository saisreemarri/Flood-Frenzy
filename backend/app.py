
from flask import Flask, jsonify, request
from flask_cors import CORS

from game import Game

app = Flask(__name__)
CORS(app)

# Global game instance
game = Game()


@app.route("/")
def home():
    return "Flood Frenzy Backend Running!"


# ----------------------------
# Start New Game
# ----------------------------
@app.route("/new-game", methods=["GET"])
def new_game():
    global game

    game = Game()

    return jsonify({
        "board": game.board,
        "moves": game.moves,
        "won": False,
        "owned": list(game.owned)
    })


# ----------------------------
# Make Move
# ----------------------------
@app.route("/make-move", methods=["POST"])
def make_move():
    global game

    data = request.get_json()

    if not data or "color" not in data:
        return jsonify({
            "error": "Color not provided."
        }), 400

    color = data["color"]

    if color not in [0, 1, 2, 3, 4]:
        return jsonify({
            "error": "Invalid color."
        }), 400

    result = game.make_move(color)

    return jsonify(result)


# ----------------------------
# Undo
# ----------------------------
@app.route("/undo", methods=["POST"])
def undo():

    result = game.undo()

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)