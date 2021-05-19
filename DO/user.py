from src.decorators import needsDatabase


class UserDO:
    """Handles database fetching and update for User objects"""

    def __init__(self, id=None, username=None):
        self.id = id
        self.username = username
        self.score = 0
        self.games = []

    @needsDatabase
    def save(self, db):
        """Saves the user to the database"""
        if self.id is None:
            raise Exception("Le champ id ne peut pas être vide")

        self.id = db.update(script="add_user", params=(self.id, self.username, self.score))

    @needsDatabase
    def load(self, db):
        """loads a user from the database"""
        if self.id is None:
            raise Exception("Impossible de charger un utilisateur sans son id !")

        data = db.fetch(script="get_user", params=(self.id,))[0]

        self.id, self.username, self.score = data

        games = db.fetch(script="get_user_games", params=(self.id,))
        self.games = [game[0] for game in games]

    def delete(self, db):
        pass