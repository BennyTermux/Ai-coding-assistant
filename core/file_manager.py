import os
from config.config_loader import Config

class FileManager:

    @staticmethod
    def create_project(name: str):
        path = os.path.join(Config.BASE_DIR, name)
        os.makedirs(path, exist_ok=True)
        return path

    @staticmethod
    def write_file(base_path, filename, content):
        full_path = os.path.join(base_path, filename)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w") as f:
            f.write(content)

        return full_path

    @staticmethod
    def read_file(path):
        with open(path, "r") as f:
            return f.read()
