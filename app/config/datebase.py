from dotenv import load_dotenv
import os

load_dotenv()


class DatabaseEnv:
    CONNECT_STRING = os.getenv("CONNECT_STRING")
