# myscript.py
import os

# Définit les hash good et bad ici
good = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
bad = "c1a4be04b972b6c17db242fc37752ad517c29402"

# Commandes bisect
os.system(f"git bisect start {bad} {good}")
exit_code = os.system("git bisect run python manage.py test")

# Affiche le résultat final
if exit_code == 0:
    print("Bisect terminé avec succès.")
else:
    print("Bisect a détecté un échec.")
