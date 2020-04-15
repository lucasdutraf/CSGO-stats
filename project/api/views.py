from flask import request, jsonify, Blueprint
from project.api.models import User, KDA, ADR
from project.api.utils import Utils
from sqlalchemy import exc
from database_singleton import Singleton


cs_blueprint = Blueprint('cs', __name__)
db = Singleton().database_connection()
utils = Utils()

@cs_blueprint.route('/add_player', methods=['POST'])
def add_player():
    post_data = request.get_json()
    if not post_data:
        return jsonify(utils.createFailMessage('Wrong JSON')), 400
    
    player = post_data.get('player')

    name = player.get('name')
    points = player.get('points')
    rank = player.get('rank')
    nick = player.get('nick')
    primary_role = player.get('primary_role')
    secondary_role = player.get('secondary_role')
    average_adr = player.get('average_adr')
    average_kda = player.get('average_kda')

    try:
        player = User(name, points, average_kda, average_adr, rank, nick, primary_role, secondary_role)

        db.session.add(player)
        db.session.flush()
        db.session.commit()

        return jsonify(utils.createSuccessMessage('Player created!')), 201

    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(utils.createFailMessage('DB error')), 400

@cs_blueprint.route('/add_kda', methods=['POST'])
def add_kda():
    post_data = request.get_json()
    if not post_data:
        return jsonify(utils.createFailMessage('Wrong JSON')), 400
    
    player = post_data.get('player')

    user_id = player.get('user_id')
    kda = player.get('kda')

    try:
        user_kda = KDA(user_id, kda)

        db.session.add(user_kda)
        db.session.flush()
        db.session.commit()

        return jsonify(utils.createSuccessMessage('KDA added!')), 201

    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(utils.createFailMessage('DB error')), 400

@cs_blueprint.route('/add_adr', methods=['POST'])
def add_adr():
    post_data = request.get_json()
    if not post_data:
        return jsonify(utils.createFailMessage('Wrong JSON')), 400
    
    player = post_data.get('player')

    user_id = player.get('user_id')
    adr = player.get('adr')

    try:
        user_adr = ADR(user_id, adr)

        db.session.add(user_adr)
        db.session.flush()
        db.session.commit()

        return jsonify(utils.createSuccessMessage('ADR added!')), 201

    except exc.IntegrityError:
        db.session.rollback()
        return jsonify(utils.createFailMessage('DB error')), 400
        
# @cs_blueprint.route('/rank', methods=['GET'])
# def get_rank():

# @cs_blueprint.route('/sort_teams', methods=['POST'])
# def sort_teams():
#     #TODO get user by json format, get user tuple, put all on list of dicts and order


# @cs_blueprint.route('/status/<name>', methods=['GET'])
# def get_status(name):