from pyquery import PyQuery as pq
import urllib.request
import os

#write the file
def writeFile(fileName, fileContent):
    if not os.path.exists('./src'):
        os.mkdir('src')
    
    if not os.path.isfile(fileName):
        f = open('src/'+fileName+'.java', 'w+')
        f.write('public class '+fileName + ' {\n')
        f.write(fileContent)
        f.write('\n}')
        f.close()
        return True
    else:
        return False

try:
    page = urllib.request.urlopen('http://stackoverflow.com/questions/513832/how-do-i-compare-strings-in-java')
    page_content = page.read().decode('utf-8')
    mainPage = pq(page_content)
    print(mainPage('#question-header').text())
    question = mainPage('#question-header').text()
    #write the source page to a file
    writeFile('java-'+question+'.html', page_content)
    i=0
    for codeSnippet in mainPage('pre code'):
        i += 1
        writeFile('impl'+str(i), pq(codeSnippet).text())
        #print(pq(codeSnippet).text(), end='\n----------------------\n')
except:
    print('error check your nerwork connection')

