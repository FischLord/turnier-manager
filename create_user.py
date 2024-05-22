from app import create_app
from app.extensions import db
from app.models.user import User

app = create_app()
app.app_context().push()

# Erstelle einen neuen Benutzer
new_user = User(username="admin", email="admin@example.com", password="password")

# Füge den Benutzer zur Sitzung hinzu und speichere ihn in der Datenbank
db.session.add(new_user)
db.session.commit()

print("Beispielbenutzer erstellt!")
