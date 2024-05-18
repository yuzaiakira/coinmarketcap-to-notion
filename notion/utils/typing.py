from dateutil.parser import parse
from urllib.parse import urlparse

PageId = str()
PageSymbol = str()

def is_date(value, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.

    :param value: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    
    :src: https://stackoverflow.com/questions/25341945/check-if-string-has-date-any-format
    """
    try: 
        
        return True, parse(value, fuzzy=fuzzy)

    except ValueError:
        return False
    
    
def is_url(value:str) -> bool:
    try:
        result = urlparse(value)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False