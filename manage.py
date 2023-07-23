import os
from dotenv import load_dotenv

# Load environment variables from .env file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, 'envs/.env'))


#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import sys
import re
import os

# def load_env():
#
#     try:
#         with open('D:\SoftUni\djangoProject\MYpetstagram\envs\.env') as f:
#             content = f.read()
#     except IOError:
#         content = ''
#     for line in content.splitlines():
#         m = re.match(r'\A([A-Za-z_0-9]+)=(.*)\Z', line)
#         if m:
#             key, val = m.group(1), m.group(2)
#             os.environ.setdefault(key, val)


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MYpetstagram.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    # load_env()
    main()
