from langdetect import detect


def LangCheck(langName):
    blockedLang = {
        'en',
        'de',
    }
    for lang in blockedLang:
        if lang == langName:
            return 'BLOCKED'
    return langName

textInput = input('Enter text to recognize it: ')

print (f'Language of ({textInput}) are {LangCheck(detect(textInput))}')
