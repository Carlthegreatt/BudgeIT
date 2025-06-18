CREATE DATABASE IF NOT EXISTS BudgetManager;
USE BudgetManager;

-- 2. Create tables
CREATE TABLE IF NOT EXISTS budget_settings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    monthly_budget DECIMAL(10,2) NOT NULL DEFAULT 0.00
);

CREATE TABLE IF NOT EXISTS transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    amount DECIMAL(10,2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    date DATE NOT NULL
);

-- @block
SELECT * FROM transactions

-- @block
SELECT * FROM budget_settings

