# SkillX — Setup Guide

## Backend (Django)

```bash
cd backend
pip install -r requirements.txt
pip install google-auth          # for Google OAuth support
python manage.py migrate
python manage.py runserver
```

Set these environment variables for production:
- `DJANGO_SECRET_KEY` — a strong random secret
- `DJANGO_DEBUG` — set to `False`
- `DJANGO_ALLOWED_HOSTS` — comma-separated list of allowed hostnames
- `GOOGLE_CLIENT_ID` — your Google OAuth client ID

## Frontend (React + Vite)

```bash
cd Frontend
cp .env.example .env             # edit if backend runs on a different port
npm install
npm run dev
```

The app will be at http://localhost:5173

## What was fixed

| # | File | Bug |
|---|------|-----|
| 1 | `backend/api/views.py` | `validate_password_strength()` raised `ValueError` but was never caught → signup crashed with HTTP 500 |
| 2 | `backend/api/views.py` | `/api/auth/google/` endpoint missing → Google login always 404'd |
| 3 | `backend/api/views.py` | `/api/code/hint/` endpoint missing → Hint button always 404'd |
| 4 | `backend/api/views.py` | `run_code` returned `{output, error}` but frontend expected `{results:[{passed,output}]}` → test panel was always blank |
| 5 | `backend/api/views.py` | `submit_code` now actually runs test cases and returns Accepted/Wrong Answer correctly |
| 6 | `backend/api/views.py` | `login` and `signup` now both return the `refresh` token the frontend stores |
| 7 | `backend/api/urls.py` | Admin URLs used `<int:user_id>` but admin_views expected `username` string → all admin endpoints crashed |
| 8 | `backend/api/urls.py` | `/api/auth/google/` and `/api/code/hint/` not registered |
| 9 | `backend/api/admin_views.py` | Parameter name mismatch with URL patterns fixed |
| 10 | `Frontend/src/pages/Companies.jsx` | **Git merge conflicts** left in file → entire Companies page crashed to blank |
| 11 | `Frontend/src/pages/Companies.jsx` | Questions used `q.leetcode_url` field that doesn't exist → links never opened |
| 12 | `Frontend/src/pages/Companies.jsx` | `openQuestion()` now guarantees a full `https://leetcode.com/...` URL |
| 13 | `Frontend/src/App.jsx` | `Interview` was lazy-imported from `./pages/Interview.jsx` (empty stub) instead of `Companies.jsx` where it's actually exported |
