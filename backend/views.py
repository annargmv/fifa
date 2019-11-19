from flask import Blueprint, jsonify, request
from .players_data import Backend

main = Blueprint('app', __name__)

@main.route('/play')

def play_game():

    # Wanted to show the players json in the view

    players = Backend()
    players_json = players.read_from_file()

    return jsonify({"players": players_json})

    # return 'Done', 201