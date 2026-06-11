-- |==============================================================|
--
-- Run this script with a privileged user (e.g. root or admin).
-- Script include fleet database tables
--
-- |==============================================================|

USE `fleet`;
SET default_storage_engine=InnoDB;

CREATE TABLE IF NOT EXISTS vehicle_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    code VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(150) NOT NULL,
    info TEXT,
    note TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vehicle_brands (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    name VARCHAR(150) NOT NULL UNIQUE,
    info TEXT,
    note TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vehicle_body_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    code VARCHAR(50) NOT NULL UNIQUE,
    name VARCHAR(150) NOT NULL,
    info TEXT,
    note TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS vehicle_models (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    brand_id INT NOT NULL,
    name VARCHAR(150) NOT NULL,
    default_body_type_id INT,
    default_fuel_type VARCHAR(100),
    default_engine_type VARCHAR(100),
    default_extra_data JSON,
    info TEXT,
    note TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (brand_id) REFERENCES vehicle_brands(id),
    FOREIGN KEY (default_body_type_id) REFERENCES vehicle_body_types(id),
    UNIQUE (brand_id, name)
);

CREATE TABLE IF NOT EXISTS vin_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    vin VARCHAR(50) UNIQUE,
    brand_id INT,
    model_id INT,
    model_info VARCHAR(255),
    model_year INT,
    body_type_id INT,
    fuel_type VARCHAR(100),
    torque VARCHAR(100),
    engine_type VARCHAR(100),
    engine_induction VARCHAR(100),
    engine_kw DECIMAL(10,2),
    engine_hp DECIMAL(10,2),
    engine_displacement DECIMAL(10,3),
    engine_code VARCHAR(100),
    engine_cylinders INT,
    engine_info TEXT,
    transmission_gears INT,
    transmission_type VARCHAR(100),
    transmission_info TEXT,
    range_value VARCHAR(100),
    exterior_color VARCHAR(100),
    interior_color VARCHAR(100),
    info TEXT,
    note TEXT,
    length_value DECIMAL(10,2),
    battery_capacity DECIMAL(10,2),
    battery_type VARCHAR(100),
    charging_ac VARCHAR(100),
    charging_dc VARCHAR(100),
    motor_count INT,
    motor_combined_power DECIMAL(10,2),
    wheel_size VARCHAR(100),
    tire_size VARCHAR(100),
    extra_data JSON,
    equipment JSON,
    features JSON,
    data_source VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (brand_id) REFERENCES vehicle_brands(id),
    FOREIGN KEY (model_id) REFERENCES vehicle_models(id),
    FOREIGN KEY (body_type_id) REFERENCES vehicle_body_types(id)
);

CREATE TABLE IF NOT EXISTS vehicles (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    public_ref VARCHAR(30) UNIQUE,
    record_group VARCHAR(100),
    vehicle_type_id INT,
    owner_ref VARCHAR(30),
    owner_name VARCHAR(255),
    registration_number VARCHAR(30),
    country_code CHAR(4) DEFAULT 'FIN',
    vin_data_id INT,
    vin_ref VARCHAR(30),
    current_odometer_value INT,
    current_odometer_unit VARCHAR(10) DEFAULT 'km',
    current_odometer_at DATETIME,
    info TEXT,
    note TEXT,
    extra_data JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_type_id) REFERENCES vehicle_types(id),
    FOREIGN KEY (vin_data_id) REFERENCES vin_data(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_vehicles_registration ON vehicles(registration_number, country_code);
CREATE INDEX IF NOT EXISTS idx_vehicles_owner_ref ON vehicles(owner_ref);
CREATE INDEX IF NOT EXISTS idx_vehicles_vin_ref ON vehicles(vin_ref);
CREATE INDEX IF NOT EXISTS idx_vehicles_vin_data ON vehicles(vin_data_id);

CREATE TABLE IF NOT EXISTS odometer_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    vehicle_id INT NOT NULL,
    odometer_value INT NOT NULL,
    unit VARCHAR(10) DEFAULT 'km',
    location_ref VARCHAR(30),
    gps_lat DECIMAL(10,8),
    gps_lon DECIMAL(11,8),
    project_ref VARCHAR(30),
    reason VARCHAR(100),
    note TEXT,
    recorded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_odometer_vehicle ON odometer_log(vehicle_id);
CREATE INDEX IF NOT EXISTS idx_odometer_recorded ON odometer_log(recorded_at);
CREATE INDEX IF NOT EXISTS idx_odometer_project_ref ON odometer_log(project_ref);

CREATE TABLE IF NOT EXISTS fuel_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    vehicle_id INT NOT NULL,
    odometer_log_id INT,
    location_ref VARCHAR(30),
    product_ref VARCHAR(30),
    quantity DECIMAL(12,3),
    unit VARCHAR(10),
    total_price DECIMAL(10,2),
    currency VARCHAR(10) DEFAULT 'EUR',
    document_ref VARCHAR(30),
    finance_ref VARCHAR(30),
    project_ref VARCHAR(30),
    note TEXT,
    fueled_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE,
    FOREIGN KEY (odometer_log_id) REFERENCES odometer_log(id) ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_fuel_vehicle ON fuel_log(vehicle_id);
CREATE INDEX IF NOT EXISTS idx_fuel_fueled_at ON fuel_log(fueled_at);
CREATE INDEX IF NOT EXISTS idx_fuel_project_ref ON fuel_log(project_ref);

CREATE TABLE IF NOT EXISTS vehicle_services (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    vehicle_id INT NOT NULL,
    service_type VARCHAR(100),
    service_status VARCHAR(30),
    planned_at DATETIME,
    planned_odometer INT,
    completed_at DATETIME,
    completed_odometer INT,
    document_ref VARCHAR(30),
    finance_ref VARCHAR(30),
    project_ref VARCHAR(30),
    info TEXT,
    note TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (vehicle_id) REFERENCES vehicles(id) ON DELETE CASCADE
);

CREATE INDEX IF NOT EXISTS idx_vehicle_services_vehicle ON vehicle_services(vehicle_id);
CREATE INDEX IF NOT EXISTS idx_vehicle_services_project_ref ON vehicle_services(project_ref);