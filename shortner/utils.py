import string
from django.utils.crypto import get_random_string

BASE62 = string.ascii_letters + string.digits

def generate_short_code(length=6):
    return get_random_string(length , BASE62)