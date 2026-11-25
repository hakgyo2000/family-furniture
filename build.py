import os
d=os.path.dirname(os.path.abspath(__file__))
src=open(os.path.join(d,'src.html'),encoding='utf-8').read()
i=src.index('<div class="app"')
head,body=src[:i],src[i:]
out=('<!doctype html>\n<html lang="ko"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
 '<meta name="robots" content="noindex,nofollow">\n'+head+'</head><body>\n'+body+'</body></html>\n')
os.makedirs(os.path.join(d,'docs'),exist_ok=True)
open(os.path.join(d,'docs','index.html'),'w',encoding='utf-8').write(out)
print(len(out))
