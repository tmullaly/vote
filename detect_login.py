#!/usr/bin/env python3
"""
Detect the current user's login name and print it.
"""

from __future__ import annotations

import getpass
import os
import pwd
import sys


def detect_login_name() -> str:
    """
    Return the best-available login name.
    """
    try:
        # Preferred when a controlling terminal is available.
        return os.getlogin()
    except OSError:
        pass

    # Fallback to environment-aware user resolution.
    user = getpass.getuser()
    if user:
        return user

    # Final fallback based on effective UID.
    try:
        return pwd.getpwuid(os.geteuid()).pw_name
    except KeyError as exc:
        raise RuntimeError("Unable to determine login name") from exc


def main() -> int:
    print(detect_login_name())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
