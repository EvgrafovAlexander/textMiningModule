from pymorphy2 import MorphAnalyzer
#библиотека регулярных выражений
import re

inpText = open('in.txt', 'r', encoding='utf8').read()
outSentences = open('outSentences.txt', 'w', encoding='utf8')
outWords = open('outWords.txt', 'w', encoding='utf8')
outWordsClean = open('outWordsClean.txt', 'w', encoding='utf8')
outWordsProcessed = open('outPofSfound.txt', 'w', encoding='utf8')

countWords = 0
countUnknownWords = 0

#разделение текста на предложения, результат в отдельный файл
sentences = inpText.split('. ')
for i in range(len(sentences)):
    print(sentences[i], file=outSentences)

#разделение предложений на слова без удаления спецсимволов, результат в отдельный файл
for sent in range(len(sentences)):
    words = sentences[sent].split()
    for word in range(len(words)):
        print(words[word], file=outWords)
    print('', file=outWords)

#разделение предложений на слова с удалением спецсимволов, результат в отдельный файл
for sent in range(len(sentences)):
    words = sentences[sent].split()
    for word in range(len(words)):
        print(re.sub(r"[:;,()#%!@*]", "", words[word].lower()), file=outWordsClean)
    print('', file=outWordsClean)

#разбиение предложений на слова, удаление спецсимволов, помещение предложений в множество
setOfsentences = []
for sent in range(len(sentences)):
    words = sentences[sent].split()
    setOfwords = []
    for word in range(len(words)):
        setOfwords.append(re.sub(r"[:;,()#%!@*]", "", words[word].lower()))
        print(setOfwords[word], file=outWordsClean)
    setOfsentences.append(setOfwords)
print(setOfsentences)

countSentences = len(setOfsentences)
for sent in range(countSentences):
    for word in range(len(setOfsentences[sent])):
        parseWord = MorphAnalyzer().parse(setOfsentences[sent][word])
        countWords += 1
        if 'UNKN'  in parseWord[0].tag:
            countUnknownWords += 1
        print(parseWord, file=outWordsProcessed)
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