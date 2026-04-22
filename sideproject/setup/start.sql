-- |==============================================================|
--
-- HELLO!
--
-- Run this script with a privileged user (e.g. root or admin). This script help to create this side project.
-- Script include basic settings and tips. Example: how to create database and users / privileges.
--
-- Replace the username with own. You can replace 'localhost' with an IP address or with '%' symbol. 
-- IP address can be like 192.168.0.%. Be careful with the % symbol though!
--
-- |==============================================================|

-- CREATE DATABASE
CREATE DATABASE IF NOT EXISTS products;

-- EXECUTE TABLE CREATION SCRIPT: (This is the file next to. This is where we create the tables in that database.)
--                                (Always check what code is in these files when importing. Just in case.)
-- mariadb -u root -p < products.sql

-- CREATE USER:
-- (Replace CHANGE_ME_SUPER_STRONG_PASSWORD with a secure password!)
CREATE USER 'username'@'localhost' IDENTIFIED BY 'CHANGE_ME_SUPER_STRONG_PASSWORD';

-- PRIVILEGES (Access to only product database tables with select, insert, update):
GRANT SELECT, INSERT, UPDATE ON products.* TO 'username'@'localhost';

-- OR FOR ALL PRIVILEGES TO ALL DATABASES AND TABLES (This is not the best option):
-- GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';

-- AND IF YOU WANT REMOVE PRIVILEGES:
-- REVOKE ALL PRIVILEGES ON products.* FROM 'username'@'localhost';

-- OPTIONAL: (Recommended for remote access. Require SSL)
ALTER USER 'username'@'localhost' REQUIRE SSL;

-- Not usually required anymore, but safe to run (old habits):
-- FLUSH PRIVILEGES;

-- IF YOU WANT TO CHECK:
-- SHOW GRANTS FOR 'username'@'localhost';

-- SETUP COMPLETE!
-- Now if you want to login with new user:
-- (this will then ask the password after enter because there is a -p)
-- option 1: mariadb -u username -p 
-- option 2: mysql -u username -p