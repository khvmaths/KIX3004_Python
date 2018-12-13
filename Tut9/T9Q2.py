f=open('article.txt','r')
l=f.read()
re=""
l=l.split('. ')
for i in l:
    re+=i[0].upper()+i[1:]+'. '
g=open('article-cap.txt','w')
g.write(re[:-3])