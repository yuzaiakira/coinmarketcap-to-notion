from abc import ABC, abstractmethod

class Page(ABC):
    def iter_pages_id(self):
        pages = self.fetch_data()
        for page in pages['results']:
            yield [page['id'], page['properties']['symbol']['title'][0]['plain_text']]
    
    def update_page_data(self, page_id:str, properties:dict):
        self.client.pages.update(page_id=page_id, properties=properties)
    
    def get_pages_data(self, data: dict):
        data = self.clean_pages_data(data)
        for page_id, page_symbol in self.iter_pages_id():
            self.update_page_data(page_id, data[page_symbol.upper()])
    
    @abstractmethod    
    def clean_pages_data(self, data: dict):
        pass