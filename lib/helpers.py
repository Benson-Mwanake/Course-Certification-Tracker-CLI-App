import os
from datetime import datetime


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def prompt_int(prompt_text, allow_blank=False):
    while True:
        val = input(prompt_text).strip()
        if allow_blank and val == "":
            return None
        if val.isdigit():
            return int(val)
        print("Please enter a number.")


def prompt_date(prompt_text, allow_blank=False):
    """
    Accepts YYYY-MM-DD. Returns a date or None.
    """
    while True:
        val = input(prompt_text).strip()
        if allow_blank and val == "":
            return None
        try:
            return datetime.strptime(val, "%Y-%m-%d").date()
        except ValueError:
            print("Please use format YYYY-MM-DD (e.g., 2025-01-31).")


def confirm(prompt_text="Are you sure? [y/N]: "):
    return input(prompt_text).strip().lower() in {"y", "yes"}


def divider(title=None):
    print("-" * 40 if not title else f"---- {title} ".ljust(40, "-"))
