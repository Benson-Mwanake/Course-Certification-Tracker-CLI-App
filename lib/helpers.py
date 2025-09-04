import os
from datetime import datetime


def clear_screen():
    """Clear terminal screen cross-platform."""
    os.system("cls" if os.name == "nt" else "clear")


def prompt_int(prompt_text, allow_blank=False):
    """Prompt for an integer. Returns int or None if blank allowed."""
    while True:
        val = input(prompt_text).strip()
        if allow_blank and val == "":
            return None
        if val.isdigit():
            return int(val)
        print("Please enter a whole number (digits only).")


def prompt_non_empty(prompt_text):
    """Prompt until user types a non-empty string."""
    while True:
        val = input(prompt_text).strip()
        if val:
            return val
        print("This field cannot be empty.")


def prompt_date(prompt_text, allow_blank=False):
    """
    Prompt for a date in YYYY-MM-DD. Returns a date object or None.
    """
    while True:
        val = input(prompt_text).strip()
        if allow_blank and val == "":
            return None
        try:
            return datetime.strptime(val, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date. Use format YYYY-MM-DD (e.g., 2025-01-31).")


def confirm(prompt_text="Are you sure? [y/N]: "):
    return input(prompt_text).strip().lower() in {"y", "yes"}


def divider(title=None):
    if title:
        print(f"---- {title} ".ljust(60, "-"))
    else:
        print("-" * 60)
