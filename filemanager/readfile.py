import xml.etree.ElementTree as ET
import sys
import re
def get_staging_files(source_file):
    path_list = list()
    with open(source_file , 'tr' , encoding='utf-8') as rf:
        tree=ET.parse(rf)
    pattern=r'\$\w+\$\/'
    patternh=r'\$\w+\$(\/[^(..)]+)+'
    root=tree.getroot()
    components=tree.findall('.//component[@name="ChangeListManager"]')
    for com in components:
        print(com.tag+"@@@"+com.get('name'))
        default_change=com.findall('.//list[@default="true"]')
        for change in default_change:
            files=change.findall('.//change')
            for file in files:
                lu=''
                if file.get('beforePath')!=None:
                    print("found@@:"+file.get('beforePath'))
                    lu=re.split(pattern,file.get('beforePath'))[1]
                else:
                    print(file.get('afterPath'))
                    temp=re.split(pattern,file.get('afterPath'))[1]
                    lu=(re.split(pattern,file.get('afterPath'))[1])
                    print('lulu....'+lu)
                if re.match(patternh,lu,re.M)!=None:
                    path_list.append(lu)
    return path_list
