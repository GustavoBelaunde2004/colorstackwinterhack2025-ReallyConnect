# Troubleshooting Guide

## Issue: Stuck in "Choose Your Role" Loop After OAuth

### Symptoms:
- You authenticated with LinkedIn OAuth successfully
- App automatically redirects to `/signup` (role selection page)
- Clicking Mentor or Mentee shows "user not found" error
- Can't proceed past role selection
- Even after restarting, you're stuck on the role selection page

### Root Cause:
After successful OAuth authentication, you have a valid Supabase session (JWT token), but no user profile record in the backend database. The app is authenticated but the user profile doesn't exist yet.

### Solution:

**Option 1: Clear Your Session and Start Fresh**

1. Click the "Sign Out" button on the role selection page
2. Go back to the landing page
3. Click "Sign In"
4. Use **email/password** instead of LinkedIn this time:
   - Email: your-email@example.com
   - Password: create a new password
5. This will create a new Supabase auth user
6. Choose your role (Mentor or Mentee)
7. Complete the onboarding

**Option 2: Clear Browser Storage Manually**

1. Open browser DevTools (F12)
2. Go to Application tab
3. Click "Clear site data" or:
   - Clear Local Storage
   - Clear Session Storage
   - Clear Cookies
4. Refresh the page
5. Start fresh with Sign In

**Option 3: Use the Backend Fix (Already Applied)**

The backend has been updated to handle first-time users automatically. When you click Mentor or Mentee, it will now:
1. Check if a user profile exists
2. If not, create it automatically
3. Then proceed to onboarding

So simply **try clicking Mentor or Mentee again** after the fix is deployed.

---

## Issue: "Not Authenticated" Error

### Symptoms:
- API calls return 401 Unauthorized
- App says "Not authenticated"

### Solutions:

1. **Check if backend is running:**
   ```bash
   # Should be running on http://localhost:8000
   curl http://localhost:8000/health
   ```

2. **Verify Supabase credentials in `.env` files:**
   - Check `backend/.env` has correct `SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY`
   - Check `frontend/.env` has correct `VITE_SUPABASE_URL` and `VITE_SUPABASE_ANON_KEY`

3. **Check if session is valid:**
   - Open DevTools (F12) → Application → Local Storage
   - Look for Supabase session data
   - If expired or missing, sign in again

4. **Restart both servers:**
   ```bash
   # Backend
   cd backend
   uvicorn main:app --reload

   # Frontend (new terminal)
   cd frontend
   npm run dev
   ```

---

## Issue: CORS Policy Error

### Symptoms:
- Browser console shows: "blocked by CORS policy"
- API calls fail with CORS error

### Solutions:

1. **Verify backend CORS configuration:**
   - Check [backend/main.py](backend/main.py:19-25)
   - Should allow `http://localhost:5173`

2. **Check frontend is running on correct port:**
   ```bash
   # Frontend should be on http://localhost:5173
   npm run dev
   ```

3. **Try clearing browser cache:**
   - Hard refresh: Ctrl+Shift+R (Windows/Linux) or Cmd+Shift+R (Mac)

---

## Issue: "User Profile Not Found" (404)

### Symptoms:
- After signing in, you see a 404 error
- Profile page shows error

### Solutions:

1. **This is expected for new users!**
   - After authentication, you need to:
     1. Choose your role (Mentor or Mentee)
     2. Complete the onboarding form
   - The profile is created during role selection

2. **If stuck on role selection:**
   - See "Stuck in Choose Your Role Loop" above

3. **If profile was deleted:**
   - Sign out and create a new account
   - Or manually recreate profile via onboarding

---

## Issue: No Mentors/Mentees Showing

### Symptoms:
- AppHome shows "No mentors to show"
- Matches page is empty

### Solutions:

1. **Create test accounts:**
   - You need at least 2 accounts to test matching
   - Create 1 Mentor account
   - Create 1 Mentee account (in incognito/different browser)

2. **Check database has interests:**
   ```bash
   # In Supabase SQL Editor, run:
   SELECT COUNT(*) FROM interests;
   # Should return 52
   ```

