#!/usr/bin/env python3

import argparse
import random
import sys

def generate_map(width, height, wall_prob, seed):
    """Génère une carte avec des murs ('o') et espaces ('.') de manière déterministe."""
    random.seed(seed)
    return [
        ''.join([
            'o' if random.random() < wall_prob else '.'
            for _ in range(width)
        ])
        for _ in range(height)
    ]

def save_map(map, filename):
    """Sauvegarde la carte dans un fichier."""
    with open(filename, 'w') as f:
        f.write(f"{len(map)}\n")
        f.write('\n'.join(map))
        f.write('\n')

def main():
    parser = argparse.ArgumentParser(description="Générateur de cartes déterministes pour BSQ.")
    parser.add_argument("width", type=int, help="Largeur de la carte")
    parser.add_argument("height", type=int, help="Hauteur de la carte")
    parser.add_argument("randomness", type=float, help="Probabilité de mur (entre 0.0 et 1.0)")
    parser.add_argument("seed", type=int, help="Graine pour la reproductibilité")
    parser.add_argument("-o", "--output", type=str, help="Fichier de sortie (optionnel)", default=None)
    parser.add_argument("--auto-save", action="store_true", help="Sauvegarde automatiquement la carte dans un fichier")

    args = parser.parse_args()

    if args.width <= 0 or args.height <= 0:
        sys.exit("Erreur : La largeur et la hauteur doivent être > 0.")
    if not (0.0 <= args.randomness <= 1.0):
        sys.exit("Erreur : La probabilité doit être entre 0 et 1.")

    map = generate_map(args.width, args.height, args.randomness, args.seed)

    # Sortie
    if args.auto_save:
        filename = f"map_{args.width}x{args.height}_r{int(args.randomness * 100)}_s{args.seed}.txt"
        save_map(map, filename)
        print(f"Carte sauvegardée dans '{filename}'.")

    elif args.output:
        filename = args.output if args.output.endswith('.txt') else f"{args.output}.txt"
        save_map(map, filename)
        print(f"Carte sauvegardée dans '{filename}'.")
    else:
        print(f"{args.height}")
        print('\n'.join(map))

if __name__ == "__main__":
    main()