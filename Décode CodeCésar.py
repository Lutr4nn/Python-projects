def decalage(caractere_origine, key) :
    """renvoie le caractère codé obtenu à partir du caractère d'origine et du décalage key""" 
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if caractere_origine == ' ':                      # test si le caractère d'origine est un espace
        return ' '                                    # renvoie du caractère espace
    else : 
        index = alphabet.index(caractere_origine)     # donne la position (index) du caractere dans l'alphabet
        index_decal = index + key                     # réalise le décalage
        if index_decal > 25 :                         # test si le décalage est supérieure au 26ème caractère
            index_decal = index_decal - 26            # décalage de 26
        caractere_code = alphabet[index_decal]        # caractère codé
        return caractere_code                         
        
def chiffrement(texte, key):
    """renvoie le texte chiffré à l'aide de la clé key"""
    texte_chiffre = ''                                         # initialisation du texte chiffré comme chaine de caractère vide
    for char in texte:                                         # pour chaque caractère de texte
        texte_chiffre = texte_chiffre + decalage(char, key)     # concaténation du texte chiffré avec le caractère décalé
    return texte_chiffre                                               # renvoie du texte chiffré
    
def decalage_inverse(caractere_origine, key) :
    """renvoie le caractère codé obtenu à partir du caractère d'origine et du décalage key""" 
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if caractere_origine == ' ':                      # test si le caractère d'origine est un espace
        return ' '                                    # renvoie du caractère espace
    else : 
        index = alphabet.index(caractere_origine)     # donne la position (index) du caractere dans l'alphabet
        index_decal = index - key                     # réalise le décalage
        if index_decal > 25 :                         # test si le décalage est supérieure au 26ème caractère
            index_decal = index_decal - 26            # décalage de 26
        caractere_code = alphabet[index_decal]        # caractère codé
        return caractere_code
        
def dechiffrement(texte, key):
    """renvoie le texte déchiffré à l'aide de la clé key"""
    texte_chiffre = ''                                         # initialisation du texte chiffré comme chaine de caractère vide
    for char in texte:                                         # pour chaque caractère de texte
        texte_chiffre = texte_chiffre + decalage(char, - key)     # concaténation du texte chiffré avec le caractère décalé
    return texte_chiffre
    
def chiffrement_ascii(texte, key):
    """renvoie le texte chiffré à l'aide de la clé key"""
    texte_chiffre = ''
    for char in texte:
        code_ascii = ord(char)                                # code ascii du caractère
        if code_ascii != ord(' '): # test si le caractère d'origine est un espace
            code_ascii += key
            if code_ascii > ord('Z'):
                code_ascii += 26
        texte_chiffre += chr(code_ascii)
    return texte_chiffre 
        
def dechiffrement_ascii(texte, key):
    """Renvoie le texte déchiffré à l'aide de la clé key"""
    texte_chiffre = ''
    for char in texte:
        code_ascii = ord(char)  
        if code_ascii != ord(' '):  
            code_ascii -= key  
            if code_ascii < ord('A'): 
                code_ascii += 26  
        texte_chiffre += chr(code_ascii)
    return texte_chiffre

def main():
    choix = input("Souhaitez-vous chiffrer ou déchiffrer? (c/d) : ")
    texte = input("Entrez le texte : ").upper()  
    key = int(input("Entrez la clé (décalage) : "))

    if choix == 'c':
        methode = input("Souhaitez-vous utiliser la méthode ASCII? (o/n) : ")
        if methode == 'o':
            print('Texte chiffré (ASCII) :', chiffrement_ascii(texte, key))
        else:
            print('Texte chiffré :', chiffrement(texte, key))
    elif choix == 'd':
        methode = input("Souhaitez-vous utiliser la méthode ASCII? (o/n) : ")
        if methode == 'o':
            print('Texte déchiffré (ASCII) :', dechiffrement_ascii(texte, key))
        else:
            print('Texte déchiffré :', dechiffrement(texte, key))
    else:
        print("La mort ou le tchétché")

if __name__ == "__main__":
    main()