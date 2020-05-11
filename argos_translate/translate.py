import os

languages = []

class Language:
    def __init__(self, code, name):
        self.code = code
        self.name = name
        self.translations_from = []
        self.translations_to = []
        languages.append(self)

    def __str__(self):
        return self.name

    def get_translation(self, to):
        valid_translations = list(filter(lambda x: x.to_lang.code == to.code, self.translations_from))
        if len(valid_translations) > 0:
            return valid_translations[0]
        return None

class Translation:
    def __init__(self, from_lang, to_lang, translate_function):
        self.from_lang = from_lang
        self.to_lang = to_lang
        self.translate_function = translate_function
        from_lang.translations_from.append(self)
        to_lang.translations_to.append(self)

    def __str__(self):
        return str(self.from_lang) + ' -> ' + str(self.to_lang)

def apertium_translation(from_code, to_code):
    def to_return(input_text):
        return os.popen('echo \'' + input_text + '\' | apertium ' + from_code + '-' + to_code + '').read()
    return to_return

# Languages
en = Language('en', 'English')
es = Language('es', 'Spanish')
eo = Language('eo', 'Esperanto')
ca = Language('ca', 'Catalan')

# Translations
en_es = Translation(en, es, apertium_translation('en', 'es'))
es_en = Translation(es, en, apertium_translation('es', 'en'))
en_eo = Translation(en, eo, apertium_translation('en', 'eo'))
eo_en = Translation(eo, en, apertium_translation('eo', 'en'))
en_ca = Translation(en, ca, apertium_translation('en', 'ca'))
ca_en = Translation(ca, en, apertium_translation('ca', 'en'))


# Everything can translate to itself
for language in languages:
    Translation(language, language, lambda x: x)

# Pivot through other languages to add translations
def composite_fun(first, second):
    return lambda x: second(first(x))

for language in languages:
    keep_adding_translations = True
    while keep_adding_translations:
        keep_adding_translations = False
        for translation in language.translations_from:
            for translation_2 in translation.to_lang.translations_from:
                if language.get_translation(translation_2.to_lang) == None:
                    # The language currently doesn't have a way to translate to this language
                    keep_adding_translations = True
                    trans_fun = composite_fun(translation.translate_function, translation_2.translate_function)
                    Translation(language, translation_2.to_lang, trans_fun) 
                
