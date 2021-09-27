#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        valeur = []
        # TODO: demander les valeurs ici
        for i in range (0,11):
            valeur.append(input(f"Entrer une valeur  : "))
        valeur.sort()

    return valeur


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mot_1 = input(str("Entrez le premier mot:"))
        mot_2 = input(str("Entrez le deuxième mot:"))
        l1 = []
        l2 = []
        for lettre in mot_1 :
            l1.append(lettre)
        l1.sort()
        for lettre in mot_2 :
            l2.append(lettre)
        l2.sort()
    if l1 == l2:
        return True
    else :
        return False


def contains_doubles(items: list) -> bool:
    for i in items:
        if items.count(i) != 1 :
            return True
    return False


def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    return {}


def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    order()

    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
