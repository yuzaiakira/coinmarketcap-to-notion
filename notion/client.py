from .base import BaseClient
from .database import Database
from .page import Page


class Client(BaseClient, Database, Page):
    properties = {
        'symbol': 'title',
        'website': 'rich_text',
        'technical_doc': 'rich_text',
        'twitter': 'rich_text',
        'reddit': 'rich_text',
        'message_board': 'rich_text',
        'announcement': 'rich_text',
        'chat': 'rich_text',
        'explorer': 'rich_text',
        'source_code': 'rich_text',
        'name': 'rich_text',
        'description': 'rich_text',
        'tags': 'multi_select',
        'platform': 'rich_text',
        'category': 'rich_text',
    }

    def get_symbols(self) -> list[str] | None:
        """get all used symbols in Notion database

        Returns:
            list[str] : list of coin symbols
            None: if cant fine any symbols from database
        """
        data = self.fetch_data()
        symbols = list()
        if data:
            for row in data['results']:
                symbol = row['properties']['symbol']['title']
                if symbol:
                    symbols.append(symbol[0]['text']['content'])

            return symbols

        return None

    def clean_pages_data(self, data: dict):

        clean_data = dict()
        for symbol in data:
            coin = data[symbol]
            if isinstance(coin, list):
                coin = coin[0]

            clean_data[symbol] = {
                'website': {
                    'rich_text': [{
                        "text": {
                            "content": '\n'.join(coin['urls']['website'])
                        }
                    }]
                },
                'technical_doc': {
                    'rich_text': [{
                        "text": {
                            "content": '\n'.join(coin['urls']['technical_doc'])
                        }
                    }]
                },
                'twitter': {
                    'rich_text': [{
                        "text": {
                            "content": '\n'.join(coin['urls']['twitter'])
                        }
                    }]
                },
                'reddit': {
                    'rich_text': [{
                        "text": {
                            "content": '\n'.join(coin['urls']['reddit'])
                        }
                    }]
                },
                'message_board': {
                    'rich_text': [{
                        "text": {
                            "content": '\n'.join(coin['urls']['message_board'])
                        }
                    }]
                },
                'announcement': {
                    'rich_text': [{
                        "text": {
                            "content": '\n'.join(coin['urls']['announcement'])
                        }
                    }]
                },
                'chat': {
                    'rich_text': [{
                        "text": {
                            "content": '\n'.join(coin['urls']['chat'])
                        }
                    }]
                },
                'explorer': {
                    'rich_text': [{
                        "text": {
                            "content": '\n'.join(coin['urls']['explorer'])
                        }
                    }]
                },
                'source_code': {
                    'rich_text': [{
                        "text": {
                            "content": '\n'.join(coin['urls']['source_code'])
                        }
                    }]
                },
                'name': {
                    'rich_text': [{
                        "text": {
                            "content": coin['name']
                        }
                    }]
                },
                'description': {
                    'rich_text': [{
                        "text": {
                            "content": coin['description']
                        }
                    }]
                },
                'tags': {
                    'multi_select': [{
                        "name": i
                    } for i in coin['tags']]
                },
                'platform': {
                    'rich_text': [{
                        "text": {
                            "content": str(coin['platform'])
                        }
                    }]
                },
                'category': {
                    'rich_text': [{
                        "text": {
                            "content": coin['category']
                        }
                    }]
                },
            }

        return clean_data
