# Smart Canteen Ordering System - Backend

Django REST Framework backend for the Smart Canteen Ordering System.

## Setup Instructions

### 1. Create Virtual Environment
\`\`\`bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
\`\`\`

### 2. Install Dependencies
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 3. Run Migrations
\`\`\`bash
python manage.py migrate
\`\`\`

### 4. Seed Menu Data
\`\`\`bash
python manage.py seed_menu
\`\`\`

### 5. Create Superuser (Admin)
\`\`\`bash
python manage.py createsuperuser
\`\`\`

### 6. Run Development Server
\`\`\`bash
python manage.py runserver
\`\`\`

The API will be available at `http://localhost:8000/api/`

## API Endpoints

### Menu Items
- `GET /api/menu-items/` - List all menu items
- `GET /api/menu-items/{id}/` - Get menu item details
- `GET /api/menu-items/by_category/` - Get items grouped by category
- `GET /api/menu-items/available/` - Get available items
- `POST /api/menu-items/` - Create menu item (Admin only)
- `PUT /api/menu-items/{id}/` - Update menu item (Admin only)
- `DELETE /api/menu-items/{id}/` - Delete menu item (Admin only)

### Orders
- `GET /api/orders/` - List all orders
- `POST /api/orders/` - Create new order
- `GET /api/orders/{order_id}/` - Get order details
- `PATCH /api/orders/{order_id}/update_status/` - Update order status
- `GET /api/orders/by_table/?table_number=1` - Get orders by table
- `GET /api/orders/{order_id}/track/` - Track order status

### Payments
- `GET /api/payments/` - List all payments
- `POST /api/payments/process_payment/` - Process payment
- `GET /api/payments/by_order/?order_id=1` - Get payment by order

### Admin
- `GET /api/admin/dashboard/` - Get dashboard statistics
- `GET /api/admin/orders/` - Get all orders with filtering
- `GET /api/admin/menu-stats/` - Get menu statistics

## Database Models

### MenuItem
- name, description, category, price, image_url, is_available, rating, reviews_count

### Order
- order_id, customer_name, table_number, phone_number, email, status, payment_method, payment_status, special_instructions, subtotal, tax, delivery_charge, total_amount

### OrderItem
- order (FK), menu_item (FK), quantity, price

### Payment
- order (OneToOne), transaction_id, amount, payment_method, status

## CORS Configuration

The backend is configured to accept requests from:
- http://localhost:3000
- http://127.0.0.1:3000

Update `CORS_ALLOWED_ORIGINS` in `config/settings.py` for production.

## Authentication

Token-based authentication is available for admin endpoints. Include the token in the Authorization header:
\`\`\`
Authorization: Bearer <token>
\`\`\`

## Environment Variables

For production, set:
- `SECRET_KEY` - Django secret key
- `DEBUG` - Set to False
- `ALLOWED_HOSTS` - Comma-separated list of allowed hosts
- `DATABASE_URL` - Database connection string (if using PostgreSQL)
