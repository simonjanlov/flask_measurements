from .database import db

 
class RecordsModel(db.Model):
    __tablename__ = 'records'
 
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    starting_point = db.Column(db.Float)
    week_1 = db.Column(db.Float)
    week_2 = db.Column(db.Float)
    week_3 = db.Column(db.Float)
    week_4 = db.Column(db.Float)
    week_5 = db.Column(db.Float)
    week_6 = db.Column(db.Float)
    week_7 = db.Column(db.Float)
    week_8 = db.Column(db.Float)
    week_9 = db.Column(db.Float)
    week_10 = db.Column(db.Float)
 
    def __init__(self, starting_point, week_1, week_2, week_3, week_4, week_5, week_6, week_7, week_8, week_9, week_10):
        self.starting_point = starting_point
        self.week_1 = week_1
        self.week_2 = week_2
        self.week_3 = week_3
        self.week_4 = week_4
        self.week_5 = week_5
        self.week_6 = week_6
        self.week_7 = week_7
        self.week_8 = week_8
        self.week_9 = week_9
        self.week_10 = week_10
 
    def __repr__(self):
        return f"Starting point: {self.starting_point}"