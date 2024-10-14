import os
import sys
import subprocess


def run_docker():
    command = ["docker", "run", "-it", "-p", "8000:8000", "edwin350/oc_lettings:latest"]
    subprocess.run(command)

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    if len(sys.argv) > 1 and sys.argv[1] == "run_docker":
        run_docker()
    else:
        execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
