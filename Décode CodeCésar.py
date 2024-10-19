def decalage(caractere_origine, key):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if caractere_origine == ' ':
        return ' '
    else:
        index = alphabet.index(caractere_origine)
        index_decal = index + key
        if index_decal > 25:
            index_decal = index_decal - 26
        caractere_code = alphabet[index_decal]
        return caractere_code

def chiffrement(texte, key):
    texte_chiffre = ''
    for char in texte:
        texte_chiffre = texte_chiffre + decalage(char, key)
    return texte_chiffre

def decalage_inverse(caractere_origine, key):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    if caractere_origine == ' ':
        return ' '
    else:
        index = alphabet.index(caractere_origine)
        index_decal = index - key
        if index_decal > 25:
            index_decal = index_decal - 26
        caractere_code = alphabet[index_decal]
        return caractere_code

def dechiffrement(texte, key):
    texte_chiffre = ''
    for char in texte:
        texte_chiffre = texte_chiffre + decalage(char, -key)
    return texte_chiffre

def chiffrement_ascii(texte, key):
    texte_chiffre = ''
    for char in texte:
        code_ascii = ord(char)
        if code_ascii != ord(' '):
            code_ascii += key
            if code_ascii > ord('Z'):
                code_ascii += 26
        texte_chiffre += chr(code_ascii)
    return texte_chiffre

def dechiffrement_ascii(texte, key):
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
    if choix != 'c' and choix != 'd':
        print("La mort ou le tchétché")
    else:
        texte = input("Entrez le texte : ").upper()
        key = int(input("Entrez la clé (décalage) : "))
        if choix == 'c':
            methode = input("Souhaitez-vous utiliser la méthode ASCII? (o/n) : ")
            if methode == 'o':
                print('Texte chiffré (ASCII) :', chiffrement_ascii(texte, key))
            elif methode == 'n':
                print('Texte chiffré :', chiffrement(texte, key))
            else:
                print("La mort ou le tchétché")
        elif choix == 'd':
            methode = input("Souhaitez-vous utiliser la méthode ASCII? (o/n) : ")
            if methode == 'o':
                print('Texte déchiffré (ASCII) :', dechiffrement_ascii(texte, key))
            elif methode == 'n':
                print('Texte déchiffré :', dechiffrement(texte, key))
            else:
                print("La mort ou le tchétché")

if __name__ == "__main__":
    main()
