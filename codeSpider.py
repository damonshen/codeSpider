from pyquery import PyQuery as pq

try:
    mainPage = pq(url= 'http://stackoverflow.com/questions/513832/how-do-i-compare-strings-in-java')
except:
    print('error check your nerwork connection')
for codeSnippet in mainPage('pre code'):
    print(pq(codeSnippet).text(), end='\n----------------------\n')
