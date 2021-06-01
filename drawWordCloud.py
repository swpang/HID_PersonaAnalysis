import numpy as np
import pandas as pd
import konlpy as kor
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv', sep=',', index_col=0, header=0, dtype=str)
data = df.to_numpy(dtype=str)

text = ""
for i in range(len(data[:,0])):
    text += data[i,7] + ' ' + data[i,8]

filtered_content = text.replace('(', ' ').replace(')', ' ').replace('/', ' ').replace(',', ' ')\
    .replace('+', ' ').replace('.', ' ').replace('-', ' ').replace('\n', ' ').replace('  ', ' ').replace('   ', ' ')
print(filtered_content)
Okt = kor.tag.Okt()
Okt_morphs = Okt.pos(filtered_content)

restricted_words=['것', '할', '수', '하는', '하지', '위해', '하여', '되어', '수', '등', '된', '때', '하려고', '하더라도', '장의', '때', '및', '함', '하였음', '해야'
                  , '않음', '하여야', '시', '통해', '큰', '후', '다시']

filtered_final = ""
for word, pos in Okt_morphs:
    if (pos == 'Noun') | (pos == 'Verb'):
        if word not in restricted_words:
            filtered_final += word + " "

print(filtered_final)


'''
wc = WordCloud(font_path='VitroTTF.ttf',
               background_color='white',
               width=4000,
               height=2000,
               max_words=75,
               max_font_size=900).generate(filtered_final)
wc.to_file('wordcloud.jpg')
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
'''