Run:
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
-
- API paths:
- POST /api/auth/users/
- POST /api/auth/jwt/create/
- GET/POST /api/menu-items/
- GET/PUT/PATCH/DELETE /api/menu-items/{id}/
- GET/POST /api/bookings/
- GET/PUT/PATCH/DELETE /api/bookings/{id}/

- Tests:
- python manage.py test

- Auth:

- POST /api/auth/users/      (register)
- POST /api/auth/jwt/create/ (login → use access token as Bearer)
