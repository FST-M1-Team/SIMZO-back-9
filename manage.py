import os
import sys
from pathlib import Path

def main():
    # 1. On force Python à regarder DANS le dossier 'src'
    base_dir = Path(__file__).resolve().parent
    src_path = str(base_dir / "src")
    if src_path not in sys.path:
        sys.path.insert(0, src_path)

    # Modifiez pour pointer vers .local
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Django n'est pas installé dans le venv.") from exc
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
