#!/usr/bin/python3
"""__init__.py
Create a unique FileStorage
instance for the application"""

import json
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
