{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "37105553-3258-4c2e-89a4-8235502384e4",
   "metadata": {},
   "source": [
    "## Exercice 1 : les impairs"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "e741b61e-ae69-4c8b-a603-e04c3f4f1e0b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n",
      "5\n",
      "7\n",
      "9\n",
      "11\n"
     ]
    }
   ],
   "source": [
    "a=3\n",
    "b=12\n",
    "\n",
    "liste = 0\n",
    "\n",
    "for element in range (a, b,2):\n",
    "    \n",
    "    print (element)\n",
    "\n",
    "# je pense qu il fallait tester pour element=un nombre entier et si decimal, ne prendre que l'entier pour réafficher la fonction\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "235f0416-f29c-4e91-a636-703bdb24e9fc",
   "metadata": {},
   "source": [
    "## Exercice 2 : le jeu du plus ou moins"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "00a67265-3893-43f6-a82f-7fbf8b3d773e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Entrez un nombre plus petit\n"
     ]
    }
   ],
   "source": [
    "\n",
    "choix_ordi = 5\n",
    "\n",
    "choix_utilisateur = 25\n",
    "#choix_utilisateur = input (\"Entrez un chiffre entre 1 et 100\")\n",
    "if choix_ordi>choix_utilisateur:\n",
    "    print (\"Entrez un nombre plus grand\")\n",
    "elif choix_ordi<choix_utilisateur:\n",
    "    print (\"Entrez un nombre plus petit\")\n",
    "else:\n",
    "    print (\"c'est le bon nombre\") \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6447fd4f-c6f6-4db9-a708-0e31cef12c73",
   "metadata": {},
   "source": [
    "### option 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "45134ec1-ce03-4ebb-bf2a-577b02dc14cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "c'est le bon nombre\n"
     ]
    }
   ],
   "source": [
    "choix_ordi = 5\n",
    "\n",
    "choix_utilisateur = 5\n",
    "#choix_utilisateur = input (\"Entrez un chiffre entre 1 et 100\")\n",
    "if choix_utilisateur>100:\n",
    "    print(\"message d'erreur, il faut un nombre entre 1 et 100\")\n",
    "elif choix_utilisateur<1:\n",
    "    print(\"message d'erreur, il faut un nombre entre 1 et 100\")\n",
    "elif choix_ordi>choix_utilisateur:\n",
    "    print (\"Entrez un nombre plus grand\")\n",
    "elif choix_ordi<choix_utilisateur:\n",
    "    print (\"Entrez un nombre plus petit\")\n",
    "else:\n",
    "    print (\"c'est le bon nombre\") \n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26e8b737-a7a9-48e6-b70e-86ceac05af51",
   "metadata": {},
   "source": [
    "## Exercice 3 : les plus grands nombres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "id": "2c255524-69eb-44f2-b9b0-5dbf73484ff2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[34101, 87948, 17612, 18639, 21513, 85084, 12695, 94683, 56145, 51269, 47813, 76128, 76618, 58108, 67745, 96499, 98365, 30877, 48341, 47265, 77607, 99158, 5082, 86906, 48303, 81299, 8272, 28684, 17754, 287, 68942, 76795, 17943, 69345, 67498, 5565, 12433, 97052, 21335, 27216, 98434, 10588, 68073, 13966, 56689, 60483, 10891, 17827, 74950, 71215, 92249, 85916, 68341, 73218, 61820, 72010, 19236, 616, 93465, 54289, 96848, 79, 67792, 88911, 88377, 47026, 45897, 84235, 80156, 98833, 45289, 20914, 55509, 32941, 15507, 42316, 84363, 94491, 19650, 13565, 84684, 80994, 79979, 72148, 52381, 7712, 72008, 5797, 84456, 13057, 77299, 40090, 15000, 56155, 42130, 4894, 7396, 38363, 28757, 93628]\n"
     ]
    }
   ],
   "source": [
    "from random import randint as rd\n",
    "liste = []\n",
    "for i in range(100):\n",
    "    liste.append(rd(0, 100000) )\n",
    "print(liste)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "id": "5e56d002-7253-4321-b17f-4ac8b16dcf1f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#utiliser un dictionnaire et quantile 0,9\n",
    "#1 les classer par ordre croissant"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 92,
   "id": "90669ead-16ca-4fe2-8686-6d0c980d9bd8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "99158\n"
     ]
    }
   ],
   "source": [
    "print(max(liste))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 113,
   "id": "4623d6d9-24d7-4e68-a8fe-dcf52e223ca7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "93481.3\n"
     ]
    }
   ],
   "source": [
    "limite = np.quantile((liste), 0.9)\n",
    "print (limite)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "9315aed0-7594-4bf7-9433-0f38da6df54d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "94683\n",
      "96499\n",
      "98365\n",
      "99158\n",
      "97052\n",
      "98434\n",
      "96848\n",
      "98833\n",
      "94491\n",
      "93628\n"
     ]
    }
   ],
   "source": [
    "for i in liste :\n",
    "    if i >limite :\n",
    "        print (i)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 116,
   "id": "e1aa0c1b-34b0-4a2d-9d21-15159a0f5361",
   "metadata": {},
   "outputs": [],
   "source": [
    "# deuxieme version avec len"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "id": "052aa1f2-0fe5-463a-acdf-b76865958376",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[  287   616  4894  5082  5565  5797  7396  7712  8272 10588 10891 12433\n",
      " 12695 13057 13565 13966 15000 15507 17612 17754 17827 17943 18639 19236\n",
      " 19650 20914 21335 21513 27216 28684 28757 30877 32941 34101 38363 40090\n",
      " 42130 42316 45289 45897 47026 47265 47813 48303 48341 51269 52381 54289\n",
      " 55509 56145 56155 56689 58108 60483 61820 67498 67745 67792 68073 68341\n",
      " 68942 69345 71215 72008 72010 72148 73218 74950 76128 76618 76795 77299\n",
      " 77607 79979 80156 80994 81299 84235 84363 84456 84684 85084 85916 86906\n",
      " 87948 88377 88911 92249 93465 93628 94491 94683 96499 96848 97052 98365\n",
      " 98434 98833 99158]\n"
     ]
    }
   ],
   "source": [
    "liste_ordonnee = np.unique(liste)\n",
    "print(liste_ordonnee)\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 168,
   "id": "665c8562-239b-40f0-b226-d211726f368c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[93497.6]\n"
     ]
    }
   ],
   "source": [
    "m = np.quantile(liste_ordonnee,[0.9])\n",
    "print(m)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "id": "e19710e3-cec9-4ee9-8f1d-0e600b9fc26e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "93628\n",
      "94491\n",
      "94683\n",
      "96499\n",
      "96848\n",
      "97052\n",
      "98365\n",
      "98434\n",
      "98833\n",
      "99158\n"
     ]
    }
   ],
   "source": [
    "for i in liste_ordonnee:\n",
    "    if i>m:\n",
    "        print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "237ab3d7-09b8-48fe-a44f-33279011e016",
   "metadata": {},
   "source": [
    "## Exercice 4 : les algorithmes de tri"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8355baea-be61-401e-939d-45224ed0493a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3a9b101-e7dd-4fbc-9a9d-d41e1ee06208",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "60d79828-daec-4ec9-95a3-08dfd36db3e7",
   "metadata": {},
   "source": [
    "## Exercice 5 : des conversions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 185,
   "id": "57f0286e-e0a4-44fc-bc45-e3973a43cbd9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "108766539725\n",
      "9\n",
      "7\n",
      "17\n",
      "17\n",
      "35\n",
      "Dans 3430061596791935255 secondes, il y a 108766539725 années, 9 mois, 7 jours\n",
      "17 heures, 17 minutes, 35 secondes\n"
     ]
    }
   ],
   "source": [
    "#soit s l'input \"entrez un nombre de secondes\"\n",
    "s = 3430061596791935255\n",
    "\n",
    "annee = s//31536000\n",
    "print(annee)\n",
    "mois = (s-annee*31536000)//2629800\n",
    "print(mois)\n",
    "jours = (s-annee*31536000-mois*2629800)//86400\n",
    "print(jours)\n",
    "heures = (s-annee*31536000-mois*2629800-jours*86400)//3600\n",
    "print(heures)\n",
    "minutes = (s-annee*31536000-mois*2629800-jours*86400-heures*3600)//60\n",
    "print(minutes)\n",
    "secondes = (s-annee*31536000-mois*2629800-jours*86400-heures*3600-minutes*60)\n",
    "print(secondes)\n",
    "print(f\"Dans {s} secondes, il y a {annee} années, {mois} mois, {jours} jours\")\n",
    "print(f\"{heures} heures, {minutes} minutes, {secondes} secondes\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 186,
   "id": "86634e10-8706-4023-936e-864c93e1daaa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# deuxieme programme"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 196,
   "id": "afdb6e9f-3187-4f0f-a0ab-415e3a91a929",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15.537600994406464\n",
      "15.54\n"
     ]
    }
   ],
   "source": [
    "vitesse_fournie = 25\n",
    " \n",
    "vitesse_kmh = vitesse_fournie/1609*1000\n",
    "print(vitesse_kmh)\n",
    "\n",
    "vitesse_kmh= str(round( vitesse_kmh, 2))\n",
    "print(vitesse_kmh)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5ad8825f-db1c-4a95-ba34-d757725892ea",
   "metadata": {},
   "source": [
    "## Exercice 6 : le triangle de Pascal"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 253,
   "id": "99026f82-d8f4-4c01-9c5f-925ac2c9b43c",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "'return' outside function (<ipython-input-253-092797090828>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-253-092797090828>\"\u001b[0;36m, line \u001b[0;32m6\u001b[0m\n\u001b[0;31m    return valeur_haute\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m 'return' outside function\n"
     ]
    }
   ],
   "source": [
    "ligne = 5\n",
    "colonne = 3\n",
    "def \n",
    "valeur_haute = 1\n",
    "for i in range(1,n):\n",
    "    valeur_haute=(valeur_haute)*(i)\n",
    "return valeur_haute"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b811f0e-5d1f-4e5c-99cf-5a6000628884",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "080610cf-b871-4977-a595-88e76adf0c4b",
   "metadata": {},
   "source": [
    "## Exercice 7 : manipulations de dictionnaires"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "aabab6ef-9aa6-46ed-a705-2266988ed283",
   "metadata": {},
   "source": [
    "Écrire une fonction qui échange les clés et les valeurs d'un dictionnaire (ce qui permettra par exemple de transformer un dictionnaire anglais/français en un dictionnaire français/anglais). On suppose qu’il n’y a pas de valeurs en double pour simplifier."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 291,
   "id": "e3d76844-808b-4836-af4d-314c460f95f9",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "mot_anglais\n"
     ]
    }
   ],
   "source": [
    "input = (\"Veuillez saisir un mot: \")\n",
    "dico_francais = {\"mot_francais\":\"bonjour\"}\n",
    "dico_anglais = {\"mot_anglais\":\"hello\"}\n",
    "\n",
    "for mot in dico_francais :\n",
    "#echange le mot en francais en anglais\n",
    "    \n",
    "    mot = \"mot_francais\"\n",
    "    mot_ang = \"mot_anglais\"\n",
    "    mot = mot_ang\n",
    "    print(mot)\n",
    "  \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "26e3f56b-e2c8-4a53-8fbc-98d500b97314",
   "metadata": {},
   "source": [
    "## Exercice 8 : manipulations de fichiers textes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "db785ae2-12c6-41ab-b022-e63c737b132a",
   "metadata": {},
   "source": [
    "Écrire un script qui permet de créer et de relire aisément un fichier texte. Votre programme demandera d'abord à l'utilisateur d'entrer le nom du fichier. Ensuite il lui proposera le choix, soit d'enregistrer de nouvelles lignes de texte, soit d'afficher le contenu du fichier. L'utilisateur devra pouvoir entrer ses lignes de texte successives en utilisant simplement la touche <Enter> pour les séparer les unes des autres. Pour terminer les entrées, il lui suffira d'entrer une ligne vide (c'est-à-dire utiliser la touche <Enter> seule)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "47167368-0b46-4bae-8534-7dbc89241f5a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Entrez le nom du fichier:\n"
     ]
    }
   ],
   "source": [
    "input = (\"Entrez le nom du fichier:\")\n",
    "print(input)\n",
    "\n",
    "\n",
    "a = \"entrer_des_lignes\"\n",
    "b = \"afficher_le_contenu_du_fichier\"\n",
    "def choix (a,b):\n",
    "    if choix == a:\n",
    "        print (\"Entrer vos lignes de texte successives en utilisant simplement la touche <Enter> pour les séparer les unes des autres. Pour terminer les entrées, il vous suffira d'entrer une ligne vide (c'est-à-dire utiliser la touche <Enter> seule).\")\n",
    "    else :\n",
    "        f = open(\"test.txt\",'r')\n",
    "        message1 = f.read()\n",
    "        print(\"J affiche le contenu du fichier\")\n",
    "    \n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "217dceea-7c00-476a-9a33-e7e15614cdf6",
   "metadata": {},
   "source": [
    "Écrire un script qui génère automatiquement un fichier texte contenant les tables de multiplication de 2 à 30 (chacune d'entre elles incluant 20 termes seulement).\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 353,
   "id": "366440b8-4d2e-4ced-999d-6c76fb6513f5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'str'>\n",
      "580\n"
     ]
    }
   ],
   "source": [
    "element = [1,2,3,4]\n",
    "for element in range (0,21):\n",
    "    for i in range (2,30):\n",
    "        table = i*element\n",
    "#        print(table)\n",
    "table2 = str(table)\n",
    "print (type(table2))\n",
    "print (table2)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d3f11a93-2a17-4aed-a6ce-bc18ab240650",
   "metadata": {},
   "source": [
    "Écrire un script qui recopie un fichier texte en triplant tous les espaces entre les mots.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "19e30d0d-2456-4293-81b7-36ecb0d4f25d",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "texte = \"test.txt\"\n",
    "\n",
    "def elimine(texte):\n",
    "    espaces = \" \"\n",
    "    for espace in espaces:\n",
    "        texte = texte.replace(espace, \"   \")\n",
    "    print(texte)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ec83465d-3437-4117-98f0-262dc35385b0",
   "metadata": {},
   "source": [
    "À partir de deux fichiers préexistants A et B, construisez un fichier C qui contienne alternativement une ligne de A, une ligne de B... et ainsi de suite jusqu'à atteindre la fin de l'un des deux fichiers originaux. Complétez ensuite C avec les éléments restant sur l'autre.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "fb3a4e81-05d2-4fe0-8c3e-164209edd78b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bonjour, la promo Dev IA Euskadi\n",
      "Aujourd'hui, nous manipulons les fichiers txt\n",
      "avec l'exercice 8\n",
      " Bonjour, la promo Dev IA Euskadi\n",
      "Aujourd'hui, nous manipulons les fichiers txt\n",
      "avec l'exercice 8\n",
      "mais ce n est pas si facile que ça !\n",
      "3\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "fichierA = [\"test.txt\"]\n",
    "fichierB = [\"test2.txt\"]\n",
    "fichierC = []\n",
    "f = open(\"test.txt\",'r')\n",
    "message1 = f.read()\n",
    "f = open(\"test2.txt\",'r')\n",
    "message2 = f.read()\n",
    "print(message1, message2)\n",
    "\n",
    "f = open(\"test.txt\", 'r')\n",
    "text=f.readlines()\n",
    "NumberOfLine = len(text)\n",
    "print(NumberOfLine)\n",
    "f = open(\"test2.txt\", 'r')\n",
    "text=f.readlines()\n",
    "NumberOfLine2 = len(text)\n",
    "print(NumberOfLine2)\n",
    "\n",
    "f.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03a59f1c-dc2b-4ccc-ab35-983bd8bdfe83",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "0cfeb78e-8f91-4ff7-96f3-0a0a84a9883d",
   "metadata": {},
   "source": [
    "Exercice 9 : quelques notes\n",
    "\n",
    "Écrire un programme permettant d'entrer des notes d'élèves d’élèves sur 20 jusqu’à ce l’utilisateur saisisse une note vide. Construire une liste et à chaque nouvelle entrée, afficher le nombre de notes entrées, la note la plus élevée, la note la plus basse, la moyenne de toutes les notes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c762bdc1-84ca-4fb4-8de2-25b436eed690",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[18, 20, 15], [2, 10, 20, 4, 7, 12]]\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'data' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-17-0ea43a751b1b>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0mliste\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mnotes_nicolas\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0mnotes_ophelie\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      5\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mliste\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 6\u001b[0;31m \u001b[0mdata\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mliste\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mastype\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfloat\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      7\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      8\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mlongueur\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'data' is not defined"
     ]
    }
   ],
   "source": [
    "notes_nicolas = [18,20,15]\n",
    "notes_ophelie = [2,10,20,4,7,12]\n",
    "\n",
    "liste = [notes_nicolas,notes_ophelie]\n",
    "print(liste)\n",
    "data[liste].astype(float)\n",
    "\n",
    "print(longueur)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5aee356c-99c8-47a5-b633-21818972e95e",
   "metadata": {},
   "outputs": [],
   "source": [
    "noms = ['a','b','c']\n",
    "notes = [1,2,3]\n",
    "mon_dic = {}\n",
    "\n",
    "for i in range(len(noms)):\n",
    "    mon_dic[noms[i]] = notes[i]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5da02e0a-8af8-447f-a76f-20b7c78c9fbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "47afdc96-5eb3-4281-92fb-fac438e8a225",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
