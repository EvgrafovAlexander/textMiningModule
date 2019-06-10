from pymorphy2 import MorphAnalyzer
#библиотека регулярных выражений
import re

inpText = open('in.txt', 'r', encoding='utf8').read()
controlList = open('checkedPofS.txt', 'r', encoding='utf8')
outWordsClean = open('outWordsClean.txt', 'w', encoding='utf8')
outPofSfound = open('outPofSfound.txt', 'w', encoding='utf8')

countWords = 0
countUnknownWords = 0

#разделение текста на предложения
sentences = inpText.split('. ')
countSentences = len(sentences)

#разделяем каждое предложение по словам
#убираем дополнительные знаки и символы
#записываем в outWordsClean слова по 1 в строку
#проводим морфологический анализ получаемых слов
#и записываем результат в outWordsProcessed
setOfsentences = []
realSetPoS = []
for sent in range(countSentences):
    words = sentences[sent].split()
    setOfwords = []
    for word in range(len(words)):
        curWord = re.sub(r"[:;,()#%!@*]", "", words[word].lower())
        parsedWord = MorphAnalyzer().parse(curWord)
        countWords += 1
        setOfwords.append(curWord)
        realSetPoS.append(parsedWord[0].tag)
        print(curWord, file=outWordsClean)
        print(parsedWord[0].tag, file=outPofSfound)
    setOfsentences.append(setOfwords)
    print('', file=outPofSfound)
    print('', file=outWordsClean)

#получаем данные из файла проверки ответов
ctrlSetPoS = []
for line in controlList:
    ctrlSetPoS.append(line.replace('\n', ''))

#сравнение найденных значений с истинными
correctPoS = 0
wrongPoS = 0
if len(ctrlSetPoS) == len(realSetPoS):
    for PoS in range(len(ctrlSetPoS)):
        if 'UNKN' in realSetPoS[PoS]:
            countUnknownWords += 1
        elif ctrlSetPoS[PoS] in realSetPoS[PoS]:
            correctPoS += 1
        else:
            wrongPoS += 1

print('Общее количество предложений:', countSentences)
print('Общее количество слов:', countWords)
print('Количество корректно определённых слов:', correctPoS)
print('Количество некорректно определённых слов:', wrongPoS)
print('Количество неопределённых слов:', countUnknownWords)
print('Эффективность:', "{0:.2f}".format((correctPoS / countWords) * 100) , '%')