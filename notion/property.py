from typing import Any

from .utils.typing import is_date, is_url

class DatabasePropertyMixin:
    def add_database_properties(self, properties:dict) -> None:
        """add new properties to database

        Args:
            properties (dict): get dictionary form {'property_name1':'type1', 'property_name2':'type2' } 
        """
        columns = dict()
        for col in properties:
            columns[col] = {
                properties[col]:{}
            }
            
        self.client.databases.update(self.database_id, properties=columns)
        
    def reset_database_properties(self, data:dict) -> None:
        """delete all database properties (not Title)

        Args:
            data (dict): get data from self.fetch_notion_data()
        """
        properties = data['results'][0]['properties']
        columns = dict()
        for col in properties:
            if properties[col]['id'] != 'title':
                columns[col] = None
                
        self.client.databases.update(self.database_id, properties=columns)
        
        
class PropertyMixin:
    properties = dict()
    
    def get_properties(self) -> dict:
        """to returns custom properties dict like {'property_name1':'type1', 'property_name2':'type2' } 

        Returns:
            dict: python dictionary like {'property_name1':'type1', 'property_name2':'type2' } 
        """
        return self.properties
    