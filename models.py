from app import db

class Location(db.Model):
  __tablename__ = "locations"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64))
  category = db.Column(db.String(64))
  visits = db.relationship('Visit', backref='location')

  def __repr__(self):
    return f"<Location: {self.id}: {self.name}>"

# #######################################################

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    visits = db.relationship('Visit', backref='user')

    def __repr__(self):
        return f"<User: {self.id}: {self.name}>"

# #######################################################

class Visit(db.Model):
    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    review = db.Column(db.Text())

    def __repr__(self):
        return f"<Visit: {self.id}: {self.review}>"