# BIApp  

A enlever RANGDEM -> car redondance avec ANNEDEM  
Modifier RANGAGEDEM avec les catégories supérieures à 56 ans en '56-+' pour comparaison ave RANGAGEAD (à voir)  
RANGADH -> attention champ vide ou null ==> veut dire moins d'un an dans la banque donc possiblement remplacer par 0 !  
Se fier à CDMOTDEM pour les gens qui ont démissionner dans la table 2 (et pas à la date DTDEM car certaines inchangées)  
  
Trier les données, virer les colonnes redondantes ou non "utiles"  
Que faire des valeurs manquantes ?  
Changer les valeurs des champs en numérique ou non  
(ACP ?)  
Normaliser les valeurs numériques ? (StandardScaler ?)  
Discréditer les valeurs nominales ? (get_dummies de la lib pandas ?)
  
Une fois les données prêtes, comment on les découpes (80% apprentissage, 10% test, 10% validation ?)  
  
Puis après tout ça --> méthode de classification, SVM, k plus proche voisin, +1 a choisir  
### Proposition pour le choix de la méthode :  
Arbre de décision (DecisionTreeClassifier)  
Régression logistique (LogisticRegression)  
  
Pour K plus proche voisins a besoin de metrique de distance (problème possible pour les valeurs non numériques --> les ignorer ou les convertir)  
  
voir sklearn.neighbors
  
  
### table 2
Démission :  
CDSITFAM pas de F ni P  
NBENF pas de supérieur ou égal à 5  
CDCATCL pas de 22, 40, 50, 98  
CDTMT pas de 4,6  

### table 1
CDTMT pas de 4  
CDCATCL pas de 50, 98 (pas de supérieur à 40)  
NBENF pas de supérieur à 6  
range numeric car ordre

## Merge tables
Attributs semblables:  
- cdsexe
- dtdem
- cdtmt
- cdcatcl
- dtadh
- cdmotdem
- agedem = dtdem - dtnais

## KNN
faire courbe de perf en fonction de k