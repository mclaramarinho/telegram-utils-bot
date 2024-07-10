import string
import re
import shorten_url

import shorten


class InvalidUrlException(Exception):
    message = "This URL is not valid."



def validate_url(url: string):
    regex = re.compile(r'(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?\/[a-zA-Z0-9]{2,}|((https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z]{2,}(\.[a-zA-Z]{2,})(\.[a-zA-Z]{2,})?)|(https:\/\/www\.|http:\/\/www\.|https:\/\/|http:\/\/)?[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,}(\.[a-zA-Z0-9]{2,})?', re.IGNORECASE)

    match = regex.match(url)

    if match:
        return True
    else:
        return False


def shortener(url: string):
    if validate_url(url):
        shortened = shorten.shorten(url)
        return shortened
    else:
        raise InvalidUrlException()


