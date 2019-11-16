"""
Showing how using Electronic Codebook is insecure
ECB should never be used because it hints about plaintext that is
exactly the same.
"""

from cryptography.hazmat.backends import default_backend
from ?