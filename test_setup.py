#!/usr/bin/env python
import os
import sys
from shared.config import config
from backend.db.sqlalchemy_manager import init_db, engine, Base
from sqlalchemy import text

# Explicitly debug print the connection URL
print("DEBUG DATABASE URL:", config.get_config('DATABASE_URL'))

def test_database_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("✅ Database connection successful!")
        return True
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return False

def setup_database():
    db_exists = test_database_connection()
    if not db_exists:
        print("🔨 Attempting to create database tables...")
        init_db()
    else:
        print("✅ Database is already set up and running.")

def check_files_exist(file_paths):
    missing_files = []
    for file in file_paths:
        if not os.path.exists(file):
            missing_files.append(file)
    if missing_files:
        print("❌ Missing files detected:")
        for file in missing_files:
            print(f" - {file}")
        return False
    print("✅ All files are present.")
    return True

if __name__ == "__main__":
    required_files = [
        "shared/event_bus.py",
        "shared/event_bus.js",
        "shared/websocket_manager.py",
        "shared/websocket_manager.js",
        "shared/config.py",
        "shared/config.js",
        "shared/constants.py",
        "shared/constants.js",
        "shared/utils.py",
        "shared/utils.js",
        "shared/error_utils.js",
        "shared/errors.py",
        "backend/db/sqlalchemy_manager.py",
        "backend/models/graph.py",
        "backend/models/node.py",
        "backend/models/edge.py",
        "backend/models/conversation.py",
        "backend/models/message.py",
        "backend/models/context.py",
        "backend/models/execution.py",
        "backend/models/execution_result.py",
        "requirements.txt",
    ]

    print("🚀 Starting AI Canvas Phase 1 setup test...\n")

    files_check = check_files_exist(required_files)
    if not files_check:
        sys.exit(1)

    setup_database()

    print("\n🎉 AI Canvas Phase 1 setup validation complete!")
