-- |==============================================================|
--
-- Run this script with a privileged user (e.g. root or admin).
-- Script include other database tables
--
-- |==============================================================|

USE `miscellaneous`;
SET default_storage_engine=InnoDB;

CREATE TABLE IF NOT EXISTS notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    note_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR(255),
    body TEXT NOT NULL,
    display_context VARCHAR(100),
    priority INT DEFAULT 0,
    pinned BOOLEAN DEFAULT FALSE,
    visible_from DATETIME,
    visible_until DATETIME,
    source VARCHAR(50),
    tags JSON,
    extra_data JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_notes_note_at ON notes(note_at);
CREATE INDEX IF NOT EXISTS idx_notes_display_context ON notes(display_context);
CREATE INDEX IF NOT EXISTS idx_notes_pinned ON notes(pinned);

CREATE TABLE IF NOT EXISTS task_lists (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    name VARCHAR(150) NOT NULL,
    display_context VARCHAR(100),
    sort_order INT DEFAULT 0,
    info TEXT,
    note TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_task_lists_display_context ON task_lists(display_context);

CREATE TABLE IF NOT EXISTS task_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    task_list_id INT,
    title VARCHAR(255) NOT NULL,
    body TEXT,
    due_at DATETIME,
    completed_at DATETIME,
    sort_order INT DEFAULT 0,
    priority INT DEFAULT 0,
    assigned_name VARCHAR(150),
    display_context VARCHAR(100),
    tags JSON,
    extra_data JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (task_list_id) REFERENCES task_lists(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_task_items_list ON task_items(task_list_id);
CREATE INDEX IF NOT EXISTS idx_task_items_due_at ON task_items(due_at);
CREATE INDEX IF NOT EXISTS idx_task_items_completed_at ON task_items(completed_at);
CREATE INDEX IF NOT EXISTS idx_task_items_display_context ON task_items(display_context);