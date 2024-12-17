# Job Board API

A RESTful API for a job board application built with Django REST Framework. This application allows employers to post jobs and job seekers to apply for positions.

## Features

- User Authentication with JWT Tokens
- Role-based Access Control:
  - Employer: Can post, edit, and manage job listings
  - Job Seeker: Can view jobs and submit applications
- Job Management System
- Application Tracking
- Resume Upload System
- Advanced Search and Filtering

## Tech Stack

- Python 3.12
- Django 5.1
- Django REST Framework
- SQLite (Development)
- JWT Authentication
- CORS Support

## Setup

1. Clone the repository
```bash
git clone https://github.com/MikiMesfin/Job_Boardapp.git
cd Job_Boardapp
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create .env file
```bash
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

5. Run migrations
```bash
python manage.py migrate
```

6. Create superuser
```bash
python manage.py createsuperuser
```

7. Run the server
```bash
python manage.py runserver 9000
```

## API Endpoints

### Authentication
- POST `/api/token/` - Get JWT token
- POST `/api/token/refresh/` - Refresh JWT token

### Jobs
- GET `/api/jobs/` - List all jobs
- POST `/api/jobs/` - Create new job (Employer only)
- GET `/api/jobs/<id>/` - Get job details
- PUT `/api/jobs/<id>/` - Update job (Employer only)
- DELETE `/api/jobs/<id>/` - Delete job (Employer only)

### Applications
- GET `/api/applications/` - List user's applications
- POST `/api/applications/create/` - Submit job application
- GET `/api/applications/<id>/` - Get application details

## Testing

Run tests with:
```bash
python manage.py test
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License

## Contact

Miki Mesfin - [@MikiMesfin](https://github.com/MikiMesfin)

Project Link: [https://github.com/MikiMesfin/Job_Boardapp](https://github.com/MikiMesfin/Job_Boardapp)