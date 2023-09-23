import re

def sentenceCase(string):
    return re.sub('([A-Z])', r' \1', string).title()

def camelCase(s):
    return ''.join([s[0].lower(), s.replace(' ', '')[1:]])
