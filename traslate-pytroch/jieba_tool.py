# 引入詞性標註介面
import jieba.posseg as psg
import random


static_label = ("nr","ns","nt","eng")
"""
text = "蔡壁元指出佳麗事件爆發之后，海關有針對進口口罩逐批查驗，從8月10日至9月3日，關務署查獲577件、總共83萬0832片偽標MIT的非醫用口罩，全數扣押在海關，並未流入市面，後續調查結果會在2周內向外界報告。"
#詞性標註
seg = psg.cut(text)
#將詞性標註結果打印出來
for ele in seg:
    ele = list(ele)
    if str(ele[1]).startswith("n") and len(ele[1])>1:
        print("\t",ele)
    else:
        print(ele)
"""
def tokenize_static_words(msg)->dict:
    def random_token(count=8):
        sets = ["A","W","C","G","a","b","x","d","3","4"]
        sets_default = ["TOM","GAVIN","MAX","CANDY","ADITI","ALMA","AlYSSA","BETTY"]
        new_str = "["

        for _ in range(5):
            new_str += (random.choice(sets_default))
        new_str+="]"
        return new_str
    text = msg
    seg = psg.cut(text)
    re_token_mapping =dict()

    #
    new_str = ""
    for ele in seg:
        ele = list(ele)
        if ele[1] in static_label:
            #print("\t", ele)
            token_temp = random_token()
            re_token_mapping[token_temp] = ele[0]
            new_str += (" "+token_temp+" ")
        else:
            new_str+=ele[0]
    return {
        "new_str":new_str,
        "re_token_mapping":re_token_mapping
    }


#text = "蔡壁元指出佳麗事件爆發之后，海關有針對進口口罩逐批查驗，從8月10日至9月3日，關務署查獲577件、總共83萬0832片偽標MIT的非醫用口罩，全數扣押在海關，並未流入市面，后續調查結果會在2周內向外界報告。"
#tokenize_static_words(text)