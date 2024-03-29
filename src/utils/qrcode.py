import os

import qrcode

from . import new_uuid

def generate_qr(string, *path, prefix, filename = None):
    path      = os.path.join(*path)
    os.makedirs(os.path.join(prefix, path), exist_ok=True)
    c = qrcode.make(string)
    path = os.path.join(path, f"{filename or new_uuid()}.png")
    c.save(os.path.join(prefix, path))
    return path