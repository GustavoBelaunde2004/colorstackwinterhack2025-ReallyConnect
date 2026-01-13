-- Add profile_picture_url columns to mentor and mentee profiles
-- Run this SQL in Supabase SQL Editor to add profile picture support

-- Add profile_picture_url to mentor_profiles
ALTER TABLE mentor_profiles
ADD COLUMN IF NOT EXISTS profile_picture_url TEXT;

-- Add profile_picture_url to mentee_profiles
ALTER TABLE mentee_profiles
ADD COLUMN IF NOT EXISTS profile_picture_url TEXT;

-- Create storage bucket for profile pictures (if not exists)
-- This should be run separately in Supabase Storage UI or via SQL
-- Note: You'll need to create this bucket in Supabase Dashboard > Storage
-- Bucket name: profile-pictures
-- Public: true (so images can be displayed)
