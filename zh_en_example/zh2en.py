import googletrans

translator = googletrans.Translator()
LANGCODES = [code for code in googletrans.LANGCODES.values()]
LANGCODE2Contry = {v:k for k,v in googletrans.LANGCODES.items()}
text='軍聞社報導，空軍相關機型實施戰力防護戰備轉場；同時，運輸機也將所需後勤維保人力、裝備載運至指定地點。'



results = translator.translate(text, dest="en", src="zh-tw")

print(results.text)
