"""
OTRS related functions
"""

import re

RE_OTRS = r"\bpermission\s*=\s*{{\s*PermissionOTRS\s*\|\s*id\s*=\s*(\d+)"
RE_OTRS_PENDING = r"{{\s*OTRS pending"


def is_otrs_pending(text):
    """
    Check if OTRS is pending
    """

    match = re.search(RE_OTRS_PENDING, text, re.IGNORECASE)
    if match:
        return True
    return False


def get_otrs(text):
    """
    Get OTRS from PermissionOTRS string
    """

    match = re.search(RE_OTRS, text, re.IGNORECASE)
    if match:
        return match.groups(1)[0]
    return None
