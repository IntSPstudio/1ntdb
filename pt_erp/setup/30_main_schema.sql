-- |==============================================================|
--
-- Run this script with a privileged user (e.g. root or admin).
-- Script include main database tables
--
-- |==============================================================|

USE `main`;
SET default_storage_engine=InnoDB;

CREATE TABLE IF NOT EXISTS location_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

INSERT INTO location_types (name) VALUES
('private'),
('company'),
('cov'),
('attractions'),
('gps_points'),
('internal')
ON DUPLICATE KEY UPDATE name = VALUES(name);

CREATE TABLE IF NOT EXISTS location_groups (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

INSERT INTO location_groups (name) VALUES
('family'),
('friends'),
('restaurants'),
('lidl-group'),
('k-group'),
('s-group'),
('main'),
('other')
ON DUPLICATE KEY UPDATE name = VALUES(name);

CREATE TABLE IF NOT EXISTS locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    name VARCHAR(255) NOT NULL,
    type_id INT,
    group_id INT,
    address1 VARCHAR(255),
    address2 VARCHAR(255),
    city VARCHAR(100),
    postcode VARCHAR(20),
    country VARCHAR(50),
    country_code CHAR(4),
    lat DECIMAL(10,8),
    lon DECIMAL(11,8),
    info TEXT,
    extra_data JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_location_type FOREIGN KEY (type_id) REFERENCES location_types(id),
    CONSTRAINT fk_location_group FOREIGN KEY (group_id) REFERENCES location_groups(id)
);

CREATE INDEX IF NOT EXISTS idx_location_city ON locations(city);
CREATE INDEX IF NOT EXISTS idx_location_group ON locations(group_id);
CREATE INDEX IF NOT EXISTS idx_location_coordinates ON locations(lat, lon);

CREATE TABLE IF NOT EXISTS documents (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    title VARCHAR(255) NOT NULL,
    document_type VARCHAR(100),
    file_path VARCHAR(1000),
    source_ref VARCHAR(30),
    info TEXT,
    note TEXT,
    extra_data JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_documents_source_ref ON documents(source_ref);

CREATE TABLE IF NOT EXISTS document_links (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    document_ref VARCHAR(30) NOT NULL,
    target_ref VARCHAR(30) NOT NULL,
    link_type VARCHAR(50),
    info VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_document_links_document_ref ON document_links(document_ref);
CREATE INDEX IF NOT EXISTS idx_document_links_target_ref ON document_links(target_ref);