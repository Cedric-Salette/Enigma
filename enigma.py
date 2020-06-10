
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

# Description des 5 rotors.
rotor_1 = ['E','K','M','F','L','G','D','Q','V','Z','N','T','O','W','Y','H','X','U','S','P','A','I','B','R','C','J']
rotor_2 = ['A','J','D','K','S','I','R','U','X','B','L','H','W','T','M','C','Q','G','Z','N','P','Y','F','V','O','E']
rotor_3 = ['B','D','F','H','J','L','C','P','R','T','X','V','Z','N','Y','E','I','W','G','A','K','M','U','S','Q','O']
rotor_4 = ['E','S','O','V','P','Z','J','A','Y','Q','U','I','R','H','X','L','N','F','T','G','K','D','C','M','W','B']
rotor_5 = ['V','Z','B','R','G','I','T','Y','U','P','S','D','N','H','L','X','A','W','M','J','Q','O','F','E','C','K']

#Description des deux réflécteurs
ref_A = ['Y','R','U','H','Q','S','L','D','P','X','N','G','O','K','M','I','E','B','F','Z','C','W','V','J','A','T']
ref_B = ['R','D','O','B','J','N','T','K','V','E','H','M','L','F','C','W','Z','A','X','G','Y','I','P','S','U','Q']


def lettre_en_nombre(lettre) : 
	return alphabet.index(lettre)


#Transformation des rotors et des reflecteurs en valeurs numériques
for i in range(26):
	rotor_1[i] = lettre_en_nombre(rotor_1[i])
	rotor_2[i] = lettre_en_nombre(rotor_2[i])
	rotor_3[i] = lettre_en_nombre(rotor_3[i])
	rotor_4[i] = lettre_en_nombre(rotor_4[i])
	rotor_5[i] = lettre_en_nombre(rotor_5[i])
	ref_A[i] = lettre_en_nombre(ref_A[i])
	ref_B[i] = lettre_en_nombre(ref_B[i])


#Selectionne un rotor 
def choix_rotor(numero):
	rotor = []
	if numero == 1:
		rotor = rotor_1
	elif numero ==2:
		rotor = rotor_2
	elif numero ==3:
		rotor = rotor_3
	elif numero ==4:
		rotor = rotor_4
	elif numero ==5:
		rotor = rotor_5
	return rotor


#Selection le reflecteur
def choix_reflecteur(numero):
	reflecteur = []
	if numero == 1:
		reflecteur = ref_A
	else:
		reflecteur = ref_B
	return reflecteur


#Permet à l'utilisateur de configurer le tableau de connexion
def configuration_cablage_de_depart():
	liste = []
	cables = input('Entrer les 6 paires de lettres reliées par un cable, en tapant les lettres dans l\'ordre : ')
	for i in range(12):
		liste.append(lettre_en_nombre(cables[i]))
	return liste

#Tourne le rotor d'un rang vers la gauche.
def decalage_un_rang(liste):
	a = liste[0]
	for i in range(25):
		liste[i] = liste[i + 1]
	liste[25] = a
	return liste
	
	
#Fonction qui retourne le rotor après avoir défini sa position initial
def pos_init_rotor(rotor, pos):
	for i in range(pos):
		decalage_un_rang(rotor)
	return rotor
	
	
	
#Passage d'une lettre dans les cablages de connexions
def valeur_apres_cablage_de_depart(valeur, liste):
	nouv = valeur
	if nouv in liste:
		n = liste.index(valeur)
		if n%2 == 0:
			nouv = liste[n + 1]
		else:
			nouv = liste[n - 1]
	return nouv


def passage_dans_un_rotor(rotor, valeur):
	return rotor[valeur]

def inverse_rotor(rotor, valeur):
	return rotor.index(valeur)
	
def passage_dans_le_reflecteur(reflecteur, valeur):
	return reflecteur[valeur]



#PROGRAMME

