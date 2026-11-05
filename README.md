# Fresavelle — Stage 2 local catalogue

The storefront uses a local SQLite database containing example products, prices and stock. Product categories, fixed units, availability, search and independent basket stock are database-backed. Images are illustrative. Cart, checkout, payments and customer accounts are not connected.

## Start the local API and staff controls

In a PowerShell window from the project folder:

```powershell
cd backend
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
.venv\Scripts\python.exe manage.py migrate
.venv\Scripts\python.exe manage.py seed_samples
.venv\Scripts\python.exe manage.py createsuperuser
.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
```

Choose a local username and password interactively; do not post the password in chat. The management screen is http://127.0.0.1:8000/staff/. The superuser can create staff users and grant only needed category/product permissions. This is a **development-only** Django interface, not the Stage 7 dashboard: its settings, login protections and local SQLite database are not production-ready. Do not expose it to a network or enter real customer data. Stock values are counts of the selected fixed selling unit; price is in kobo (100 kobo = ₦1). Basket stock is independent and does not adjust ingredients. The sample seed does not overwrite existing records.

On this machine, if the Python virtual-environment launcher remains broken and the previously downloaded wheels in `backend/.wheels` are present, run these commands instead, from `backend`:

```powershell
python -c "from pathlib import Path; from zipfile import ZipFile; [ZipFile(w).extractall('.deps') for w in Path('.wheels').glob('*.whl')]"
$env:PYTHONPATH = (Resolve-Path '.deps').Path
python manage.py migrate
python manage.py seed_samples
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8000
```

Run `createsuperuser` once, not on every startup. Leave the API window open. API: http://127.0.0.1:8000/api/products/.

## Start the storefront

In a second PowerShell window:

```powershell
cd frontend
npm.cmd install
npm.cmd run build
npm.cmd run start -- --hostname 127.0.0.1 --port 3001
```

Open http://127.0.0.1:3001. Leave both windows open. If the API is down the page reports that the catalogue is unavailable.

## Database and credentials

Supabase PostgreSQL remains the agreed future database, but has not been configured or tested. This local stage does not need a Supabase account or credentials. When a test project is needed, create a separate Supabase test project, retrieve its PostgreSQL connection string from its dashboard, and place secrets only in an ignored local environment file such as `backend/.env` or a secure deployment secret store; never commit it or paste credentials into chat. PostgreSQL configuration, migration and connectivity must be implemented and verified before claiming Supabase support. Supabase Storage is not connected.

## Tests

With the virtual environment active, run `python manage.py test` in `backend`. With the local wheel fallback above, set `PYTHONPATH` to `.deps` first. The automated tests use a separate temporary test database.

## Stage 2 shopping pages

The home page is at http://127.0.0.1:3001/. Browse http://127.0.0.1:3001/catalogue, search at http://127.0.0.1:3001/search?search=rice, and open a product from its card. Category and sorting selections stay in the URL. Product descriptions can be edited in the local staff interface; existing examples without descriptions show a placeholder.

Use the footer's **Staff sign in** link with the local Django superuser you created or a local staff account explicitly granted catalogue permissions. It is separate from customer Account. The staff screen is temporary and development-only; its prices are entered in kobo. The future custom dashboard should accept naira while the backend stores integer kobo.

## Separate Supabase PostgreSQL test setup (Stage 2)

Use a new test project, not an existing production project. Disable the Supabase Data API in its integration settings before migrating: Django owns access and its tables are not configured for the generated Data API. In the Supabase Connect dialog choose Session pooler (the IPv4-compatible session connection), and replace the password placeholder; percent-encode any reserved characters in the password. Save this single line in the ignored local file `backend/.env.supabase.local`, not in chat or source control:

```text
FRESAVELLE_TEST_DATABASE_URL=postgresql://USER:PASSWORD@YOUR-TEST-HOST:5432/postgres
```

With the existing local wheel setup, set `$env:PYTHONPATH = (Resolve-Path '.deps').Path` from the backend directory. To explicitly opt into the separate database, use `python manage.py migrate --settings=config.settings_supabase` and `python manage.py test --settings=config.settings_supabase`. These commands do not migrate or overwrite SQLite. The Django test suite asks PostgreSQL to create a uniquely named temporary database; if the provider denies this, it must be resolved without running tests against existing data. PostgreSQL results must be reported separately from SQLite results. The test connection requires TLS encryption (`sslmode=require`); certificate verification and production security require further work before launch.

To return to SQLite, use the ordinary management commands without `--settings=config.settings_supabase`. No records are copied or reset automatically, and separate staff credentials are required for any new database.
