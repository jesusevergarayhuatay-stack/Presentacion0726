import json, base64
data = json.load(open('data.json'))
labels = {1:"Informe Defensorial N°001-2023-DP/ACSGO",2:"Informe Defensorial N°273",3:"Informe Defensorial 278",4:"Informe Defensorial 284",5:"Informe Defensorial 279",6:"Informe Jurídico Defensorial N°001-2025-DP/ACSGO",7:"Informe Técnico Legal N°003-2025-DP/ACSGO",8:"Informe Técnico Legal N°004-2025-DP/ACSGO"}
shorts = {1:"N°001-2023",2:"N°273",3:"N°278",4:"N°284",5:"N°279",6:"N°001-2025",7:"N°003-2025",8:"N°004-2025"}
for d in data:
    d['label']=labels[d['n']]; d['short']=shorts[d['n']]
DATA = json.dumps(data, ensure_ascii=False)
LOGO='data:image/png;base64,'+base64.b64encode(open('Defensoría_del_Pueblo.png','rb').read()).decode()
ANNIV='data:image/png;base64,'+base64.b64encode(open('Logo30anos_web.png','rb').read()).decode()
open('__parts.json','w').write(json.dumps({'DATA':DATA,'LOGO':LOGO,'ANNIV':ANNIV}))
print('parts ready', len(DATA))
