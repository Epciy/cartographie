
from  restos import liste_restos,liste_restos_2018,liste_resto_disponible,molinel_list

# affichage des informations sur un restaurant, à compléter
def affiche_resto (resto):
    print('[',resto.get('pos'),']',end=' ')
    print(resto.get('nom'))
    print()

# boucle sur tous les restaurants, pour affichage
for resto in liste_restos:
    affiche_resto(resto)

#2.Affichage de nombre de restaurants disponibles
def affichage_nombre_resto(resto):
    return len(resto)
print("Le nombre de restaurants disponible :",affichage_nombre_resto(liste_restos))

#3.le calcule  d'avis  été donnés au total.  la moyenne d'avis  reçus par chaque restaurant.
def nombre_avis_total(restos):
    total_avis=0
    for resto in restos:
        total_avis+=resto["votes"]
    return total_avis

print("le nombre d'avis total : ",nombre_avis_total(liste_restos))

def moyenne_avis(restos):
    moyenne=nombre_avis_total(restos)//affichage_nombre_resto(restos)
    return moyenne
print("la moyenne d'avis  reçus par chaque restaurant: ",moyenne_avis(liste_restos))

#4.Afficher la moyenne des notes, ainsi que l'écart-type.
def moyenne_note(restos):
    total=0
    for resto in restos:
        total+=resto["note"]
    moyenne=total/affichage_nombre_resto(restos)
    return moyenne
print("La moyenne des notes :",moyenne_note(liste_restos))
# L'écart-type
"""" l'écart-type :  E=squareroot(sum((xi-n)**2)/N)
 E: ecart type
 xi=note de chaque restaurant
 n=moyenne de notes
 N=le nombre total de restaurant 
""" 
import math
N=affichage_nombre_resto(liste_restos)
n=moyenne_note(liste_restos)
def ecart_type(restos):
    notes=[]
    for resto in restos :
        xi=(resto["note"]-n)**2
        notes.append(xi)
    print(notes)
    ecart_type=math.sqrt(sum(notes)/N)
    return ecart_type
print("L'écart type : ",ecart_type(liste_restos))
#5..Affichage de nombre des restaurants ayant une note de 4,5 ou plus
def affichage_resto_bien_classé(restos):
    result=0
    for resto in restos :
        if resto['note']>=4.5:
           result+=1 
    return result
      
print("Affichage de nombre des restaurants ayant une note de 4,5 ou plus : ",affichage_resto_bien_classé(liste_restos))

#6.le calucule de la moyenne des latitudes et des longitudes. À quel endroit correspondent ces coordonnées (utiliser par exemple ce site ou directement Google Maps pour visualiser sur une carte la localisation calculée) ?
 # le nombre des restaurants.
def moyenne_los_lat(restos):
    N=affichage_nombre_resto(restos)
    d={}
    moy1=0
    moy2=0
    for resto in restos :
        moy1+=resto["lon"]
        moy2+=resto["lat"]
    d["longitude"]=moy1/N
    d["latitude"]=moy2/N
    return d
print("la moyenne des latitudes et des longitudes: ",moyenne_los_lat(liste_restos))
print("ces coordonnées correspondent À  l'endroit :  13 Place du Trocadéro et du 11 Novembre, 75016 Paris, France")
    
#Meme question mais avec plus de 50 avis
ans=[] 
for resto in liste_restos:
    if resto["votes"]>50:
        ans.append(resto)
N=len(ans)
pour_avis=moyenne_los_lat(ans)

print("la moyenne des latitudes et des longitudes  seulment pour les restaurants avec plus de 50 avis : ",pour_avis)

print("ces coordonnées correspondent À  l'endroit  : 5 Avenue Anatole France, 75007 Paris, France")

#7.Indiquer si oui ou non il y a un restaurant dans la rue alphonse mercier. Idem avec la rue de la porte .
for resto in liste_restos:
    if resto["rue"]=="la rue alphonse mercier" or resto["rue"]=="la rue de la porte":
        print("un restaurant est dans l'endroit indiqué")
    print("aucun restaurant dans l'endroit indiqués")
#8.
def position(restos):
    for resto in restos :
        if resto["pos"]==1:
            print("restaurant classé à la première position: ",resto)
        if resto["pos"]==len(restos):
            print("le restaurant placé à la dernière position: ",resto)
position(liste_restos)
#9.
for resto in liste_resto_disponible:
    if resto['nom']=='La duccasse':
        print("les informations disponibles sur le restaurant la ducasse :",resto)
    if resto["rue"]=="rue des postes":
        print("les informations disponibles sur le restaurant qui se trouve au 14 rue des postes : ",resto)

#10.
res=[]
for r in molinel_list:
    res.append(r["nom"])

print("la liste des restaurants se trouvant rue du molinel : ",res)

