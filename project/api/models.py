from database_singleton import Singleton

db = Singleton().database_connection()


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    rank = db.Column(db.String(40), nullable=False)
    nick = db.Column(db.String(30), nullable=False)
    points = db.Column(db.Float, nullable=False)
    average_kda = db.Column(db.Float, nullable=True)
    average_adr = db.Column(db.Float, nullable=True)
    primary_role = db.Column(db.Enum('AWP', 'Rifler', 'Lurker', 'Entry Fragger', 'Support'), nullable=True)
    secondary_role = db.Column(db.Enum('AWP', 'Rifler', 'Lurker', 'Entry Fragger', 'Support'), nullable=True)
    
    def __init__(self, name, points, average_kda, average_adr, rank, nick, primary_role, secondary_role):
        self.name = name
        self.points = points
        self.rank = rank
        self.nick = nick
        self.primary_role = primary_role
        self.secondary_role = secondary_role
        self.average_adr = average_adr
        self.average_kda = average_kda

    def to_json(self):
        return {
            'user_id': self.user_id,
            'points': self.points,
            'name': self.name,
            'rank': self.rank,
            'nick': self.nick,
            'primary_role': self.primary_role,
            'secondary_role': self.secondary_role,
            'average_kda': self.average_kda,
            'average_adr': self.average_adr
        }
class KDA(db.Model):
    __tablename__ = 'statistic_kda'

    kda_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    kda = db.Column(db.Float, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, kda, user_id):
        self.kda = kda
        self.user_id = user_id

    def to_json(self):
        return {
            'kda_id': self.kda_id,
            'kda': self.kda,
            'user_id': self.user_id
        }

class ADR(db.Model):
    __tablename__ = 'statistic_adr'

    adr_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    adr = db.Column(db.Float, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, adr, user_id):
        self.adr = adr
        self.user_id = user_id

    def to_json(self):
        return {
            'adr_id': self.adr_id,
            'adr': self.adr,
            'user_id': self.user_id
        }