#Selection des rotors
i = input('Entrer le numero du premier rotor (1, 2, 3, 4 ou 5) : ')
i1 = int(i)
j = input('Entrer le numero du deuxieme rotor (1, 2, 3, 4 ou 5) : ')
j1 = int(j)
k = input('Entrer le numero du troisieme rotor (1, 2, 3, 4 ou 5) : ')
k1 = int(k)
R1 = choix_rotor(i1)
R2 = choix_rotor(j1)
R3 = choix_rotor(k1)

#Position initial des rotors
p1 = input('Entrer la position initiale du premier rotor choisi : ')
p2 = input('Entrer la position initiale du deuxieme rotor choisi : ')
p3 = input('Entrer la position initiale du troisieme rotor choisi : ')
a = R1.index(lettre_en_nombre(p1))
R1 = pos_init_rotor(R1, a)
b = R2.index(lettre_en_nombre(p2))
R2 = pos_init_rotor(R2, b)
c = R3.index(lettre_en_nombre(p3))
R3 = pos_init_rotor(R3, c)

#Choix du reflecteur
l = input('Entrer le numero du reflecteur (1 ou 2) :')
l1 = int(1)
ref = choix_reflecteur(l1)

#Configuration des cables | Fait dans l'initialisation

#Initialisation
cables = []
message = []
message_decode = []
tour = 0 #Permet de compter une à une les variables à décrypter

cables = configuration_cablage_de_depart()
message = input('Entrer le message à decoder : ')


while tour < len(message):
	if tour % 78 <= 25:
		nombre = lettre_en_nombre(message[tour])
		nouv_1 = valeur_apres_cablage_de_depart(nombre, cables)
		nouv_2 = passage_dans_un_rotor(R1, nouv_1)
		nouv_3 = passage_dans_un_rotor(R2, nouv_2)
		nouv_4 = passage_dans_un_rotor(R3, nouv_3)
		nouv_5 = passage_dans_le_reflecteur(ref, nouv_4)
		nouv_6 = inverse_rotor(R3, nouv_5)
		nouv_7 = inverse_rotor(R2, nouv_6)
		nouv_8 = inverse_rotor(R1, nouv_7)
		nouv_9 = valeur_apres_cablage_de_depart(nouv_8, cables)
		message_decode.append(alphabet[nouv_9])
		decalage_un_rang(R1)
	
	if tour % 78 > 25 and tour % 78 <= 51:
		decalage_un_rang(R2)
		nombre = lettre_en_nombre(message[tour])
		nouv_1 = valeur_apres_cablage_de_depart(nombre, cables)
		nouv_2 = passage_dans_un_rotor(R1, nouv_1)
		nouv_3 = passage_dans_un_rotor(R2, nouv_2)
		nouv_4 = passage_dans_un_rotor(R3, nouv_3)
		nouv_5 = passage_dans_le_reflecteur(ref, nouv_4)
		nouv_6 = inverse_rotor(R3, nouv_5)
		nouv_7 = inverse_rotor(R2, nouv_6)
		nouv_8 = inverse_rotor(R1, nouv_7)
		nouv_9 = valeur_apres_cablage_de_depart(nouv_8, cables)
		message_decode.append(alphabet[nouv_9])
	if tour % 78 > 51 and tour % 78 <= 77:
		decalage_un_rang(R3)
		nombre = lettre_en_nombre(message[tour])
		nouv_1 = valeur_apres_cablage_de_depart(nombre, cables)
		nouv_2 = passage_dans_un_rotor(R1, nouv_1)
		nouv_3 = passage_dans_un_rotor(R2, nouv_2)
		nouv_4 = passage_dans_un_rotor(R3, nouv_3)
		nouv_5 = passage_dans_le_reflecteur(ref, nouv_4)
		nouv_6 = inverse_rotor(R3, nouv_5)
		nouv_7 = inverse_rotor(R2, nouv_6)
		nouv_8 = inverse_rotor(R1, nouv_7)
		nouv_9 = valeur_apres_cablage_de_depart(nouv_8, cables)
		message_decode.append(alphabet[nouv_9])
	
	tour = tour + 1
	
	
print(message_decode)
		
