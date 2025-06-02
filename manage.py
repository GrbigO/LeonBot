#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


if __name__ == "__main__":
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "leonbot.settings")

    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)



