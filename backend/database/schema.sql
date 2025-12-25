-- ReallyConnect Database Schema
-- Run this SQL in Supabase SQL Editor to create all tables

-- ============================================
-- 1. User Profiles (extends auth.users)
-- ============================================
CREATE TABLE IF NOT EXISTS user_profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    full_name TEXT,
    role TEXT NOT NULL CHECK (role IN ('mentor', 'mentee', 'both')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_user_profiles_role ON user_profiles(role);

-- ============================================
-- 2. Mentor Profiles
-- ============================================
CREATE TABLE IF NOT EXISTS mentor_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL UNIQUE REFERENCES auth.users(id) ON DELETE CASCADE,
    industry TEXT,
    role TEXT,  -- Job title/role
    help_types_offered TEXT[] NOT NULL DEFAULT '{}',
    max_requests_per_week INTEGER NOT NULL DEFAULT 3 CHECK (max_requests_per_week > 0),
    interests TEXT[] DEFAULT '{}',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for matching queries
CREATE INDEX IF NOT EXISTS idx_mentor_active ON mentor_profiles(is_active) WHERE is_active = TRUE;
CREATE INDEX IF NOT EXISTS idx_mentor_help_types ON mentor_profiles USING GIN(help_types_offered);
CREATE INDEX IF NOT EXISTS idx_mentor_interests ON mentor_profiles USING GIN(interests);
CREATE INDEX IF NOT EXISTS idx_mentor_industry ON mentor_profiles(industry);

-- ============================================
-- 3. Mentee Profiles
-- ============================================
CREATE TABLE IF NOT EXISTS mentee_profiles (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID NOT NULL UNIQUE REFERENCES auth.users(id) ON DELETE CASCADE,
    goals TEXT,
    help_needed TEXT[] NOT NULL DEFAULT '{}',
    background TEXT,
    interests TEXT[] DEFAULT '{}',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes for matching queries
CREATE INDEX IF NOT EXISTS idx_mentee_help_needed ON mentee_profiles USING GIN(help_needed);
CREATE INDEX IF NOT EXISTS idx_mentee_interests ON mentee_profiles USING GIN(interests);

-- ============================================
-- 4. Mentorship Requests
-- ============================================
CREATE TABLE IF NOT EXISTS mentorship_requests (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    mentee_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    mentor_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    help_type TEXT NOT NULL CHECK (help_type IN ('resume_review', 'mock_interview', 'career_advice', 'social_advice')),
    context TEXT NOT NULL,
    key_questions TEXT[] NOT NULL DEFAULT '{}',
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'accepted', 'declined')),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    responded_at TIMESTAMPTZ
);

-- Prevent duplicate pending requests using partial unique index
CREATE UNIQUE INDEX IF NOT EXISTS idx_no_duplicate_pending 
    ON mentorship_requests(mentee_id, mentor_id) 
    WHERE status = 'pending';

-- Indexes for common queries
CREATE INDEX IF NOT EXISTS idx_requests_mentor_status ON mentorship_requests(mentor_id, status);
CREATE INDEX IF NOT EXISTS idx_requests_mentee ON mentorship_requests(mentee_id);
CREATE INDEX IF NOT EXISTS idx_requests_status ON mentorship_requests(status) WHERE status = 'pending';
CREATE INDEX IF NOT EXISTS idx_requests_created ON mentorship_requests(created_at DESC);

-- ============================================
-- 5. Connections (Accepted Requests)
-- ============================================
CREATE TABLE IF NOT EXISTS connections (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    mentor_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    mentee_id UUID NOT NULL REFERENCES auth.users(id) ON DELETE CASCADE,
    request_id UUID REFERENCES mentorship_requests(id) ON DELETE SET NULL,
    contact_exchanged BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    
    -- Prevent duplicate connections
    CONSTRAINT unique_connection UNIQUE (mentor_id, mentee_id)
);

CREATE INDEX IF NOT EXISTS idx_connections_mentor ON connections(mentor_id);
CREATE INDEX IF NOT EXISTS idx_connections_mentee ON connections(mentee_id);
CREATE INDEX IF NOT EXISTS idx_connections_created ON connections(created_at DESC);

