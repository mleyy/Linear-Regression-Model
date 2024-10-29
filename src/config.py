import os
class Config(object):
    # Use a secure method to generate a default secret key if not provided
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24).hex())
    PORT = int(os.environ.get('APP_PORT', 9090))  # Ensure PORT is an integer
