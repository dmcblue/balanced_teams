class Member:
    def __init__(self, name: str, is_online: bool, ranking: int) -> None:
        self.name = name
        self.ranking = ranking
        self.raw_status = "online" if is_online else "offline"

class ParsedMessage:
    def __init__(self, command: str, **attributes):
        self.command = command
        for attribute_name in attributes.keys():
            # self[attribute_name] = attributes[attribute_name]
            self.__dict__[attribute_name] = attributes[attribute_name]
