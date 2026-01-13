# ReallyConnect Setup Guide

This guide will help you connect the frontend and backend of ReallyConnect.

## Prerequisites

- Node.js 18+ and npm
- Python 3.10+
- A Supabase account (free tier is fine)

## Step 1: Supabase Setup

1. **Create a Supabase project**
   - Go to [https://app.supabase.com](https://app.supabase.com)
   - Create a new project
   - Wait for the project to be provisioned

2. **Run the database schema**
   - Navigate to SQL Editor in your Supabase dashboard
   - Copy the contents of `backend/database/schema.sql`
   - Paste and run it in the SQL Editor
   - Copy the contents of `backend/database/seed_interests.sql`
   - Paste and run it in the SQL Editor to populate interests

3. **Get your API credentials**
   - Go to Project Settings > API
   - Copy the following values:
     - Project URL (e.g., `https://xxxxx.supabase.co`)
     - `anon` / `public` key
     - `service_role` key (keep this secret!)
     - JWT Secret (optional, in Project Settings > API > JWT Settings)

4. **Configure Authentication**
   - Go to Authentication > Providers
   - Enable Email provider (for email/password auth)
   - Optional: Enable LinkedIn OAuth
     - Follow Supabase docs to set up LinkedIn OAuth
     - Add your redirect URL: `http://localhost:5173/signup`

## Step 2: Backend Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create environment file**
   ```bash
   cp .env.example .env
   ```

5. **Edit `.env` file**
   ```
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_SERVICE_ROLE_KEY=your-service-role-key-here
   ```

6. **Test the connection**
   ```bash
   uvicorn main:app --reload
   ```
   - Open [http://localhost:8000/test-supabase](http://localhost:8000/test-supabase)
   - You should see: `{"status": "connected", "message": "Successfully connected to Supabase"}`

7. **Keep the backend running**
   - The backend will run on http://localhost:8000
   - Leave this terminal window open

## Step 3: Frontend Setup

1. **Open a new terminal** and navigate to frontend directory
   ```bash
   cd frontend
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Create environment file**
   ```bash
   cp .env.example .env
   ```

4. **Edit `.env` file**
   ```
   VITE_SUPABASE_URL=https://your-project.supabase.co
   VITE_SUPABASE_ANON_KEY=your-anon-public-key-here
   VITE_API_BASE_URL=http://localhost:8000
   ```

5. **Start the development server**
   ```bash
   npm run dev
   ```
   - Frontend will run on http://localhost:5173

## Step 4: Test the Integration

1. **Open your browser** to [http://localhost:5173](http://localhost:5173)

2. **Create a test account**
   - Click "Sign In"
   - Since LinkedIn OAuth may not be configured, use "Sign In with Email"
   - Or go to Supabase Dashboard > Authentication > Users > Add User manually

3. **Test the flow**
   - Sign up with email/password
   - Choose Mentor or Mentee role
   - Complete the onboarding form
   - Navigate to /app/home

4. **Verify API calls**
   - Open browser DevTools (F12) > Network tab
   - You should see API calls to `http://localhost:8000/api/...`
   - Check backend terminal for request logs

## Common Issues

### Issue: "Not authenticated" error
- **Solution**: Make sure you're signed in and have a valid JWT token
- Check browser DevTools > Application > Local Storage for Supabase session

### Issue: "CORS policy" error
- **Solution**: Backend CORS is already configured to allow all origins
- If still issues, check `backend/main.py` CORS settings

### Issue: "Failed to connect to backend"
- **Solution**: Ensure backend is running on http://localhost:8000
- Check `VITE_API_BASE_URL` in frontend `.env` file

### Issue: "No mentors to show"
- **Solution**: Create mentor profiles through the onboarding flow
- You need at least 2 accounts: one mentor and one mentee to test matching

### Issue: "Cannot read properties of undefined"
- **Solution**: Make sure database schema is properly set up
- Re-run `backend/database/schema.sql` in Supabase SQL Editor

## Testing User Flows

### Mentor Flow
1. Sign up with email: `mentor@test.com`
2. Choose "Mentor" role
3. Complete mentor onboarding:
   - Industry: Software Engineering
   - Job Title: Senior Developer
   - Help types: Select all
   - Max requests: 5
   - Select at least 3 interests
4. Navigate to /app/matches to see incoming requests
5. Accept/decline requests from mentees

### Mentee Flow
1. Sign up with email: `mentee@test.com`
2. Choose "Mentee" role
3. Complete mentee onboarding:
   - Industry: Software Engineering
   - Goals: Learn to code
   - Background: Student
   - Help needed: Select relevant types
   - Select at least 3 interests
4. Navigate to /app/home to see recommended mentors
5. Swipe right (like) to send mentorship request
6. Check /app/matches to see accepted requests

## Production Deployment

### Backend Deployment
1. Update CORS in `backend/main.py`:
   ```python
   allow_origins=["https://your-frontend-domain.com"]
   ```

2. Deploy to a platform:
   - Railway.app
   - Heroku
   - DigitalOcean App Platform
   - Google Cloud Run

3. Set environment variables on the platform

### Frontend Deployment
1. Update `.env` for production:
   ```
   VITE_API_BASE_URL=https://your-backend-domain.com
   ```

2. Build the frontend:
   ```bash
   npm run build
   ```

3. Deploy to:
   - Vercel (recommended)
   - Netlify
   - GitHub Pages
   - AWS S3 + CloudFront

4. Update Supabase redirect URLs:
   - Go to Authentication > URL Configuration
   - Add your production URL to redirect URLs

## Architecture Overview

```
┌─────────────────┐
│   Frontend      │
│   (React)       │
│   Port: 5173    │
└────────┬────────┘
         │
         │ HTTP Requests (with JWT)
         │
         ▼
┌─────────────────┐
│   Backend       │
│   (FastAPI)     │
│   Port: 8000    │
└────────┬────────┘
         │
         │ Supabase Client (Service Role)
         │
         ▼
┌─────────────────┐
│   Supabase      │
│   (PostgreSQL   │
│   + Auth)       │
└─────────────────┘
```

## API Endpoints

All API endpoints are documented at [http://localhost:8000/docs](http://localhost:8000/docs) when the backend is running.

Key endpoints:
- `POST /api/users/me` - Create/update user profile
- `GET /api/interests` - Get all interests (public)
- `POST /api/mentors/me` - Create mentor profile
- `POST /api/mentees/me` - Create mentee profile
- `GET /api/recommendations` - Get recommended mentors
- `POST /api/requests` - Create mentorship request
- `PATCH /api/requests/{id}/accept` - Accept request (mentor only)
- `GET /api/requests` - Get user's requests

## Need Help?

- Check browser console for errors (F12 > Console)
- Check backend terminal for error logs
- Check Supabase logs in dashboard
- Review API responses in Network tab (F12 > Network)
