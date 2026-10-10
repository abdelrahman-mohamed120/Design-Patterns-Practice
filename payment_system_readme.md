# Payment System (Strategy Design Pattern Case Study)

This repository demonstrates a practical implementation of the **Strategy Design Pattern** in Python, modeled after a real-world backend architectural case study for a multi-gateway payment processing engine.

---

## 📌 Case Study Context: E-Commerce Payment Gateway

### Problem Statement

In modern backend systems (e.g., Uber pricing engine, e-commerce checkout systems), business requirements frequently evolve to support multiple algorithms or operational modes.

Without a flexible design, handling multiple payment providers like **Stripe**, **PayPal**, or **Paymob** using traditional `if/else` or `switch` statements leads to:

- **Spaghetti Code:** Hard-to-maintain, tightly coupled logic in the checkout flow.
- **Violation of the Open/Closed Principle (SOLID):** Modifying or adding a new payment gateway forces changes to core business logic, risking regression bugs.
- **Tight Coupling:** The core application becomes dependent on specific vendor integrations.

---

## 🛠️ The Solution: Strategy Pattern

The **Strategy Pattern** is a behavioral design pattern that defines a family of algorithms, encapsulates each one into a separate class, and makes them interchangeable at runtime via a common interface.

### Benefits in This System

1. **Open/Closed Principle:** New payment providers (e.g., Paymob, Apple Pay) can be added simply by creating a new strategy class without modifying the existing `Checkout` class.
2. **Interchangeability at Runtime:** The payment method can be selected or dynamically swapped depending on user choice or regional settings.
3. **Separation of Concerns:** Each gateway handles its own API parameters, authorization logic, and response formats independently.

---

## 🏗️ System Architecture & Class Structure

The codebase is organized into clear components following the Strategy Pattern structure:

```
payment_system/
│
├── strategies/
│   ├── __init__.py
│   ├── payment_strategy.py   # Abstract Strategy (Interface)
│   ├── stripe_payment.py     # Concrete Strategy 1
│   └── paypal_payment.py     # Concrete Strategy 2
│
├── checkout.py               # Context Class
└── main.py                   # Client Execution
```

### 1. Abstract Strategy (`PaymentStrategy`)

Defines the contract/interface that all concrete strategies must implement (`pay(amount)`).

### 2. Concrete Strategies (`StripePayment`, `PaypalPayment`)

Implement specific payment handling logic using vendor-specific credentials (e.g., API keys, email/password credentials).

### 3. Context (`Checkout`)

Maintains a reference to a `PaymentStrategy` instance and delegates the payment execution to the current strategy without knowing its internal details.

---

## 💾 Database Schema Design (`transactions` Table)

To handle different response payloads from various payment gateways (Stripe returns token IDs, PayPal returns Payer IDs/transaction hashes, etc.), the `transactions` table is designed using a **hybrid approach** (structured metadata + JSON column for polymorphic vendor payloads).

### SQL Schema (`transactions`)

```sql
CREATE TABLE transactions (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    transaction_uuid VARCHAR(36) UNIQUE NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'USD',
    gateway_name VARCHAR(50) NOT NULL, -- 'Stripe', 'PayPal', 'Paymob'
    status VARCHAR(20) NOT NULL,       -- 'success', 'failed', 'pending'
    gateway_transaction_id VARCHAR(255), -- Reference ID provided by vendor
    gateway_raw_response JSON,          -- Flexible store for complete vendor payload
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
```

### Key DB Design Decisions:

- **`gateway_name`**: Allows filtering and querying analytics per provider.
- **`gateway_transaction_id`**: Stores the unique transaction reference provided by external APIs for reconciliation and webhooks.
- **`gateway_raw_response` (JSON)**: Safely stores vendor-specific metadata without requiring schema migrations whenever a new provider is introduced.

---

## 🚀 Running the Code

### Execute the Main Application

```bash
python payment_system/main.py
```

### Sample Output

```text
Processing payment of $150.0 through Stripe with API key: sk_live_12345
{'status': 'success', 'amount': 150.0, 'gateway': 'Stripe'}
------------------------------
Processing payment of $150.0 through PayPal with email: user@example.com
{'status': 'success', 'amount': 150.0, 'gateway': 'PayPal'}
```
