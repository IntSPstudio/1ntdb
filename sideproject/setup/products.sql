--|==============================================================|
-- 
-- This is for product database basics
-- Allows you to create products and link them to different product gtins
-- UPC, EAN, ISBN etc
-- Also allows price history
--
--|==============================================================|

USE products;
SET default_storage_engine=InnoDB;

--|==============================================================|
-- BRANDS

CREATE TABLE brands (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(150) NOT NULL UNIQUE,
    info VARCHAR(255)
);
CREATE INDEX idx_brand_name ON brands(name);

--|==============================================================|
-- CATEGORIES

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,

    status INT DEFAULT 1,

    code VARCHAR(10) UNIQUE,
    name VARCHAR(150),

    parent_id INT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (parent_id)
        REFERENCES categories(id)
        ON DELETE SET NULL
);
CREATE INDEX idx_category_name ON categories(name);
CREATE INDEX idx_category_code ON categories(code);

--|==============================================================|
-- UNITS

CREATE TABLE units (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    symbol VARCHAR(10)
);

--|==============================================================|
-- PRODUCTS

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,

    status INT DEFAULT 1,

    name VARCHAR(255) NOT NULL,

    brand_id INT,
    category_id INT,

    qty_value DECIMAL(10,3),
    unit_id INT,

    manufacturer VARCHAR(255),
    made_in VARCHAR(60),

    info TEXT,
    note TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    FOREIGN KEY (brand_id)
        REFERENCES brands(id)
        ON DELETE SET NULL,

    FOREIGN KEY (category_id)
        REFERENCES categories(id)
        ON DELETE SET NULL,

    FOREIGN KEY (unit_id)
        REFERENCES units(id)
        ON DELETE SET NULL
);
CREATE INDEX idx_product_name ON products(name);
CREATE INDEX idx_product_category ON products(category_id);
CREATE INDEX idx_product_brand ON products(brand_id);

--|==============================================================|
-- PRODUCT IDENTIFIERS (Example: GTIN)

CREATE TABLE product_identifiers (
    id INT AUTO_INCREMENT PRIMARY KEY,

    status INT DEFAULT 1,

    product_id INT NOT NULL,

    identifier VARCHAR(50) NOT NULL,
    type VARCHAR(20),

    info TEXT,

    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON DELETE CASCADE,

    UNIQUE (identifier, type)
);
CREATE INDEX idx_identifier_product ON product_identifiers(product_id);

--|==============================================================|
-- PRODUCT PRICE HISTORY

CREATE TABLE product_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,

    status INT DEFAULT 1,

    product_id INT NOT NULL,
    location_id INT,

    price DECIMAL(10,2),
    currency VARCHAR(10),
    --vat DECIMAL(5,2),

    price_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON DELETE CASCADE
);
CREATE INDEX idx_price_product ON product_prices(product_id);
CREATE INDEX idx_price_location ON product_prices(location_id);
CREATE INDEX idx_price_date ON product_prices(price_date);

--|==============================================================|
-- SAMPLE DATA

INSERT INTO units (name, symbol) VALUES
('gram','g'),
('kilogram','kg'),
('milliliter','ml'),
('desiliter','dl'),
('liter','l'),
('piece','pcs'),
('meter','m'),
('centimeter','cm'),
('millimeter','mm');