-- |==============================================================|
--
-- Run this script with a privileged user (e.g. root or admin).
-- Script include system tables
--
-- |==============================================================|

USE `system`;
SET default_storage_engine=InnoDB;

CREATE TABLE IF NOT EXISTS statuses (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE,
    info VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'read',
    info VARCHAR(255),
    last_login_at DATETIME,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (status_id) REFERENCES statuses(id)
);

CREATE TABLE IF NOT EXISTS user_logins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    user_id INT NOT NULL,
    login_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    success BOOLEAN DEFAULT TRUE,
    ip_address VARCHAR(50),
    user_agent VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (status_id) REFERENCES statuses(id)
);

CREATE INDEX IF NOT EXISTS idx_user_logins_user ON user_logins(user_id);
CREATE INDEX IF NOT EXISTS idx_user_logins_time ON user_logins(login_time);

CREATE TABLE IF NOT EXISTS entity_prefixes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    prefix CHAR(4) NOT NULL UNIQUE,
    entity_name VARCHAR(100) NOT NULL,
    database_name VARCHAR(100) NOT NULL,
    table_name VARCHAR(100) NOT NULL,
    info VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (status_id) REFERENCES statuses(id),
    CHECK (prefix REGEXP '^[0-9]{4}$')
);