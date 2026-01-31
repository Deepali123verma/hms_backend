# 🏨 Hotel Management System – Backend API

This is a **Hotel Management System Backend** built using **Flask**, **Flask-RESTx**, and **PostgreSQL**.  
The system provides RESTful APIs for managing hotel operations such as rooms, bookings, billing, staff, authentication, and restaurant services.

---

## 🚀 Tech Stack

- Backend Framework: Flask (Python)
- API Documentation: Flask-RESTx (Swagger UI)
- Database: PostgreSQL
- ORM: SQLAlchemy
- Tools: pgAdmin, Postman, Swagger UI

---

## 📂 Project Structure

hotel-management-backend/
│
├── app.py  
├── config.py  
├── models.py  
├── requirements.txt  
├── .env  
│
├── routes/
│   ├── auth.py  
│   ├── rooms.py  
│   ├── booking.py  
│   ├── billing.py  
│   ├── staff.py  
│   └── restaurant.py  
│
└── migrations/

---

## 🔑 Environment Variables (.env)

DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/hotel_db  
SECRET_KEY=your_secret_key

---

## 🧩 Modules & APIs

### Authentication
- POST /api/auth/register  
- POST /api/auth/login  

### Rooms
- GET /api/rooms/  
- POST /api/rooms/  

### Booking
- GET /api/booking/  
- POST /api/booking/  

### Billing
- GET /api/billing/  
- POST /api/billing/  

### Staff
- GET /api/staff/  
- POST /api/staff/  

### Restaurant
- GET /api/restaurant/menu  
- POST /api/restaurant/menu  
- GET /api/restaurant/order  
- POST /api/restaurant/order  

---

## 🧾 Database Tables

- users  
- rooms  
- bookings  
- billing  
- staff  
- restaurant_menu  
- restaurant_orders  

(All tables are created manually using pgAdmin)

---

## ▶️ How to Run the Project

1. Clone the repository  
   git clone https://github.com/your-username/hotel-management-backend.git  

2. Create virtual environment  
   python -m venv venv  

3. Activate virtual environment  
   venv\Scripts\activate  

4. Install dependencies  
   pip install -r requirements.txt  

5. Run the server  
   python app.py  

---

## 📖 API Documentation (Swagger)

http://127.0.0.1:5000/api/



## 👩‍💻 Author

Deepali Verma  
