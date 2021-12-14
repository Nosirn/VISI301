# VISI301
CMI Informatique => Cours 301
Type de jeu :

- mode zombie
- survivre le plus longtemps à des vagues
- 2 modes différents ? : - survivre le plus lontemps
		         - défendre la base le plus longtemps


Joueur :

- on déplace le joueur (vue de dessus)
- il peut tirer en visant avec la souris
- nombre de point de vie (régénération naturelle)
- système monétaire
- système de score

Zombies :

- ils se déplacent vers une cible (le joueur ou la base et le joueur selon le mode)
- différents type de zombie
- les zombies arrivent par vagues

Objets :

- on peut acheter des objets avec l'argent que l'on a
- armes
- potion d'armure
- boost consommable sur une durée
- éléments interactif (posable, pièges, zone de soin)


Map :

- murs
- lac
- cache (accessible par le joueur mais pas par le zombie) / inverse possible
- armurerie pour acheter les objest
- base ?
- zones déblocables selon une condition ( argent et autre)
- éléments interactif ( pour débloquer des zones)

base :

- un grand nombre de PV

Installation packages:

$ pip install pygame

$ pip install pytmx

$ pip install pyscroll

$ pip install pygame-menu -U