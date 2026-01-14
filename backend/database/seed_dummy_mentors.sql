-- Seed Dummy Mentor Data for Testing
-- This script creates test mentor profiles in the Engineering industry
-- Run this after your database schema is set up

-- Instructions:
-- 1. First, create dummy users in Supabase Dashboard:
--    - Go to Authentication > Users > Add User
--    - Create 5-10 test users with emails like: mentor1@test.com, mentor2@test.com, etc.
--    - Use any password (e.g., "Test123!")
--    - Copy the UUID of each created user
--
-- 2. Replace the UUIDs in this script with the real user IDs from Supabase
--
-- 3. Run this SQL script in Supabase SQL Editor

-- Note: Using placeholder UUIDs - REPLACE THESE with real auth.users UUIDs from your Supabase project
-- Format: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx'

-- ====================
-- DUMMY USER PROFILES
-- ====================

-- Mentor 1: Senior Software Engineer
INSERT INTO user_profiles (user_id, email, full_name, role, industry, created_at, updated_at)
VALUES (
  'fb7ddb70-62e9-4c6c-9459-2767c4acc111', -- REPLACE with real UUID
  'mentor1@test.com',
  'Sarah Chen',
  'mentor',
  'Engineering',
  NOW(),
  NOW()
) ON CONFLICT (user_id) DO NOTHING;

-- Mentor 2: Engineering Manager
INSERT INTO user_profiles (user_id, email, full_name, role, industry, created_at, updated_at)
VALUES (
  '2dfd97d6-f788-4b07-8d8a-0720d812596c', -- REPLACE with real UUID
  'mentor2@test.com',
  'Marcus Johnson',
  'mentor',
  'Engineering',
  NOW(),
  NOW()
) ON CONFLICT (user_id) DO NOTHING;



-- ====================
-- MENTOR PROFILES
-- ====================

-- Mentor 1: Senior Software Engineer - Resume & Interview Focus
INSERT INTO mentor_profiles (
  user_id,
  job_title,
  company,
  years_of_experience,
  industry,
  bio,
  help_types_offered,
  max_requests_per_week,
  is_active,
  created_at,
  updated_at
) VALUES (
  'fb7ddb70-62e9-4c6c-9459-2767c4acc111', -- REPLACE with real UUID
  'Senior Software Engineer',
  'Google',
  8,
  'Engineering',
  'Passionate about helping engineers level up their careers. Specialized in system design and technical interviews at FAANG companies.',
  ARRAY['resume_review', 'mock_interview', 'career_advice']::help_type[],
  5,
  TRUE,
  NOW(),
  NOW()
) ON CONFLICT (user_id) DO NOTHING;

-- Mentor 2: Engineering Manager - Leadership & Career Growth
INSERT INTO mentor_profiles (
  user_id,
  job_title,
  company,
  years_of_experience,
  industry,
  bio,
  help_types_offered,
  max_requests_per_week,
  is_active,
  created_at,
  updated_at
) VALUES (
  '2dfd97d6-f788-4b07-8d8a-0720d812596c', -- REPLACE with real UUID
  'Engineering Manager',
  'Microsoft',
  12,
  'Engineering',
  'Former engineer turned manager. Love helping engineers transition to leadership roles and navigate career growth.',
  ARRAY['career_advice', 'resume_review', 'mock_interview']::help_type[],
  4,
  TRUE,
  NOW(),
  NOW()
) ON CONFLICT (user_id) DO NOTHING;


-- ====================
-- MENTOR INTERESTS (Optional - links to existing interests)
-- ====================
-- Note: This assumes you have interests already in your interests table
-- You may need to adjust interest_ids based on your actual interests table

-- Example: Link mentors to common engineering interests
-- Uncomment and adjust these if you have interests set up:

/*
-- Link Mentor 1 (Sarah) to Web Development & Algorithms interests
INSERT INTO mentor_interests (mentor_id, interest_id, created_at)
VALUES
  ('00000000-0000-0000-0000-000000000001', 1, NOW()),
  ('00000000-0000-0000-0000-000000000001', 5, NOW())
ON CONFLICT DO NOTHING;

-- Link Mentor 2 (Marcus) to Leadership & Career Development interests
INSERT INTO mentor_interests (mentor_id, interest_id, created_at)
VALUES
  ('00000000-0000-0000-0000-000000000002', 10, NOW()),
  ('00000000-0000-0000-0000-000000000002', 12, NOW())
ON CONFLICT DO NOTHING;

-- Continue for other mentors as needed...
*/

-- ====================
-- VERIFICATION QUERIES
-- ====================
-- Run these to verify the data was inserted correctly:

-- Check user profiles
-- SELECT user_id, email, full_name, role, industry FROM user_profiles WHERE role = 'mentor' ORDER BY created_at DESC;

-- Check mentor profiles
-- SELECT user_id, job_title, company, years_of_experience, help_types_offered, is_active FROM mentor_profiles ORDER BY created_at DESC;

-- Check count
-- SELECT COUNT(*) as mentor_count FROM mentor_profiles WHERE industry = 'Engineering' AND is_active = TRUE;
