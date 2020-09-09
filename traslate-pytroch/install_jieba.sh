curl -w -sS https://codeload.github.com/ldkrsi/jieba-zh_TW/zip/master > jieba.zip && \
unzip jieba.zip                             && \
rm jieba.zip
mv jieba-zh_TW-master/jieba/ ./
rm -rf jieba-zh_TW-master

