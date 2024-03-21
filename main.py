from urllib import request
from collections import Counter
from functools import reduce
from operator import add

def stripTags(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]

    inside = 0
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text

def removeStopwords(lista_palavras, stopwords):
    return [w for w in lista_palavras if w not in stopwords]

def listaPalavrasPFreqDici(lista_palavras):
    freq_palavras = [lista_palavras.count(p) for p in lista_palavras]
    return dict(list(zip(lista_palavras,freq_palavras)))

stopwords = ['a','agora','ainda','alguém','algum','alguma','algumas','alguns','ampla','amplas','amplo','amplos','ante','antes','ao','aos','após','aquela','aquelas','aquele','aqueles','aquilo','as','até','através','cada','coisa','coisas','com','como','contra','contudo','da','daquele','daqueles','das','de','dela','delas','dele','deles','depois','dessa','dessas','desse','desses','desta','destas','deste','deste','destes','deve','devem','devendo','dever','deverá','deverão','deveria','deveriam','devia','deviam','disse','disso','disto','dito','diz','dizem','do','dos','e','é','ela','elas','ele','eles','em','enquanto','entre','era','essa','essas','esse','esses','esta','está','estamos','estão','estas','estava','estavam','estávamos','este','estes','estou','eu','fazendo','fazer','feita','feitas','feito','feitos','foi','for','foram','fosse','fossem','grande','grandes','há','isso','isto','já','la','lá','lhe','lhes','lo','mas','me','mesma','mesmas','mesmo','mesmos','meu','meus','minha','minhas','muita','muitas','muito','muitos','na','não','nas','nem','nenhum','nessa','nessas','nesta','nestas','ninguém','no','nos','nós','nossa','nossas','nosso','nossos','num','numa','nunca','o','os','ou','outra','outras','outro','outros','para','pela','pelas','pelo','pelos','pequena','pequenas','pequeno','pequenos','per','perante','pode','pude','podendo','poder','poderia','poderiam','podia','podiam','pois','por','porém','porque','posso','pouca','poucas','pouco','poucos','primeiro','primeiros','própria','próprias','próprio','próprios','quais','qual','quando','quanto','quantos','que','quem','são','se','seja','sejam','sem','sempre','sendo','será','serão','seu','seus','si','sido','só','sob','sobre','sua','suas','talvez','também','tampouco','te','tem','tendo','tenha','ter','teu','teus','ti','tido','tinha','tinham','toda','todas','todavia','todo','todos','tu','tua','tuas','tudo','última','últimas','último','últimos','um','uma','umas','uns','vendo','ver','vez','vindo','vir','vos','vós']

url = 'https://pt.wikipedia.org/wiki/Energia_renov%C3%A1vel'
url2 = 'https://www.enelgreenpower.com/pt/learning-hub/energias-renoveveis'
url3 = 'https://brasilescola.uol.com.br/geografia/fontes-renovaveis-energia.htm'

response = request.urlopen(url)
response2 = request.urlopen(url2)
response3 = request.urlopen(url3)
html = response.read().decode('UTF-8')
html2 = response2.read().decode('UTF-8')
html3 = response3.read().decode('UTF-8')

text = stripTags(html).lower()
text2 = stripTags(html2).lower()
text3 = stripTags(html3).lower()

words_list = text.split()
words_list2 = text2.split()
words_list3 = text3.split()

words_list = removeStopwords(words_list, stopwords)
words_list2 = removeStopwords(words_list2, stopwords)
words_list3 = removeStopwords(words_list3, stopwords)

aux_word_frequency = []
aux_word_frequency2 = []
aux_word_frequency3 = []

for word in words_list:
  if word.isalpha():
    aux_word_frequency.append(word)

for word in words_list2:
  if word.isalpha():
    aux_word_frequency2.append(word)

for word in words_list3:
  if word.isalpha():
    aux_word_frequency3.append(word)

words_list = aux_word_frequency
words_list2 = aux_word_frequency2
words_list3 = aux_word_frequency3  

dictionary = listaPalavrasPFreqDici(words_list)
dictionary2 = listaPalavrasPFreqDici(words_list2)
dictionary3 = listaPalavrasPFreqDici(words_list3)

filtered_dict = {key:val for key, val in dictionary.items() if val > 2}
filtered_dict2 = {key:val for key, val in dictionary2.items() if val > 2}
filtered_dict3 = {key:val for key, val in dictionary3.items() if val > 2}

dict_list = [ filtered_dict, filtered_dict2, filtered_dict3 ]

result_dict = reduce(add, (map(Counter, dict_list)))

print(result_dict)