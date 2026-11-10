"""CT-AI HO-3.4.2 : observer un perceptron apprendre la fonction ET, époque après époque.

Lancer : python labs/perceptron.py
À essayer : remplacer SAMPLES par la fonction OU exclusif (XOR). L'apprentissage
n'aboutit jamais, car ce problème n'est pas linéairement séparable.
"""
from typing import List, Tuple

SAMPLES =[((0, 0), 0), ((0, 1), 0), ((1, 0), 0), ((1, 1), 1)]
LEARNING_RATE = 0.2
MAX_EPOCHS = 30


def predict(weights: List[float], bias: float, inputs: Tuple[int, int]) -> int:
    activation = sum(w * x for w, x in zip(weights, inputs)) + bias
    return 1 if activation > 0 else 0


def train_epoch(weights: List[float], bias: float) -> Tuple[List[float], float, int]:
    errors = 0
    for inputs, target in SAMPLES:
        error = target - predict(weights, bias, inputs)
        errors += abs(error)
        weights = [w + LEARNING_RATE * error * x for w, x in zip(weights, inputs)]
        bias += LEARNING_RATE * error
    return weights, bias, errors


def main() -> None:
    weights, bias = [0.0, 0.0], 0.0
    for epoch in range(1, MAX_EPOCHS + 1):
        weights, bias, errors = train_epoch(weights, bias)
        rounded = [round(w, 2) for w in weights]
        print(f"Époque {epoch:2d} : poids={rounded} biais={bias:.2f} erreurs={errors}")
        if errors == 0:
            print("Apprentissage terminé : aucune erreur sur cette époque.")
            return
    print("Pas de convergence : le problème n'est peut-être pas linéairement séparable.")


if __name__ == "__main__":
    main()
