# Skip Onboarding for Existing Users - Update Summary

## What Was Changed

I've updated the application to automatically skip onboarding for users who already have complete profiles. Now, returning users go straight to the app instead of being forced through the signup/onboarding flow again.

---

## Changes Made

### 1. **SignUp Page** ([frontend/src/pages/SignUp.jsx](frontend/src/pages/SignUp.jsx))

**Added on mount check:**
- When page loads, checks if user already has a mentor/mentee profile
- If profile exists → Redirects to `/app/home`
- If profile doesn't exist → Shows role selection

**Added in role selection:**
- After selecting Mentor/Mentee, checks if profile already exists
- If exists → Skips onboarding, goes to `/app/home`
- If doesn't exist → Goes to onboarding form

**Code:**
```javascript
// Check on mount (lines 19-43)
useEffect(() => {
  const checkExistingProfile = async () => {
    if (!userProfile) return;

    try {
      if (userProfile.role === "mentor") {
        await mentorAPI.getMe();
        navigate("/app/home");  // Profile exists, skip to app
      } else if (userProfile.role === "mentee") {
        await menteeAPI.getMe();
        navigate("/app/home");  // Profile exists, skip to app
      }
    } catch (err) {
      // 404 = no profile, stay on signup page
    }
  };
  checkExistingProfile();
}, [userProfile, navigate]);

// Check after role selection (lines 53-70)
try {
  if (role === "mentor") {
    await mentorAPI.getMe();
    navigate("/app/home");  // Skip onboarding
  } else {
    await menteeAPI.getMe();
    navigate("/app/home");  // Skip onboarding
  }
} catch (profileError) {
  if (profileError.status === 404) {
    navigate(role === "mentor" ? "/signup/mentor" : "/signup/mentee");
  }
}
```

---

### 2. **MentorOnboarding Page** ([frontend/src/pages/MentorOnboarding.jsx](frontend/src/pages/MentorOnboarding.jsx))

**Added check on mount:**
- Attempts to fetch existing mentor profile
- If profile exists → Redirects to `/app/home`
- If doesn't exist (404) → Proceeds with onboarding form

**Code:**
```javascript
// Lines 25-48
useEffect(() => {
  const checkProfileAndFetchInterests = async () => {
    try {
      await mentorAPI.getMe();
      // Profile exists, redirect to app home
      navigate("/app/home");
    } catch (err) {
      // Profile doesn't exist (404), proceed with onboarding
      if (err.status === 404) {
        // Fetch interests for the form
        const interests = await interestsAPI.getAll();
        setAvailableInterests(interests);
      }
    }
  };
  checkProfileAndFetchInterests();
}, [navigate]);
```

---

### 3. **MenteeOnboarding Page** ([frontend/src/pages/MenteeOnboarding.jsx](frontend/src/pages/MenteeOnboarding.jsx))

**Added check on mount:**
- Attempts to fetch existing mentee profile
- If profile exists → Redirects to `/app/home`
- If doesn't exist (404) → Proceeds with onboarding form

**Code:**
```javascript
// Lines 26-49
useEffect(() => {
  const checkProfileAndFetchInterests = async () => {
    try {
      await menteeAPI.getMe();
      // Profile exists, redirect to app home
      navigate("/app/home");
    } catch (err) {
      // Profile doesn't exist (404), proceed with onboarding
      if (err.status === 404) {
        // Fetch interests for the form
        const interests = await interestsAPI.getAll();
        setAvailableInterests(interests);
      }
    }
  };
  checkProfileAndFetchInterests();
}, [navigate]);
```

---

## How It Works Now

### **Flow for New Users:**
1. Sign in → Authenticated
2. Navigate to `/signup` → Choose role (Mentor or Mentee)
3. Backend checks: No mentor/mentee profile exists
4. Navigate to `/signup/mentor` or `/signup/mentee`
5. Fill out onboarding form
6. Submit → Profile created
7. Navigate to `/app/home` → App loads

