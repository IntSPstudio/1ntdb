-- |==============================================================|
--
-- Run this script with a privileged user (e.g. root or admin).
-- Script include basic settings and tips. 
-- Example: how to create users / privileges.
-- PS. No DELETE: the application should use status_id for soft delete.
--
-- You can replace 'localhost' with an IP address or with '%' symbol. 
-- IP address can be like 192.168.0.%. Be careful with the % symbol though!
--
-- |==============================================================|

-- CREATE USER:
-- (Replace CHANGE_ME_SUPER_STRONG_PASSWORD with a secure password!)
CREATE USER IF NOT EXISTS '1ntdb_app'@'localhost'
    IDENTIFIED BY 'CHANGE_ME_SUPER_STRONG_PASSWORD1';
CREATE USER IF NOT EXISTS '1ntdb_readonly'@'localhost'
    IDENTIFIED BY 'CHANGE_ME_SUPER_STRONG_PASSWORD2';

-- OPTIONAL: (Recommended for remote access. Require SSL)
ALTER USER '1ntdb_app'@'localhost' REQUIRE SSL;
ALTER USER '1ntdb_readonly'@'localhost' REQUIRE SSL;

-- APP USERS RULES
GRANT SELECT, INSERT, UPDATE ON `system`.* TO '1ntdb_app'@'localhost';
GRANT SELECT, INSERT, UPDATE ON `main`.* TO '1ntdb_app'@'localhost';
GRANT SELECT, INSERT, UPDATE ON `products`.* TO '1ntdb_app'@'localhost';
GRANT SELECT, INSERT, UPDATE ON `fleet`.* TO '1ntdb_app'@'localhost';
GRANT SELECT, INSERT, UPDATE ON `work`.* TO '1ntdb_app'@'localhost';
GRANT SELECT, INSERT, UPDATE ON `finance`.* TO '1ntdb_app'@'localhost';
GRANT SELECT, INSERT, UPDATE ON `miscellaneous`.* TO '1ntdb_app'@'localhost';
GRANT SELECT, INSERT, UPDATE ON `observations`.* TO '1ntdb_app'@'localhost';

-- READ ONLY USERS RULES
GRANT SELECT ON `system`.* TO '1ntdb_readonly'@'localhost';
GRANT SELECT ON `main`.* TO '1ntdb_readonly'@'localhost';
GRANT SELECT ON `products`.* TO '1ntdb_readonly'@'localhost';
GRANT SELECT ON `fleet`.* TO '1ntdb_readonly'@'localhost';
GRANT SELECT ON `work`.* TO '1ntdb_readonly'@'localhost';
GRANT SELECT ON `finance`.* TO '1ntdb_readonly'@'localhost';
GRANT SELECT ON `miscellaneous`.* TO '1ntdb_readonly'@'localhost';
GRANT SELECT ON `observations`.* TO '1ntdb_readonly'@'localhost';

-- Not usually required anymore, but safe to run (old habits):
-- FLUSH PRIVILEGES;