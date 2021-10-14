# pylint: disable=no-self-argument
import html5lib
from html5lib.html5parser import ParseError

class HTMLMixIn:
    def validate_html_content(html_content):
        html5parser = html5lib.HTMLParser(strict=True)
        try:
            html5parser.parse(html_content)
        except ParseError as e:
            raise Exception('ERROR: Invalid HTML ->', str(e))
