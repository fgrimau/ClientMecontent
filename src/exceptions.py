class CommandNotFoundException(Exception):
    def __init__(self, command: str):
        self.command = command

    def __str__(self):
        return f"La commande '{self.command}' n'a pas pu être trouvée, tapez !help pour avoir de l'aide"


class BadFormatException(Exception):
    def __init__(self, command: str, pattern: str):
        self.command = command
        self.pattern = pattern

    def __str__(self):
        return f"La commande '{self.command}' ne suit pas le pattern '{self.pattern}'"


class BadTypeArgumentException(Exception):
    def __init__(self, arg, requiredType):
        self.arg = arg
        self.requiredType = requiredType

    def __str__(self):
        return f"L'argument {self.arg} n'a pas le bon type (Requis : {self.requiredType}, recu {type(self.arg)})"


class InvalidFieldException(Exception):
    def __init__(self, arg, possibleFields):
        self.arg = arg
        self.possibleFields = possibleFields

    def __str__(self):
        return f"L'argument {self.arg} ne correspond pas à un champ reconnu (Champs possibles : {self.possibleFields})"


class InvalidArgumentException(Exception):
    def __init__(self, arg, argumentType):
        self.arg = arg
        self.argumentType = argumentType

    def __str__(self):
        return f"L'argument {self.arg} n'est pas correct (Attendu : {self.argumentType})"


class IllegalUserException(Exception):
    def __init__(self, user, game_id):
        self.user = user
        self.game = game_id

    def __str__(self):
        return f"L'utilisateur <@{self.user}> n'est pas dans la partie {self.game_id}"
