from app import create_app, db
from app.models import Livres
import os
import json
from pathlib import Path

app = create_app()


def load_fixtures():
    # chemin = Path(__file__).cwd() / "fixtures" / "Livres.json"
    livres_path = os.path.join(os.path.dirname(__file__), 'app', "./fixtures/Livres.json")
    with open(livres_path, 'r' , encoding='utf-8') as file:
        livres = json.load(file)
        print(livres)

    for livre in livres:
        livre = Livres(**livre)
        db.session.add(livre)

    db.session.commit()
    print("Fixtures loaded successfully.")


with app.app_context():
    db.create_all()

    db.drop_all()
    db.create_all()
    # fixtures
    load_fixtures()
    print("Database created successfully")

if __name__ == "__main__":
    app.run()
