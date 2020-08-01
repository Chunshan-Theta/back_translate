import googletrans

translator = googletrans.Translator()

with open("./back_trans_data/backward_gen/file_0_of_1.txt") as f:
  text=str(f.read())



results = translator.translate(text, src="en", dest="zh-tw")
with open("./back_translate_zh/example_file_zh3.txt","w") as f:
  f.write(str(results.text))

#print(results.text)