#11.
def max_avis(restos):
    max_avis=0
    for resto in restos:
        max_avis=max(max_avis,resto["votes"])
    for resto in restos:
        if resto["votes"]==max_avis:
            return resto["nom"]
print("le restaurant ayant reçu le plus d'avis: ",max_avis(molinel_list))

#12.
def affichage(resto_2018):
    print("Le nombre de restaurants disponible :",affichage_nombre_resto(resto_2018))
    print("le nombre d'avis total : ",nombre_avis_total(resto_2018))
    print("la moyenne d'avis  reçus par chaque restaurant: ",moyenne_avis(resto_2018))
    print("La moyenne des notes :",moyenne_note(resto_2018))
    print("Affichage de nombre des restaurants ayant une note de 4,5 ou plus : ",affichage_resto_bien_classé(resto_2018))
    
    print("la moyenne des latitudes et des longitudes: ",moyenne_los_lat(resto_2018))
affichage(liste_restos_2018)
#13.
from collections import defaultdict
from archive import archives
last_year="2022"
def resto_disparus(archive):
    data=defaultdict(list) # collecter les noms des restaurants pour chaque année
    for date in archive :
        for resto in archive[date]:
            data[date].append(resto["nom"])
    res=[[],[]]
    
    for date in data:
        for resto in data[date]:
            if date!=last_year and resto not in data[last_year] and resto not in res[0]:
                res[0].append(resto)
        for resto in data[last_year]:
            if date!=last_year and resto not in data[date] and resto not in res[1]:
                res[1].append(resto)
    return res
print("restaurants ont disparu derniére année : ",resto_disparus(archives)[0])
print("les restaurants qui sont apparus lors de la dernière année",resto_disparus(archives)[1])  

#14.le restaurant qui a le plus progressé dans le classement
nouveau_resto=resto_disparus(archives)[1]
#reperer lesresto existe depuis longtemps
ancien_resto=[]

for resto in archives[last_year]:
    if resto["nom"] not in nouveau_resto:
        ancien_resto.append(resto['nom'])


def classment(archive):
    data=defaultdict(list)
    for date in archive :
        for resto in archive[date]:
            if resto['nom'] in ancien_resto:
                data[resto["nom"]].append(resto["votes"])
    print(data)
    for k,v in data.items():
        if v==sorted(v):
            print("le restaurant qui a le plus progressé dans le classement : ",k)
        else:
            print("le restaurant qui a chuté le plus durement: ",k)       

classment(archives)
#15.
def evolution(archive):
    data=defaultdict(list)
    for date in archive :
        for resto in archive[date]:
            if resto['nom'] in ancien_resto:
                data[resto["nom"]].append([date,resto["votes"]])
    return data
print("l'évolution d'un restaurant donné au fil des années : ",evolution(archives))

#16.17.
def address_partagé(archive):
    data=defaultdict(list)
    for resto in archive[last_year]:
        data[resto["rue"]].append(resto["nom"])
    #afficher la rue qui est plusieur restaurant
    res=[]
    for key,value in data.items():
        if len(value)>1:
            res.append(key)

    return res
print("la ou les rue(s) ayant le plus de restaurants : ",address_partagé(archives))
  
#18.19.
def meilleur_resto(archive):
    res=[[],[]]
    for date in archive:
        for resto in archive[date]:
            if resto["note"]>4 and resto["rue"] not in res[0] :
                res[0].append(resto["rue"])
            elif resto["note"]<4 and resto["rue"] not in res[1]:
                res[1].append(resto["rue"])
    return res
print("la meilleure rue pour les restaurants : ",meilleur_resto(archives)[0])

#19.
print("la rue à ne pas fréquenter pour ses restaurants : ",meilleur_resto(archives)[1])

#20.les restaurants par ordre de classement
def classment_restaurants(archive):
    classment=defaultdict(list)

    for date in archive:
        for resto in archive[date]:
            if resto["nom"] not in classment[resto["note"]]:
                classment[resto["note"]].append(resto["nom"])
    keys=sorted(classment)
    d={i:classment[i] for i in keys}
    return [i for i in d.values()]
print(" les restaurants par ordre de classement (ordre ascendant): ",classment_restaurants(archives))
#21.medianne note /medianne avis
def key_arr(archive,x):
    res=[]
    for date in archive :
        for resto in archive[date]:
            if not resto[x] in res:
                res.append(resto[x])
    return res
note_arr=sorted(key_arr(archives,"note"))
avis_arr=sorted(key_arr(archives,"votes"))

def median(x):
    half=len(x)//2
    if not len(x)%2:
        return (x[half - 1] + x[half]) / 2.0
    return x[half]  
print("médianne note : ",median(note_arr))
print("médianne avis : ",median(avis_arr)) 
 
#22.voir cartographie.py et Untitled.ipynb
# la cartographie des restaurants lillois se trouve sur "map.html" merci zoom vers Lille ,france 

