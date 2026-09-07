import sqlite3
import json
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "diagram_generator.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Create projects table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS projects (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Create diagrams table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS diagrams (
            id TEXT PRIMARY KEY,
            project_id TEXT NOT NULL,
            topology_json TEXT NOT NULL,
            version INTEGER NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (project_id) REFERENCES projects (id)
        )
    """)
    
    # Create custom_icons table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS custom_icons (
            id TEXT PRIMARY KEY,
            tag TEXT NOT NULL UNIQUE,
            description TEXT NOT NULL,
            filename TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Phase 3 frontend/architecture metadata migrations for existing databases
    def ensure_column(table, column, definition):
        cursor.execute(f"PRAGMA table_info({table})")
        existing = {row[1] for row in cursor.fetchall()}
        if column not in existing:
            cursor.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")

    ensure_column("diagrams", "title", "TEXT")
    ensure_column("diagrams", "architecture_view", "TEXT DEFAULT 'logical'")
    ensure_column("diagrams", "lint_score", "INTEGER")
    ensure_column("diagrams", "lint_grade", "TEXT")
    ensure_column("diagrams", "metadata_json", "TEXT")
    ensure_column("custom_icons", "provider", "TEXT DEFAULT 'organization'")
    ensure_column("custom_icons", "category", "TEXT DEFAULT 'application'")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS diagram_quality (
            id TEXT PRIMARY KEY,
            diagram_id TEXT NOT NULL,
            score INTEGER,
            grade TEXT,
            findings_json TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (diagram_id) REFERENCES diagrams (id)
        )
    """)
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_diagrams_project_updated ON diagrams(project_id, updated_at DESC)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_quality_diagram ON diagram_quality(diagram_id, created_at DESC)")
    conn.commit()
    conn.close()

# Project Helpers
def create_project(project_id: str, name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO projects (id, name) VALUES (?, ?)",
        (project_id, name)
    )
    conn.commit()
    conn.close()

def get_projects():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM projects ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# Diagram Helpers
def save_diagram(diagram_id: str, project_id: str, topology_json: str, version: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    # Check if exists
    cursor.execute("SELECT id FROM diagrams WHERE id = ?", (diagram_id,))
    exists = cursor.fetchone()
    if exists:
        cursor.execute(
            "UPDATE diagrams SET topology_json = ?, version = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            (topology_json, version, diagram_id)
        )
    else:
        cursor.execute(
            "INSERT INTO diagrams (id, project_id, topology_json, version) VALUES (?, ?, ?, ?)",
            (diagram_id, project_id, topology_json, version)
        )
    conn.commit()
    conn.close()

def get_diagram(diagram_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diagrams WHERE id = ?", (diagram_id,))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_project_diagrams(project_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diagrams WHERE project_id = ? ORDER BY updated_at DESC", (project_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

# Custom Icon Helpers
def save_custom_icon(icon_id: str, tag: str, description: str, filename: str, provider: str = "organization", category: str = "application"):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT OR REPLACE INTO custom_icons (id, tag, description, filename, provider, category) VALUES (?, ?, ?, ?, ?, ?)",
        (icon_id, tag, description, filename, provider, category)
    )
    conn.commit()
    conn.close()

def get_custom_icons():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM custom_icons ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def delete_custom_icon(icon_id: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT filename FROM custom_icons WHERE id = ?", (icon_id,))
    row = cursor.fetchone()
    if row:
        filename = row["filename"]
        cursor.execute("DELETE FROM custom_icons WHERE id = ?", (icon_id,))
        conn.commit()
        conn.close()
        return filename
    conn.close()
    return None
