"""CT-AI AI-5.1.5 / HO-5.1.7 : appliquer des contraintes de dataset sur un petit jeu de données.

Lancer : python labs/contraintes_dataset.py
Exercice : avant de lancer, repérez à la main les anomalies et nommez la contrainte qui détecte chacune.
"""
from datetime import date
from typing import Any, Dict, List

Row = Dict[str, Any]

ROWS: List[Row] = [
    {"ref": "T-1", "age": 34, "pays": "FR", "commande": date(2026, 1, 5), "livraison": date(2026, 1, 9)},
    {"ref": "T-2", "age": 130, "pays": "FR", "commande": date(2026, 1, 6), "livraison": date(2026, 1, 8)},
    {"ref": "T-3", "age": None, "pays": "TN", "commande": date(2026, 1, 7), "livraison": date(2026, 1, 10)},
    {"ref": "T-4", "age": "41", "pays": "BE", "commande": date(2026, 1, 9), "livraison": date(2026, 1, 4)},
    {"ref": "T-5", "age": 29, "pays": "TN", "commande": date(2026, 1, 11), "livraison": date(2026, 1, 14)},
    {"ref": "T-6", "age": 29, "pays": "TN", "commande": date(2026, 1, 11), "livraison": date(2026, 1, 14)},
]
AGE_MIN, AGE_MAX = 18, 99
IDENTIFIER_ATTRIBUTE = "ref"


def check_missing(rows: List[Row]) -> List[str]:
    return [f"Missing : {r['ref']}, age absent" for r in rows if r["age"] is None]


def check_type(rows: List[Row]) -> List[str]:
    return [
        f"Type : {r['ref']}, age {r['age']!r} n'est pas un entier"
        for r in rows
        if r["age"] is not None and not isinstance(r["age"], int)
    ]


def check_range(rows: List[Row]) -> List[str]:
    return [
        f"Range : {r['ref']}, age {r['age']} hors de [{AGE_MIN}, {AGE_MAX}]"
        for r in rows
        if isinstance(r["age"], int) and not AGE_MIN <= r["age"] <= AGE_MAX
    ]


def check_duplicate(rows: List[Row]) -> List[str]:
    """Quasi-doublons : lignes identiques en dehors de leur identifiant."""
    contents = [{k: v for k, v in r.items() if k != IDENTIFIER_ATTRIBUTE} for r in rows]
    return [
        f"Duplicate : {rows[i]['ref']} identique à une ligne précédente"
        for i, content in enumerate(contents)
        if content in contents[:i]
    ]


def check_useful(rows: List[Row], attribute: str) -> List[str]:
    distinct = {r[attribute] for r in rows}
    return [f"Useful : toutes les valeurs de {attribute} sont uniques"] if len(distinct) == len(rows) else []


def check_greater_than(rows: List[Row]) -> List[str]:
    return [
        f"Greater Than : {r['ref']}, livraison antérieure à la commande"
        for r in rows
        if r["livraison"] <= r["commande"]
    ]


def main() -> None:
    findings = (
        check_missing(ROWS)
        + check_type(ROWS)
        + check_range(ROWS)
        + check_duplicate(ROWS)
        + check_useful(ROWS, IDENTIFIER_ATTRIBUTE)
        + check_greater_than(ROWS)
    )
    print("\n".join(findings) or "Aucune anomalie.")


if __name__ == "__main__":
    main()
