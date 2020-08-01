import googletrans

translator = googletrans.Translator()

with open("./back_translate_zh/example_file_zh.txt") as f:
  text=str(f.read())



results = translator.translate(text, dest="en", src="zh-tw")
with open("./back_translate_zh/example_file.txt","w") as f:
  f.write(str(results.text))

#print(results.text)
