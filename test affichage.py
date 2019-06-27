
###test affichage
liste_exemples=[]
axeX=[]
somme=[]
i=0
for j in range(99):
    ex=[]
    
    for k in range (duree_apprentissage):
        axeX.append(i*6)
        i+=1
        somme.append(puissance[i]+X[i])
        ex.append(puissance[i]+X[i])
    liste_exemples.append(ex)

affichage=[]
preds=clf.predict(liste_exemples)
for k in range(len(preds)):
    affichage=affichage+[preds[k] for z in range(duree_apprentissage)]

pl.figure(1)
pl.subplot(211)
pl.plot(axeX, somme)


pl.subplot(212)
pl.plot(axeX, affichage)
pl.show()