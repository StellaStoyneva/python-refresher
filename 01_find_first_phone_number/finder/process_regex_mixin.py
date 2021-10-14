import re

class ProcessRegexMixIn:
    def find_first_match(input_data, pattern):
        matches = re.search(pattern, input_data)
        if(matches):
            return matches.group()
            