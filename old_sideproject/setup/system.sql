USE system;

-- |==============================================================|
-- STATUS TABLE

CREATE TABLE statuses (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    info VARCHAR(255)
);

-- |==============================================================|
-- USERS
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    status_id INT DEFAULT 1,
    username VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) DEFAULT 'read',
    info VARCHAR(255),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- |==============================================================|
-- USER LOGIN HISTORY (SECURITY / AUDIT)

CREATE TABLE user_logins (
    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    login_time DATETIME DEFAULT CURRENT_TIMESTAMP,

    success BOOLEAN DEFAULT TRUE,

    ip_address VARCHAR(50),
    user_agent VARCHAR(255),

    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE INDEX idx_user_logins_user ON user_logins(user_id);
CREATE INDEX idx_user_logins_time ON user_logins(login_time);