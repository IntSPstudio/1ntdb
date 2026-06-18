-- |==============================================================|
--
-- Run this script with a privileged user (e.g. root or admin).
-- Script include product database tables
--
-- |==============================================================|

USE `products`;
SET default_storage_engine=InnoDB;

CREATE TABLE IF NOT EXISTS organizations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    sys_name VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(150) NOT NULL,
    info VARCHAR(255),
    org_type VARCHAR(50),
    location_ref VARCHAR(30),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_organizations_name ON organizations(name);
CREATE INDEX IF NOT EXISTS idx_organizations_location_ref ON organizations(location_ref);

CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    sys_name VARCHAR(50) UNIQUE,
    name VARCHAR(150),
    info VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_category_name ON categories(name);
CREATE INDEX IF NOT EXISTS idx_category_code ON categories(sys_name);

CREATE TABLE IF NOT EXISTS route_categories (
    product_id INT,
    category_id INT,
    status_id INT DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
)

CREATE TABLE IF NOT EXISTS units (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    name VARCHAR(20) NOT NULL,
    symbol VARCHAR(10),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    sys_name VARCHAR(255) UNIQUE NOT NULL, 
    name VARCHAR(255) NOT NULL,
    brand_id INT,
    qty_value DECIMAL(10,3),
    unit_id INT,
    default_manufacturer_brand_id INT,
    default_budget_ref VARCHAR(30),
    info VARCHAR(255),
    note VARCHAR(255),
    extra_data JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (brand_id) REFERENCES organizations(id) ON DELETE SET NULL,
    FOREIGN KEY (default_manufacturer_brand_id) REFERENCES organizations(id) ON DELETE SET NULL,
    FOREIGN KEY (unit_id) REFERENCES units(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_product_name ON products(name);
CREATE INDEX IF NOT EXISTS idx_product_brand ON products(brand_id);
CREATE INDEX IF NOT EXISTS idx_product_default_manufacturer ON products(default_manufacturer_brand_id);
CREATE INDEX IF NOT EXISTS idx_product_default_budget_ref ON products(default_budget_ref);

CREATE TABLE IF NOT EXISTS identifier_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    value VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(255),
    regex_pattern VARCHAR(255),
    priority INT DEFAULT 0,
    info VARCHAR(255),
    status_id INT DEFAULT 1,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS product_identifiers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    product_id INT,
    value VARCHAR(50) NOT NULL,
    type_id INT,
    info VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY(type_id) REFERENCES identifier_types(id),
    FOREIGN KEY(product_id) REFERENCES products(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_identifier_product ON product_identifiers(product_id);
CREATE INDEX IF NOT EXISTS idx_identifier_value ON product_identifiers(value);

CREATE TABLE IF NOT EXISTS product_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    product_id INT NOT NULL,
    location_ref VARCHAR(30),
    price DECIMAL(10,2) NOT NULL,
    currency VARCHAR(10) DEFAULT 'EUR',
    quantity_value DECIMAL(12,3),
    unit_id INT,
    price_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    source_type VARCHAR(30),
    source_ref VARCHAR(30),
    document_ref VARCHAR(30),
    finance_ref VARCHAR(30),
    order_ref VARCHAR(30),
    info VARCHAR(255),
    note VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (unit_id) REFERENCES units(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_price_product ON product_prices(product_id);
CREATE INDEX IF NOT EXISTS idx_price_location_ref ON product_prices(location_ref);
CREATE INDEX IF NOT EXISTS idx_price_date ON product_prices(price_date);

CREATE TABLE IF NOT EXISTS stock_locations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    name VARCHAR(150) NOT NULL,
    parent_ref VARCHAR(30),
    location_ref VARCHAR(30),
    info VARCHAR(255),
    note VARCHAR(255),
    extra_data JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_stock_locations_name ON stock_locations(name);
CREATE INDEX IF NOT EXISTS idx_stock_locations_parent_ref ON stock_locations(parent_ref);

CREATE TABLE IF NOT EXISTS stock_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    product_id INT NOT NULL,
    stock_location_id INT,
    manufacturer_brand_id INT,
    current_quantity DECIMAL(12,3),
    quantity_unit_id INT,
    measured_weight DECIMAL(12,3),
    weight_unit_id INT,
    condition_name VARCHAR(100),
    info VARCHAR(255),
    note VARCHAR(255),
    extra_data JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (stock_location_id) REFERENCES stock_locations(id) ON DELETE SET NULL,
    FOREIGN KEY (manufacturer_brand_id) REFERENCES organizations(id) ON DELETE SET NULL,
    FOREIGN KEY (quantity_unit_id) REFERENCES units(id) ON DELETE SET NULL,
    FOREIGN KEY (weight_unit_id) REFERENCES units(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_stock_items_product ON stock_items(product_id);
CREATE INDEX IF NOT EXISTS idx_stock_items_location ON stock_items(stock_location_id);
CREATE INDEX IF NOT EXISTS idx_stock_items_manufacturer ON stock_items(manufacturer_brand_id);

CREATE TABLE IF NOT EXISTS stock_quantity_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    stock_item_id INT NOT NULL,
    quantity DECIMAL(12,3) NOT NULL,
    unit_id INT,
    quantity_event_type VARCHAR(50) DEFAULT 'measurement',
    measured_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    source VARCHAR(50),
    note VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (stock_item_id) REFERENCES stock_items(id) ON DELETE CASCADE,
    FOREIGN KEY (unit_id) REFERENCES units(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_stock_quantity_log_item ON stock_quantity_log(stock_item_id);
CREATE INDEX IF NOT EXISTS idx_stock_quantity_log_measured_at ON stock_quantity_log(measured_at);

CREATE TABLE IF NOT EXISTS stock_weight_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    stock_item_id INT NOT NULL,
    measured_weight DECIMAL(12,3) NOT NULL,
    weight_unit_id INT,
    measured_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    source VARCHAR(50),
    note VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (stock_item_id) REFERENCES stock_items(id) ON DELETE CASCADE,
    FOREIGN KEY (weight_unit_id) REFERENCES units(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_stock_weight_log_item ON stock_weight_log(stock_item_id);
CREATE INDEX IF NOT EXISTS idx_stock_weight_log_measured_at ON stock_weight_log(measured_at);

CREATE TABLE IF NOT EXISTS stock_movements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    product_id INT NOT NULL,
    stock_item_id INT,
    movement_type VARCHAR(30) NOT NULL,
    quantity DECIMAL(12,3) NOT NULL,
    unit_id INT,
    from_location_id INT,
    to_location_id INT,
    project_ref VARCHAR(30),
    budget_ref VARCHAR(30),
    source_ref VARCHAR(30),
    document_ref VARCHAR(30),
    finance_ref VARCHAR(30),
    reason VARCHAR(255),
    note VARCHAR(255),
    happened_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY (stock_item_id) REFERENCES stock_items(id) ON DELETE SET NULL,
    FOREIGN KEY (unit_id) REFERENCES units(id) ON DELETE SET NULL,
    FOREIGN KEY (from_location_id) REFERENCES stock_locations(id) ON DELETE SET NULL,
    FOREIGN KEY (to_location_id) REFERENCES stock_locations(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_stock_movements_product ON stock_movements(product_id);
CREATE INDEX IF NOT EXISTS idx_stock_movements_item ON stock_movements(stock_item_id);
CREATE INDEX IF NOT EXISTS idx_stock_movements_happened ON stock_movements(happened_at);
CREATE INDEX IF NOT EXISTS idx_stock_movements_project_ref ON stock_movements(project_ref);
CREATE INDEX IF NOT EXISTS idx_stock_movements_budget_ref ON stock_movements(budget_ref);

INSERT INTO units (name, symbol) VALUES
('gram', 'g'),
('kilogram', 'kg'),
('milliliter', 'ml'),
('desiliter', 'dl'),
('liter', 'l'),
('piece', 'pcs'),
('meter', 'm'),
('centimeter', 'cm'),
('millimeter', 'mm')
ON DUPLICATE KEY UPDATE
    symbol = VALUES(symbol);