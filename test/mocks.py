class Member:
    def __init__(self, name: str, is_online: bool, ranking: int) -> None:
        self.name = name
        self.ranking = ranking
        self.raw_status = "online" if is_online else "offline"
