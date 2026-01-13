# ReallyConnect - Quick Start Guide

Get the app running in 10 minutes!

## Prerequisites Check

```bash
node --version  # Should be 18+
python --version  # Should be 3.10+
```

## 1. Supabase Setup (5 min)

1. Go to https://app.supabase.com and create a new project
2. Wait for project to provision
3. Go to SQL Editor and run these files:
   - Copy/paste `backend/database/schema.sql` → Run
   - Copy/paste `backend/database/seed_interests.sql` → Run
4. Go to Settings > API and copy:
   - Project URL
   - `anon public` key
   - `service_role` key

## 2. Backend Setup (2 min)

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env`:
```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
```

Start backend:
```bash
uvicorn main:app --reload
```

Test: Open http://localhost:8000/test-supabase
Should see: `{"status": "connected"}`

## 3. Frontend Setup (2 min)

Open a NEW terminal:

```bash
cd frontend
npm install
cp .env.example .env
```

Edit `.env`:
```
VITE_SUPABASE_URL=https://your-project.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
VITE_API_BASE_URL=http://localhost:8000
```

Start frontend:
```bash
npm run dev
```

## 4. Test It (1 min)

1. Open http://localhost:5173
2. Click "Sign In"
3. Create account with email/password
4. Choose role (Mentor or Mentee)
5. Complete onboarding
6. Browse matches!

## Troubleshooting

**"Not authenticated"**
- Check if backend is running (http://localhost:8000)
- Verify Supabase keys in `.env` files

**"CORS error"**
- Backend CORS already configured
- Make sure frontend is on http://localhost:5173

**"No mentors"**
- Create multiple accounts (at least 1 mentor, 1 mentee)
- Make sure database schema was run

## That's It!

For detailed info, see [SETUP.md](SETUP.md) or [INTEGRATION_COMPLETE.md](INTEGRATION_COMPLETE.md).

**The app is fully connected and ready to use!** 🚀
