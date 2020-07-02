# This is a python3 translation of https://github.com/marian-nmt/moses-scripts/blob/master/scripts/tokenizer/normalize-punctuation.perl
import re

def normalize_punctuation(text, language='en', PENN=0):
    # remove extra spaces
    text = text.replace('\r','')
    text = text.replace('(',' (')
    text = text.replace(')',') ')
    text = re.sub(' +', ' ', text)
    text = re.sub(r'\) ([\.\!\:\?\;\,])',r')\1',text)
    text = text.replace('( ', '(')
    text = text.replace(' )', ')')
    text = re.sub(r'(\d) %', r'\1%', text)
    text = text.replace(' :',':')
    text = text.replace(' ;',';')
    
    # normalize unicode punctuation
    if (PENN == 0):
        text = text.replace('`','\'')
        text = text.replace("''",'"')

    text = text.replace('„','"')
    text = text.replace('“','"')
    text = text.replace('”','"')
    text = text.replace('–','-')
    text = text.replace('—',' - ')
    text = re.sub(' +', ' ', text)
    text = text.replace('´','\'')
    text = re.sub(r'([a-z])‘([a-z])',r"\1'\2",text)
    text = re.sub(r'([a-z])’([a-z])',r"\1'\2",text)
    text = text.replace('‘','"')
    text = text.replace('‚','"')
    text = text.replace('’','"')
    text = text.replace("''",'"')
    text = text.replace("´´",'"')
    text = text.replace('…','...')
    # French quotes
    text = text.replace(' « ','"')
    text = text.replace('« ','"')
    text = text.replace('«','"')
    text = text.replace(' » ','"')
    text = text.replace(' »','"')
    text = text.replace('»','"')
    # handle pseudo-spaces
    text = text.replace(' %','%')
    text = text.replace('nº ','nº ')
    text = text.replace(' :', ':')
    text = text.replace(' ºC', ' ºC')
    text = text.replace(' cm', ' cm')
    text = text.replace(' ?', '?')
    text = text.replace(' !', '!')
    text = text.replace(' ;', ';')
    text = text.replace(', ', ', ')
    text = re.sub(' +', ' ', text)

    # English "quotation," followed by comma, style
    if (language.lower() == 'en'):
        text = re.sub(r'"([,\.]+)', r'\1"', text)

    # Czech is confused
    elif (language.lower() in ['cs','cz']):
        pass
    # German/Spanish/French "quotation", followed by comma, style
    else:
        text = text.replace(',"','",')
        text = re.sub(r'(\.+)"(\s*[^<])', '"\1\2') # don't fix period at end of sentence

    if (language.lower() in ['de', 'es', 'cz', 'cs', 'fr']):
        text = re.sub(r'(\d) (\d)', r'\1,\2', text)
    else:
        text = re.sub(r'(\d) (\d)', r'\1.\2', text)
    return text
sample='a’b'
n=normalize_punctuation