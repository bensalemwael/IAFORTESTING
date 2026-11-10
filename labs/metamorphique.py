"""CT-AI AI-6.1.5 / HO-6.1.6 : détecter un défaut sans oracle grâce au test métamorphique.

Lancer : python labs/metamorphique.py
Le modèle ci-dessous simule une boîte noire qui contient un défaut volontaire.
Exercice : ajoutez votre propre relation, par exemple « ajouter une chambre ne baisse pas le prix ».
"""
from typing import Callable, Dict, List, Tuple

Case = Dict[str, int]

SOURCE_CASES: List[Case] = [
    {"surface": 45, "chambres": 1, "etage": 2},
    {"surface": 72, "chambres": 3, "etage": 5},
    {"surface": 95, "chambres": 3, "etage": 4},
    {"surface": 118, "chambres": 4, "etage": 1},
]
SURFACE_STEP = 10
SURFACE_DEFECT_THRESHOLD = 100
PRICE_PER_M2 = 3200
ROOM_BONUS = 9000
FLOOR_BONUS = 1500
DEFECT_DISCOUNT = 0.7


def model_price(case: Case) -> float:
    """Boîte noire : au-delà du seuil de surface, un défaut fait chuter le prix."""
    price = case["surface"] * PRICE_PER_M2 + case["chambres"] * ROOM_BONUS + case["etage"] * FLOOR_BONUS
    return price * DEFECT_DISCOUNT if case["surface"] >= SURFACE_DEFECT_THRESHOLD else price


def monotonic_surface(source: Case) -> Tuple[Case, bool]:
    """Monotonie : à caractéristiques égales, une surface plus grande ne baisse pas le prix."""
    follow_up = {**source, "surface": source["surface"] + SURFACE_STEP}
    return follow_up, model_price(follow_up) >= model_price(source)


def invariant_key_order(source: Case) -> Tuple[Case, bool]:
    """Invariance : l'ordre des attributs fournis ne change pas le prix."""
    follow_up = dict(reversed(list(source.items())))
    return follow_up, model_price(follow_up) == model_price(source)


RELATIONS: List[Tuple[str, Callable[[Case], Tuple[Case, bool]]]] = [
    ("Monotonie sur la surface", monotonic_surface),
    ("Invariance à l'ordre", invariant_key_order),
]


def main() -> None:
    for name, relation in RELATIONS:
        for source in SOURCE_CASES:
            follow_up, holds = relation(source)
            print(f"{'OK   ' if holds else 'ÉCHEC'} {name} : {source} -> {follow_up}")


if __name__ == "__main__":
    main()
