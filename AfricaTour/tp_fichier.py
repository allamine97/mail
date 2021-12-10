import io
def nombreVoyelles(chaine):
    voyelles=["a","o","i","u","e","y","A","O","I","U","E","Y"]
    s=0
    for i in voyelles:
        cnt=chaine.count(i)
        s=s+cnt
    return s
def nombreconsonnes(chaine):
    consonnes=["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
    s=0
    for i in consonnes:
        cnt=chaine.count(i)
        s=s+cnt
    return s
def verifierChiffre(chaine):
    res=" "
    if(chaine.isdigit()):
        res="le fichier contient bien un chiffre"
    else:
        res="le fichier ne contient pas de chiffre"
    return res
a=io.open("fichier.txt","r")
nbrLignes=len(a.readlines())
a.close()
a=io.open("fichier.txt","r")
nbrMots=len(a.read().split())
a.close()
a=io.open("fichier.txt","r")
ch=a.read()
a.close()
##Test Console
print(nombreconsonnes(ch))
print(nombreVoyelles(ch))
print(verifierChiffre(ch))
print(nbrMots)
print(nbrLignes)
##Fin Console
b=io.open("compterendu.txt","w")
b.write("Le nombre de ligne est : "+ str(nbrLignes) + " , le nombre de mots est : " + str (nbrMots) + " nombre de voyelles : " + str(nombreVoyelles(ch)) + " nombre de consonnes : " + str(nombreconsonnes(ch)) + " et " +verifierChiffre(ch))
b.close()
