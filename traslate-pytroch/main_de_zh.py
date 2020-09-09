import torch
import fairseq
import googletrans

from bleu import bleu

sampling= 1


# List available models
torch.hub.list('pytorch/fairseq')  # [..., 'transformer.wmt16.en-de', ... ]



# Load a transformer trained on WMT'16 En-De
# Note: WMT'19 models use fastBPE instead of subword_nmt, see instructions below
de2en = torch.hub.load('pytorch/fairseq', 'transformer.wmt19.de-en',
                       checkpoint_file='model1.pt:model2.pt:model3.pt:model4.pt',
                       tokenizer='moses', bpe='fastbpe',sampling=sampling)
de2en.eval()  # disable dropout


#seqs = ['The remarks, reported first in The Atlantic magazine and corroborated by several outlets, including CNN, seemed so in character with Trump\'s public persona that even an onslaught of denials from current and former officials did little to negate the impression that Trump is a man who sometimes says terrible things.']
text = "多一個空間是龍山寺周邊的複合式咖啡廳，不限時間結合桌遊跟電影，隱藏在台味十足的萬華區巷弄間，充滿粉嫩色調的裝潢顯得相當吸睛，販售輕食與糕點還有上百款桌遊，亦有獨立包廂可租借。咖啡廳有慵懶風的吊椅及網美球池非常適合拍照，多一個空間是濃厚少女心的龍山寺咖啡廳，喜歡拍照的人不要錯過。"
seq = str(googletrans.Translator().translate(text, dest="de", src="zh-tw").text)

print("0", seq)
print("0", text)

s1 = de2en.translate(seq)
print("1", s1)
print("1", googletrans.Translator().translate(s1, src="en", dest="zh-tw").text)

s2 = de2en.translate(seq)
print("2", s2)
print("2", googletrans.Translator().translate(s2, src="en", dest="zh-tw").text)


