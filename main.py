import requests

url='http://www.jaduniv.edu.in/'
url='http://www.jaduniv.edu.in/requiredfiles/intermediate_content_default.php'
url='http://www.jaduniv.edu.in/requiredfiles/display_notices.php?type=l&nc=all&Submit=View'
url='http://www.jaduniv.edu.in/requiredfiles/display_notices.php?type=l&nc=Admission&Submit=View'
data=requests.get(url)
cont=data.content
text=data.text
print(data.status_code)
dic={}
#print(text)
#tag=text.find('<div class="noticeDes"')
tag=text.find('<a href="#')
text=text[tag+1:]
while tag>-1 :
    #print(tag)
    io=text.find('#')
    ic=text.find('" onclick=')
    id=text[io+1:ic]
    #print(ic,id)
    close=text.find('>')
    end=text.find('</a>')
    title=text[close+1:end]
    sic=text.find('id="')
    sie=text.find('" name="')
    sid=text[sic+5:sie]
    pdfhome='http://www.jaduniv.edu.in/'
    keywords=['sports','Sports','FET','B.Tech','Quota','QUOTA','SPORTS','U.G.','Engg.','Tech.','Pharmacy','Courses']
    #print(ie,ic)
    #print(sid,id,title)
    dic[id]=title
    for keyword in keywords:
        if keyword in title:
            print(sid,id,title)
            break
        #else:
            #print(' n')




    #tag=text.find('<div class="noticeDes"')
    tag=text.find('<a href="#')
    text=text[tag+1:]
#print(dic)
'''
writting in excel

import xlsxwriter     
      
book = xlsxwriter.Book('Example2.xlsx')     
sheet = book.add_sheet()     
       
# Rows and columns are zero indexed.     
row = 0    
column = 0    
      
content = ["Parker", "Smith", "John"]     
      
# iterating through the content list     
for item in content :     
      
    # write operation perform     
    sheet.write(row, column, item)     
      
    # incrementing the value of row by one with each iterations.     
    row += 1    
          
book.close()  
'''