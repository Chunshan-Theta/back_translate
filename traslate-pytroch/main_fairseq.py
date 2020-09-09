import torch
import fairseq
import googletrans

from bleu import bleu

sampling= 1


# List available models
torch.hub.list('pytorch/fairseq')  # [..., 'transformer.wmt16.en-de', ... ]

# Load a transformer trained on WMT'16 En-De
# Note: WMT'19 models use fastBPE instead of subword_nmt, see instructions below
en2de = torch.hub.load('pytorch/fairseq', 'transformer.wmt19.en-de',
                       checkpoint_file='model1.pt:model2.pt:model3.pt:model4.pt',
                       tokenizer='moses', bpe='fastbpe',sampling=sampling)
en2de.eval()  # disable dropout

# Load a transformer trained on WMT'16 En-De
# Note: WMT'19 models use fastBPE instead of subword_nmt, see instructions below
de2en = torch.hub.load('pytorch/fairseq', 'transformer.wmt19.de-en',
                       checkpoint_file='model1.pt:model2.pt:model3.pt:model4.pt',
                       tokenizer='moses', bpe='fastbpe',sampling=sampling)
de2en.eval()  # disable dropout

# The underlying model is available under the *models* attribute
assert isinstance(en2de.models[0], fairseq.models.transformer.TransformerModel)

# Move model to GPU for faster translation
#en2de.cuda()

# Translate a sentence
#en2de.translate('Hello world!')
# 'Hallo Welt!'

# Batched translation
#en2de.translate(['Hello world!', 'The cat sat on the mat.'])
# ['Hallo Welt!', 'Die Katze saß auf der Matte.']

#seqs = ['The remarks, reported first in The Atlantic magazine and corroborated by several outlets, including CNN, seemed so in character with Trump\'s public persona that even an onslaught of denials from current and former officials did little to negate the impression that Trump is a man who sometimes says terrible things.']
text = "蔡壁元指出加利事件爆發後，海關有針對進口口罩逐批查驗，從8月10日至9月3日，關務署查獲577件共83萬0832片偽標MIT的非醫用口罩，全數扣押在海關，並未流入市面，後續調查結果會在2周內向外界報告。"
seq = str(googletrans.Translator().translate(text, dest="en", src="zh-tw").text)

print("0", seq)
print("0", text)
seq = en2de.translate(seq)

s1 = de2en.translate(seq)
print("1",s1)
print("1",googletrans.Translator().translate(s1, src="en", dest="zh-tw").text)

s2 = de2en.translate(seq)
print("2",s2)
print("2",googletrans.Translator().translate(s2, src="en", dest="zh-tw").text)


