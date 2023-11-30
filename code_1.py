# Fonction de chiffrement SDES (exemple à partir du lien fourni)
def sdes(message, key):
    # Implementation de SDES (à remplacer par votre propre implémentation)
    # ...
    pass

# Fonction de cassage brutal
def cassage_brutal(message_chiffre, taille_cle1, taille_cle2):
    for k1 in range(2 ** taille_cle1):
        for k2 in range(2 ** taille_cle2):
            tentative = sdes(sdes(message_chiffre, k1), k2)
            if tentative == message_chiffre:
                return k1, k2
    return None, None

# Exemple d'utilisation
taille_cle1 = 8
taille_cle2 = 8
message_chiffre = sdes(sdes("message clair", 42), 77)  # Exemple de chiffrement

cle1_trouvee, cle2_trouvee = cassage_brutal(message_chiffre, taille_cle1, taille_cle2)

print("Clé 1 trouvée:", cle1_trouvee)
print("Clé 2 trouvée:", cle2_trouvee)
