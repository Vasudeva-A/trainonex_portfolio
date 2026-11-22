# Trainonex Interactive Portfolio + Admin CMS

A beginner-friendly Django portfolio project inspired by the supplied reference:
- Responsive, multi-page public site with Home, About, Services, Work, Case Study and Contact pages
- Project cards, category filters and individual case-study pages
- Django login for staff users
- Dashboard with project/category CRUD, image uploads and publish/draft status
- Contact form saved to the database
- SQLite by default; optional MySQL configuration through environment variables

## 1. Setup (Windows)

```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000

## 2. Admin dashboard

Open http://127.0.0.1:8000/accounts/login/
Sign in using the superuser created with `createsuperuser`.
Dashboard: http://127.0.0.1:8000/dashboard/

Do not publish or share your real admin password in GitHub or README.

## 3. Add projects

Use Dashboard > Add Project. Add a title, category, description, optional cover image and toggle Published.
Only published projects appear on the public site.

## 4. Optional MySQL

SQLite is configured by default. To switch:
1. Install and verify the MySQL server and Python driver in your environment.
2. Set `DB_ENGINE=mysql` and the DB values in `.env`.
3. Create the database and a restricted database user.
4. Run `python manage.py migrate`.
5. Test login, project CRUD, image upload and contact form against MySQL.

Install `mysqlclient` only when you are ready and your Windows security policy allows it:
`pip install mysqlclient`

Never disable Windows security controls to load a database driver.

## 5. Production checklist

- Set DEBUG=False and a strong SECRET_KEY in the hosting environment.
- Set ALLOWED_HOSTS to your real domain.
- Configure HTTPS and secure cookies.
- Use persistent media storage for uploaded project images.
- Keep secrets out of GitHub.
- Back up the database.
- Create a staff/superuser account securely on the host.

This is a learning/assessment starter, not a hardened enterprise CMS. Review host-specific security and storage settings before public production use.
