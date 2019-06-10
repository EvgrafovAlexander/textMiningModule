from pymorphy2 import MorphAnalyzer
#библиотека регулярных выражений
import re

inpText = open('in.txt', 'r', encoding='utf8').read()
outWordsClean = open('outWordsClean.txt', 'w', encoding='utf8')
outWordsProcessed = open('outPofSfound.txt', 'w', encoding='utf8')

countWords = 0
countUnknownWords = 0

#разделение текста на предложения
sentences = inpText.split('. ')
countSentences = len(sentences)

#разбиение предложений на слова, удаление спецсимволов, помещение предложений в множество
setOfsentences = []

for sent in range(countSentences):
    words = sentences[sent].split()
    setOfwords = []
    for word in range(len(words)):
        finalWord = re.sub(r"[:;,()#%!@*]", "", words[word].lower())
        setOfwords.append(finalWord)
        parseWord = MorphAnalyzer().parse(finalWord)
        countWords += 1
        if 'UNKN'  in parseWord[0].tag:
            countUnknownWords += 1
        print(setOfwords[word], file=outWordsClean)
        print(parseWord, file=outWordsProcessed)
    setOfsentences.append(setOfwords)
    print('', file=outWordsClean)
    print('', file=outWordsProcessed)

print('Общее количество предложений: ', countSentences)
print('Общее количество слов: ', countWords)
print('Количество определённых слов: ', countWords - countUnknownWords)
print('Количество неопределённых слов: ', countUnknownWords)


#print(*MorphAnalyzer().parse('кочерга'))


'''
for line in inpText:
    print(inpText[line])


print(MorphAnalyzer().parse('кочерга')[0].inflect({'plur', 'gent'}))

print(MorphAnalyzer().parse('думающему')[0].normal_form)

print(MorphAnalyzer().parse('фазан'))
'''