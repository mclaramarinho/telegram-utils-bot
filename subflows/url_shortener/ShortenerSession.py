import string

from subflows.url_shortener import validate_url, shortener


# STEPS:
# 0 - Get URL
# 1 - Send short URL
# 2 - Ask if finished


class ShortenerSession:
    step: int
    prev: int
    url: string
    shortened_url: string

    def __init__(self, url: string):
        try:
            is_valid = validate_url(url)
            if(is_valid):
                self.url = url
                self.shortened_url = shortener(self.url)
            else:
                raise "Invalid URL"
        except Exception as ex:
            raise ex