3. **Verify mentor profile is active:**
   - Mentor profiles have `is_active` flag
   - Set to `true` during onboarding

4. **Check industry matching:**
   - Mentors and mentees must have same industry for recommendations
   - Edit profiles to match industries

---

## Issue: Database Schema Errors

### Symptoms:
- SQL errors in backend logs
- "relation does not exist" errors
- "column does not exist" errors

### Solutions:

1. **Run database migrations:**
   - Go to Supabase dashboard → SQL Editor
   - Copy contents of `backend/database/schema.sql`
   - Paste and execute
   - Copy contents of `backend/database/seed_interests.sql`
   - Paste and execute

2. **Check Supabase connection:**
   ```bash
   curl http://localhost:8000/test-supabase
   # Should return: {"status": "connected"}
   ```

3. **Verify table names in Supabase:**
   - Go to Supabase dashboard → Table Editor
   - Should see: user_profiles, interests, mentor_profiles, etc.

---

## Issue: Frontend Won't Start

### Symptoms:
- `npm run dev` fails
- Module not found errors

### Solutions:

1. **Reinstall dependencies:**
   ```bash
   cd frontend
   rm -rf node_modules package-lock.json
   npm install
   npm run dev
   ```

2. **Check Node version:**
   ```bash
   node --version  # Should be 18+
   ```

3. **Check for port conflicts:**
   ```bash
   # Kill process on port 5173
   lsof -ti:5173 | xargs kill -9  # Mac/Linux
   # Windows: netstat -ano | findstr :5173, then taskkill /PID <PID> /F
   ```

---

## Issue: Backend Won't Start

### Symptoms:
- `uvicorn main:app --reload` fails
- Import errors
- Module not found

### Solutions:

1. **Reinstall dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Check Python version:**
   ```bash
   python --version  # Should be 3.10+
   ```

3. **Activate virtual environment:**
   ```bash
   # Mac/Linux
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

4. **Check environment variables:**
   ```bash
   # Make sure .env file exists
   ls -la backend/.env
   ```

---

## Issue: LinkedIn OAuth Not Working

### Symptoms:
- "Sign In through LinkedIn" button does nothing
- OAuth redirect fails

### Solutions:

1. **LinkedIn OAuth requires setup:**
   - Go to Supabase dashboard → Authentication → Providers
   - Enable LinkedIn provider
   - Add LinkedIn OAuth credentials from LinkedIn Developers portal
   - Add redirect URL: `http://localhost:5173/signup`

2. **Use email/password instead:**
   - Email authentication works out of the box
   - No additional setup required

3. **Check Supabase auth settings:**
   - Go to Authentication → URL Configuration
   - Verify redirect URLs include `http://localhost:5173`

---

## Debug Checklist

When something goes wrong, check:

1. ✅ Backend is running (`http://localhost:8000/health`)
2. ✅ Frontend is running (`http://localhost:5173`)
3. ✅ Database schema is loaded in Supabase
4. ✅ Environment variables are set (both `.env` files)
5. ✅ Supabase credentials are correct
6. ✅ Browser console has no errors (F12 → Console)
7. ✅ Network tab shows successful API calls (F12 → Network)
8. ✅ You're signed in (check Application → Local Storage)

---

## Getting Help

If none of these solutions work:

1. **Check browser console** (F12 → Console) for error messages
2. **Check backend terminal** for error logs
3. **Check Supabase logs** (Dashboard → Logs)
4. **Inspect Network tab** (F12 → Network) to see failed requests
5. **Review the code** at the error location

**Common Error Patterns:**

- **401 Unauthorized** → Authentication issue (JWT token missing/invalid)
- **404 Not Found** → Resource doesn't exist (profile, mentor, etc.)
- **403 Forbidden** → Permission issue (wrong role, RLS policy)
- **500 Internal Server Error** → Backend crash (check terminal logs)
- **CORS error** → Frontend/backend URL mismatch

---

## Still Stuck?

Create an issue with:
1. What you were trying to do
2. What happened instead
3. Browser console errors
4. Backend terminal errors
5. Steps to reproduce
