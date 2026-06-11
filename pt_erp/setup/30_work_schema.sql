-- |==============================================================|
--
-- Run this script with a privileged user (e.g. root or admin).
-- Script include work related tables
--
-- |==============================================================|

USE `work`;
SET default_storage_engine=InnoDB;

CREATE TABLE IF NOT EXISTS journal_entries (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    entry_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    title VARCHAR(255),
    body TEXT NOT NULL,
    project_ref VARCHAR(30),
    target_ref VARCHAR(30),
    source VARCHAR(50),
    tags JSON,
    extra_data JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_journal_entries_entry_at ON journal_entries(entry_at);
CREATE INDEX IF NOT EXISTS idx_journal_entries_project_ref ON journal_entries(project_ref);
CREATE INDEX IF NOT EXISTS idx_journal_entries_target_ref ON journal_entries(target_ref);