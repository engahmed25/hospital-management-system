# Hospital Management System

A comprehensive web-based Hospital Management System built with Django 5.1. This system provides a complete solution for managing hospital operations including patient registration, doctor profiles, clinic management, appointment booking, and staff administration.

## 🏥 Features

### 👤 User Management (Account App)
- **Custom User Registration & Authentication**
  - Extended user model with phone number and address fields
  - Secure login/logout functionality  
  - User profile management
  - Automatic profile creation for new users

### 👩‍⚕️ Doctor Management
- **Doctor Profiles**
  - Complete doctor information (name, specialization, bio)
  - Photo upload functionality
  - Doctor listing with detailed view pages
  - Integration with clinic assignments

### 🏥 Clinic Management
- **Clinic Information System**
  - Clinic details with descriptions and feature images
  - Working hours management (9 AM - 7 PM slots)
  - Many-to-many relationship with doctors
  - Clinic listing and detailed view pages

### 📅 Reservation System
- **Smart Appointment Booking**
  - User-specific reservation management
  - Date and time slot selection
  - Dynamic doctor selection based on clinic choice
  - 20-minute interval time slots with "Noon" option
  - AJAX-powered dynamic forms
  - Reservation cancellation functionality
  - View and manage personal appointments

### 🏢 Staff Management
- **Administrative Dashboard**
  - Staff-only access control
  - CRUD operations for clinics and doctors
  - Comprehensive dashboard with data visualization
  - Image upload management for clinics and doctors

### 🔍 Search & Navigation
- **Unified Search System**
  - Search across doctors and clinics
  - Responsive Bootstrap-based UI
  - Intuitive navigation with FontAwesome icons
  - Mobile-friendly design

## 🛠 Tech Stack

- **Backend**: Django 5.1
- **Database**: MySQL 
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Authentication**: Django's built-in authentication system with custom user model
- **Media Handling**: Local file storage with organized upload directories
- **Icons**: FontAwesome
- **AJAX**: Vanilla JavaScript for dynamic form interactions

## 📋 Prerequisites

- Python 3.8+
- MySQL 5.7+ or MySQL 8.0+
- pip (Python package installer)
- Virtual environment (recommended)

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/engahmed25/hospital-management-system.git
cd hospital-management-system/hospital_project
```

### 2. Create and Activate Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install django==5.1
pip install mysqlclient  # or PyMySQL
pip install Pillow      # for image handling
```

### 4. Database Configuration

#### MySQL Setup:
1. Install MySQL server
2. Create a database named `mydb`
3. Update `hospital_project/settings.py` with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files (if needed)
```bash
python manage.py collectstatic
```

### 8. Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## 📁 Project Structure

```
hospital_project/
├── account/                 # User management & authentication
│   ├── models.py           # CustomUser, Profile models
│   ├── views.py            # Registration, login, profile views
│   ├── forms.py            # Registration, login, search forms
│   └── templates/account/   # Account-related templates
├── clinic/                  # Clinic management
│   ├── models.py           # Clinic model with working hours
│   ├── views.py            # Clinic listing and detail views
│   └── templates/clinic/    # Clinic templates
├── doctor/                  # Doctor management
│   ├── models.py           # Doctor model with photos
│   ├── views.py            # Doctor listing and detail views
│   └── templates/doctor/    # Doctor templates
├── reservation/             # Appointment booking system
│   ├── models.py           # Reservation model
│   ├── views.py            # Booking, listing, cancellation views
│   ├── forms.py            # Reservation forms
│   └── templates/reservation/ # Reservation templates
├── staff/                   # Staff administration
│   ├── views.py            # CRUD operations for clinics/doctors
│   ├── forms.py            # Admin forms
│   └── templates/staff/     # Staff dashboard templates
├── templates/               # Base templates
│   ├── base.html           # Main template with navigation
│   └── home.html           # Homepage
├── static/                  # Static files (CSS, JS, images)
├── media/                   # User uploads
│   ├── clinic_images/      # Clinic feature images
│   └── doctor_photos/      # Doctor profile photos
└── hospital_project/        # Django project settings
    ├── settings.py         # Configuration
    ├── urls.py            # URL routing
    └── wsgi.py            # WSGI application
```

## 🌐 URL Routes

| URL Pattern | Description | Access Level |
|-------------|-------------|-------------|
| `/` | Homepage with featured clinics/doctors | Public |
| `/account/register/` | User registration | Public |
| `/account/login/` | User login | Public |
| `/account/profile/` | User profile management | Authenticated |
| `/account/search/` | Unified search | Public |
| `/doctors/` | Doctor listing | Public |
| `/doctors/<id>/` | Doctor detail | Public |
| `/clinics/` | Clinic listing | Public |
| `/clinics/<id>/` | Clinic detail | Public |
| `/reservations/` | User's reservations | Authenticated |
| `/reservations/create/` | Create new reservation | Authenticated |
| `/reservations/<id>/` | Reservation detail | Authenticated |
| `/reservations/<id>/cancel/` | Cancel reservation | Authenticated |
| `/staff/` | Staff dashboard | Staff Only |
| `/admin/` | Django admin panel | Admin Only |

## 💡 Usage Guide

### For Patients:
1. **Register/Login** to access booking features
2. **Browse Clinics** and **Doctors** to find suitable healthcare providers
3. **Create Reservations** by selecting clinic, doctor, date, and time slot
4. **Manage Appointments** - view, cancel, or modify existing reservations
5. **Use Search** to quickly find specific doctors or clinics

### For Staff:
1. **Access Staff Dashboard** (requires staff privileges)
2. **Manage Clinics** - add, edit, or delete clinic information
3. **Manage Doctors** - add, edit, or delete doctor profiles
4. **Upload Images** for clinics and doctors
5. **Assign Doctors** to clinics through the many-to-many relationship

### For Administrators:
1. **Django Admin Panel** for complete system management
2. **User Management** - create staff accounts, manage permissions
3. **Data Management** - bulk operations, advanced filtering
4. **System Monitoring** - view all reservations, user activities

## 🔧 Advanced Features

### Dynamic Form Interactions
- **AJAX-powered reservation form** that dynamically loads doctors based on selected clinic
- **Time slot generation** based on clinic working hours
- **Real-time form validation** with Bootstrap styling

### Image Management
- **Automated file organization** with separate directories for different image types
- **Image resizing and optimization** (can be extended)
- **Safe file upload** with proper validation

### Security Features
- **CSRF protection** on all forms
- **User authentication** required for sensitive operations
- **Staff-only access** for administrative functions
- **SQL injection prevention** through Django ORM



## 📝 Development Notes

- **Database**: Configured for MySQL but can be easily switched to PostgreSQL or SQLite
- **Media Files**: Currently stored locally; can be configured for cloud storage
- **Environment Variables**: Consider using django-environ for production settings
- **Caching**: Can be implemented for better performance with high traffic



## 📄 License

This project is developed as a graduation project for database course studies.

---

**Built with ❤️ using Django 5.1**