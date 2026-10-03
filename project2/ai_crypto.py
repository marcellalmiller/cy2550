from pathlib import Path
import os
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt_file(input_path: str, output_path: str, password: str) -> None:
    """Encrypt a file using AES-256-GCM with a password."""
    data = Path(input_path).read_bytes()

    # Random salt prevents identical passwords from producing the same key.
    salt = os.urandom(16)

    # Derive a 256-bit AES key from the password.
    key = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        600_000,
        dklen=32,
    )

    # GCM requires a unique nonce for each encryption.
    nonce = os.urandom(12)

    ciphertext = AESGCM(key).encrypt(nonce, data, None)

    # Store salt + nonce + ciphertext.
    Path(output_path).write_bytes(salt + nonce + ciphertext)
