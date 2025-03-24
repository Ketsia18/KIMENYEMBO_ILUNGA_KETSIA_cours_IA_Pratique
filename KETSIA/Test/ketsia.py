import math 
def calculer_volume_cone(rayon,hauteur):
    return (1/3)* math.pi *rayon**2 * hauteur

    rayon = float(input("Entrez le rayon du cone : "))
    hauteur = float(input("entrez la hauteur du cone :"))

    volume = calculer_volume_cone(rayon, hauteur)
     print(f"le volume du cone est de {volume : 2f} unités cubes.")