import googletrans
from fairseq.models.lightconv import LightConvModel
import jieba
from bleu import bleu

google_transer = googletrans.Translator()
zh2en = LightConvModel.from_pretrained(
  'wmt17.zh-en.lightconv-glu/',
  checkpoint_file='model.pt',
  data_name_or_path='wmt17.zh-en.lightconv-glu',
  bpe='subword_nmt',
  bpe_codes='wmt17.zh-en.lightconv-glu/en.code',
  sampling=1
)

s_text = "蔡壁元指出加利事件爆發後，海關有針對進口口罩逐批查驗，從8月10日至9月3日，關務署查獲577件共83萬0832片偽標台灣製造的非醫用口罩，全數扣押在海關"
text = str(google_transer.translate(s_text, src="zh-tw", dest="zh-cn").text)
text = " ".join(jieba.lcut(text))
print(text)


text = zh2en.translate(text)
print(text)


zh = google_transer.translate(text, src="en", dest="zh-tw").text
print(bleu(ans=s_text,translated_txet=zh),zh)
