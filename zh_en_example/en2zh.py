import googletrans

translator = googletrans.Translator()
LANGCODES = [code for code in googletrans.LANGCODES.values()]
LANGCODE2Contry = {v:k for k,v in googletrans.LANGCODES.items()}
text='The military news agency reported that Air Force aircraft have turned over duties in preparation for war.At the same time, transportation aircraft are also carrying the necessary logistic support manpower and equipment to designated locations.'




results = translator.translate(text, src="en", dest="zh-tw")

print(results.text)
