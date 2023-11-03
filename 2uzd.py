""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.

kas ir RSS?


"""

import feedparsen

# URL uz RSS plūsmu 

rss_ur1='https://news.google.com/home?hl=lv&gl=LV&ceid=LV:lv'

# iegūsim RSS plūsmas datus
kkk=feedparsen.parse(rss_ur1)

#parbauda un janoforme 

for entry in kkk.entries:
    print("Virsraksts: ", entry.title)
    print("Saite: ", entry.link)
    print("Publicēšanas datums:", entry.published)
    print('\n')
