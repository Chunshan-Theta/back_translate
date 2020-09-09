curl -w -sS https://dl.fbaipublicfiles.com/fairseq/models/dynamicconv/wmt17.zh-en.dynamicconv-glu.tar.gz > wmt17_zh_en.tar.gz && \
tar -zxvf wmt17_zh_en.tar.gz                             && \
rm wmt17_zh_en.tar.gz

curl -w -sS https://dl.fbaipublicfiles.com/fairseq/models/dynamicconv/wmt17.zh-en.lightconv-glu.tar.gz > wmt17_zh_en.tar.gz && \
tar -zxvf wmt17_zh_en.tar.gz                             && \
rm wmt17_zh_en.tar.gz
