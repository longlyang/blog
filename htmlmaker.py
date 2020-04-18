import os
from lxml import etree



relativepath=r'C:\Users\long\PycharmProjects\htmlmaker'

postdir=relativepath + r'\post'
postindextemplate=relativepath + r'\post\index-template.html'
postindex=relativepath + r'\post\index.html'
codedir=relativepath + r'\code'
codeindextemplate=relativepath + r'\code\index-template.html'
codeindex=relativepath + r'\code\index.html'
notedir=relativepath + r'\note'
noteindextemplate=relativepath + r'\note\index-template.html'
noteindex=relativepath + r'\note\index.html'
indextemplate=relativepath + r'\index-template.html'
index=relativepath + r'\index.html'

alllist=[] #[#div...]
postlist=[] #[#div...]
codelist=[] #[#div...]
notelist=[] #[#div...]

def parsedir(dir):
    '''

    :param dir:
    :return: [(date,name,filelocation)...]
    '''
    l=[]
    for root, dirs, files in os.walk(dir):
        for file in files:
            try:
                date,name=file.split('_')
                l.append((date,name,file))
            except:
                continue
    return l

def replaceCRLFwithLF(file):
    '''
    strip &#13;
    :param file:
    :return:
    '''
    data=''
    with open(file,'r',encoding="utf-8") as f:
        data=f.read().replace('&#13;', '')
    with open(file,'w',encoding="utf-8")as f:
        f.write(data)

def gethtmldoc(file):
    '''

    :param file:
    :return: etree doc obj
    '''
    Parser = etree.HTMLParser(encoding="utf-8")
    return etree.parse(file,Parser)

def writebackfile(etreedoc,file):
    '''
    write etree doc str to file
    :param etreedoc:
    :param file:
    :return:
    '''
    etreedoc.write(file,pretty_print=False, encoding='utf-8',method='html')
    replaceCRLFwithLF(file)

def insertintodoc(templatefile,divlist,outputfile):
    '''
    insert div to doc
    :param templatefile:
    :param divlist:
    :param outputfile:
    :return:
    '''
    doc=gethtmldoc(templatefile)
    divlocation = doc.xpath("//div[@class='content']")[0]
    for i in divlist:
        divlocation.insert(0,etree.XML(i))
    writebackfile(doc,outputfile)

def main():
    for i in parsedir(postdir):
        item='<div class="content-item">'
        item=item+'<div class="content-item-row-date">'+i[0]+'</div> '
        item=item+'<div class="content-item-row-title"><a href="./post/'+i[2]+'">'+i[1].rsplit('.')[0]+'</a></div>'
        item=item+'</div>'
        alllist.append(item)
        item = '<div class="content-item">'
        item = item + '<div class="content-item-row-date">' + i[0] + '</div> '
        item = item + '<div class="content-item-row-title"><a href="./' + i[2] + '">' + i[1].rsplit('.')[0] + '</a></div>'
        item = item + '</div>'
        postlist.append(item)

    for i in parsedir(codedir):
        item='<div class="content-item">'
        item=item+'<div class="content-item-row-date">'+i[0]+'</div> '
        item=item+'<div class="content-item-row-title"><a href="./code/'+i[2]+'">'+i[1].rsplit('.')[0]+'</a></div>'
        item=item+'</div>'
        alllist.append(item)
        item = '<div class="content-item">'
        item = item + '<div class="content-item-row-date">' + i[0] + '</div> '
        item = item + '<div class="content-item-row-title"><a href="./' + i[2] + '">' + i[1].rsplit('.')[0] + '</a></div>'
        item = item + '</div>'
        codelist.append(item)

    for i in parsedir(notedir):
        item='<div class="content-item">'
        item=item+'<div class="content-item-row-date">'+i[0]+'</div> '
        item=item+'<div class="content-item-row-title"><a href="./note/'+i[2]+'">'+i[1].rsplit('.')[0]+'</a></div>'
        item=item+'</div>'
        alllist.append(item)
        item = '<div class="content-item">'
        item = item + '<div class="content-item-row-date">' + i[0] + '</div> '
        item = item + '<div class="content-item-row-title"><a href="./' + i[2] + '">' + i[1].rsplit('.')[0] + '</a></div>'
        item = item + '</div>'
        notelist.append(item)
    
    insertintodoc(postindextemplate,postlist,postindex)
    insertintodoc(codeindextemplate,codelist,codeindex)
    insertintodoc(noteindextemplate,notelist,noteindex)
    insertintodoc(indextemplate,alllist,index)

if __name__ == '__main__':
    main()