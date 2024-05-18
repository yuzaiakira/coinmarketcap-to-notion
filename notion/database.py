from typing import Any
import notion_client

from .property import DatabasePropertyMixin, PropertyMixin


class Database(DatabasePropertyMixin, PropertyMixin):

    def fetch_data(self) -> notion_client.typing.SyncAsync[Any]:
        """Return all notion data 

        Returns:
            notion_client.typing.SyncAsync[Any]: a dictionary from database data and information
        """
        return self.client.databases.query(database_id=self.database_id) 
    
    def database(self) -> None:
        return self.client.databases.retrieve(database_id=self.database_id)
    
    def migrate_database(self):
        notion_data = self.fetch_data() 
        self.reset_database_properties(notion_data)

        new_properties = self.get_properties()
        self.add_database_properties(new_properties)
        

    
    
    