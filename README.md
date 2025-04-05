# Asset Management System

A Django-based asset management system for tracking company assets and their assignments to employees. This system helps organizations manage and track their assets efficiently.

## Features

### Employee Management
- Full CRUD operations for employee records
- Track employee information:
  - Full Name
  - Work Email Address
  - Country (with options for Timor Leste, Papua New Guinea, Australia, Fiji, Indonesia)
  - Other country specification option

### Asset Management
- Complete CRUD operations for asset records
- Asset Types supported:
  - Laptop
  - Monitor
  - Mobile Phone
  - Other (with specification option)
- Track detailed asset information:
  - Asset Name/Model
  - Serial Number
  - Responsible Person
  - Location
  - Working Condition Status
  - Adapter Information
  - Charger Details
  - Additional Notes

## Technology Stack

- Python 3.x
- Django 4.x
- Bootstrap 5 (for responsive UI)
- SQLite (database)
- HTML/CSS
- JavaScript

## Installation

1. Clone the repository
```bash
git clone https://github.com/joanico/asset-management-system.git
cd asset-management-system
```

2. Create and activate virtual environment
```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python -m venv venv
source venv/bin/activate
```

3. Install required packages
```bash
pip install -r requirements.txt
```

4. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser (optional)
```bash
python manage.py createsuperuser
```

6. Start development server
```bash
python manage.py runserver
```

7. Visit the application 
```

## Project Structure
```

## Features Details

### Employee Management
- Create new employee records
- View list of all employees
- Update employee information
- Delete employee records
- Track assigned assets per employee

### Asset Management
- Register new assets
- View comprehensive asset list
- Update asset information
- Delete asset records
- Track asset status and location
- Monitor asset assignments

## Testing

Run the test suite:
```bash
# Run all tests
python manage.py test

# Run specific test file
python manage.py test asset_app.test_models
python manage.py test asset_app.test_views

# Run with verbosity for more details
python manage.py test -v 2
```

## Development

1. Create a new branch for features
```bash
git checkout -b feature/new-feature
```

2. Make changes and commit
```bash
git add .
git commit -m "Add new feature: description"
```

3. Push changes
```bash
git push origin feature/new-feature
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Author

- **Joanico** - *Initial work* - [joanico](https://github.com/joanico)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

- Django Documentation
- Bootstrap Documentation
- Python Testing Best Practices