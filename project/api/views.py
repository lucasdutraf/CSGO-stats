from flask import request, jsonify, Blueprint
from project.api.models import User, KDA, ADR
from sqlalchemy import exc
from database_singleton import Singleton


cs_blueprint = Blueprint('cs', __name__)
db = Singleton().database_connection()


@cs_blueprint.route('/add_player', methods=['POST'])
def add_player():

@cs_blueprint.route('/add_kda', methods=['POST'])
def add_kda():

@cs_blueprint.route('/add_adr', methods=['POST'])
def add_adr():

@cs_blueprint.route('/rank', methods=['GET'])
def get_rank():

@cs_blueprint.route('/sort_teams', methods=['POST'])
def sort_teams():
    #TODO get user by json format, get user tuple, put all on list of dicts and order


@cs_blueprint.route('/status/<name>', methods=['GET'])
def get_status(name):