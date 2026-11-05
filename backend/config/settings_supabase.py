"""Opt-in Supabase test settings; never use with production data."""
import os
from pathlib import Path
from urllib.parse import unquote, urlsplit
from uuid import uuid4
from django.core.exceptions import ImproperlyConfigured
from .settings import *  # noqa: F403

secret_file = Path(__file__).resolve().parent.parent / '.env.supabase.local'
url = os.environ.get('FRESAVELLE_TEST_DATABASE_URL', '')
if not url and secret_file.is_file():
    for line in secret_file.read_text(encoding='utf-8-sig').splitlines():
        if line.startswith('FRESAVELLE_TEST_DATABASE_URL='):
            url = line.partition('=')[2].strip().strip('"').strip("'")
            break
if not url:
    raise ImproperlyConfigured('Set FRESAVELLE_TEST_DATABASE_URL in backend/.env.supabase.local for the separate Supabase test project.')
try:
    parsed = urlsplit(url)
    host = parsed.hostname or ''
    port = parsed.port or 5432
    if parsed.scheme not in ('postgres', 'postgresql') or not parsed.username or not parsed.password or not parsed.path.strip('/') or not (host.endswith('.supabase.co') or host.endswith('.supabase.com')):
        raise ValueError('Invalid test connection')
except ValueError:
    raise ImproperlyConfigured('Invalid Supabase test connection. Check the local secret file without sharing it.') from None

DATABASES = {'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': unquote(parsed.path.lstrip('/')),
    'USER': unquote(parsed.username),
    'PASSWORD': unquote(parsed.password),
    'HOST': host,
    'PORT': port,
    'OPTIONS': {'sslmode': 'require', 'connect_timeout': 10},
    'CONN_MAX_AGE': 0,
    'TEST': {'NAME': 'fresavelle_test_' + uuid4().hex[:12]},
}}
