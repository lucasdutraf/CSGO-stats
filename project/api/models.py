from database_singleton import Singleton

db = Singleton().database_connection()


class User(db.Model):
    __tablename__ = 'user'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    rank = db.Column(db.String(11), nullable=False)
    nick = db.Column(db.String(30), nullable=False)
    role = db.Column(db.Enum('AWP', 'Rifler', 'Lurker', 'Entry Fragger', 'Support'), nullable=True)
    secondary_role = db.Column(db.Enum('AWP', 'Rifler', 'Lurker', 'Entry Fragger', 'Support'), nullable=True)
    
    def __init__(self, name, rank, nick, role, secondary_role):
        self.name = name
        self.rank = rank
        self.nick = nick
        self.role = role
        self.secondary_role = secondary_role

    def to_json(self):
        return {
            'user_id': self.user_id,
            'name': self.name,
            'rank': self.rank,
            'nick': self.nick,
            'role': self.role,
            'secondary_role': self.secondary_role,
        }