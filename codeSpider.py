from pyquery import PyQuery as pq
import os

#write the file
def writeFile(fileName, fileContent):
    if not os.path.isfile(fileName):
        f = open('src/'+fileName, 'w+')
        f.write(fileContent)
        f.close()
        return True
    else:
        return False

try:
    mainPage = pq(url= 'http://stackoverflow.com/questions/513832/how-do-i-compare-strings-in-java')
except:
    print('error check your nerwork connection')
i=0
for codeSnippet in mainPage('pre code'):
    i += 1
    writeFile('impl'+str(i), pq(codeSnippet).text())
    #print(pq(codeSnippet).text(), end='\n----------------------\n')