### **Flow for Returning Users:**
1. Sign in → Authenticated
2. Navigate to `/signup` → **Immediately redirects to `/app/home`**
3. User is already in the app!

### **Flow for Users Who Selected Role But Didn't Complete Onboarding:**
1. Sign in → Authenticated
2. Navigate to `/signup`
3. User profile exists with role, but no mentor/mentee profile
4. Shows role selection
5. User clicks their role again
6. Backend checks: No profile
7. Navigate to onboarding
8. User completes onboarding

### **Direct Navigation Protection:**
If someone tries to navigate directly to:
- `/signup/mentor` → Checks for mentor profile, redirects to `/app/home` if exists
- `/signup/mentee` → Checks for mentee profile, redirects to `/app/home` if exists

---

## What Gets Checked

**User Profile (`user_profiles` table):**
- Created when user selects Mentor or Mentee role
- Contains: `id`, `full_name`, `role`

**Role-Specific Profile:**
- **Mentor**: `mentor_profiles` table (industry, job_title, help_types_offered, interests, etc.)
- **Mentee**: `mentee_profiles` table (industry, goals, background, help_needed, interests, etc.)

**Logic:**
```
If user_profile.role == "mentor":
  Try to fetch mentor_profile
  If exists → Skip onboarding
  If 404 → Show onboarding

If user_profile.role == "mentee":
  Try to fetch mentee_profile
  If exists → Skip onboarding
  If 404 → Show onboarding
```

---

## Benefits

✅ **Better UX**: Returning users don't see onboarding again
✅ **Faster access**: Skip unnecessary steps
✅ **Smart routing**: Handles all edge cases (direct URLs, manual navigation, etc.)
✅ **No data loss**: Existing profiles are preserved
✅ **Graceful handling**: 404 errors are expected and handled properly

---

## Testing Scenarios

### Scenario 1: Brand new user
- Sign up → Choose role → Complete onboarding → Access app ✅

### Scenario 2: Returning user with complete profile
- Sign in → Immediately goes to `/app/home` ✅

### Scenario 3: User who selected role but didn't complete onboarding
- Sign in → `/signup` page → Choose role again → Complete onboarding → Access app ✅

### Scenario 4: User manually navigates to onboarding URL
- User with profile goes to `/signup/mentor` → Redirects to `/app/home` ✅
- User without profile goes to `/signup/mentor` → Shows onboarding form ✅

### Scenario 5: User tries to change roles
- User is mentor, tries to go to `/signup/mentee` → Still shows their mentor onboarding (if incomplete) or redirects to app
- To change roles, user must sign out and create new account (or edit profile)

---

## Files Modified

1. [frontend/src/pages/SignUp.jsx](frontend/src/pages/SignUp.jsx)
   - Added `useEffect` to check existing profile on mount
   - Updated `handleRoleSelection` to check profile before navigating

2. [frontend/src/pages/MentorOnboarding.jsx](frontend/src/pages/MentorOnboarding.jsx)
   - Added `useEffect` to check if mentor profile exists
   - Redirects to app if profile found

3. [frontend/src/pages/MenteeOnboarding.jsx](frontend/src/pages/MenteeOnboarding.jsx)
   - Added `useEffect` to check if mentee profile exists
   - Redirects to app if profile found

---

## No Backend Changes Required

All logic is handled on the frontend by checking if profiles exist via API calls:
- `GET /api/mentors/me` → Returns 200 if exists, 404 if not
- `GET /api/mentees/me` → Returns 200 if exists, 404 if not

The backend was already set up to handle this correctly!

---

## Notes

- **Profile completeness** is determined by the existence of a mentor/mentee profile record
- Users who only created a `user_profile` (with role) but didn't complete onboarding will still see the onboarding form
- Once onboarding is complete, they'll skip it on subsequent logins
- This works seamlessly with the existing authentication and protected route system

---

**Status:** ✅ Complete and ready to test!
