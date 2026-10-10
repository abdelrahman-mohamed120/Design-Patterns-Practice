CREATE DATABASE IF NOT EXISTS DesignPatternsPractice;

USE DesignPatternsPractice;

CREATE TABLE transactions (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    transaction_uuid VARCHAR(36) UNIQUE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    gateway_name VARCHAR(50) NOT NULL, -- 'Stripe', 'PayPal', 'Paymob'
    status VARCHAR(20) NOT NULL, -- 'success', 'failed', 'pending'
    gateway_transaction_id VARCHAR(255), -- Reference ID provided by vendor
    gateway_raw_response JSON, -- Flexible store for complete vendor payload
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);