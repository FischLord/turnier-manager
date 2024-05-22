import subprocess
import os
import signal
import atexit
from threading import Thread
from app import create_app

app = create_app()

# Globale Variable für den Tailwind-Prozess
tailwind_process = None

def run_tailwind():
    """Führt den Tailwind CSS Watcher im Hintergrund aus."""
    global tailwind_process
    tailwind_process = subprocess.Popen(
        ["npm", "run", "build:css"], 
        cwd=os.path.dirname(os.path.abspath(__file__))
    )

def cleanup():
    """Beendet den Tailwind CSS Watcher."""
    global tailwind_process
    if tailwind_process:
        tailwind_process.terminate()
        tailwind_process.wait()

if __name__ == "__main__":
    # Registriere die Cleanup-Funktion, um sicherzustellen, dass der Tailwind-Prozess beendet wird
    atexit.register(cleanup)
    
    # Erstelle einen Thread für den Tailwind Watcher
    tailwind_thread = Thread(target=run_tailwind)
    tailwind_thread.start()

    # Starte die Flask-Anwendung im Hauptthread
    try:
        app.run(debug=True)
    except KeyboardInterrupt:
        pass
    finally:
        cleanup()
