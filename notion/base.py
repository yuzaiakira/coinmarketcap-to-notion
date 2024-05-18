import notion_client


class BaseClient:    
    def __init__(self, token: str, database_id: str) -> None:
        self.__token = token
        self.client = notion_client.Client(auth=self.__token)
        self.database_id = database_id
        