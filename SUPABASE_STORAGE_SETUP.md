# Supabase Storage Setup Guide

## Overview
This guide shows you how to set up Supabase Storage for profile picture uploads in ReallyConnect.

---

## Step 1: Create Storage Bucket

1. Open your Supabase project dashboard at [https://supabase.com/dashboard](https://supabase.com/dashboard)

2. Navigate to **Storage** in the left sidebar

3. Click **"New bucket"** button

4. Configure the bucket:
   - **Name**: `profile-pictures`
   - **Public bucket**: ✅ YES (check this box)
   - **File size limit**: 2MB
   - **Allowed MIME types**: Leave default (all images allowed)

5. Click **"Create bucket"**

---

## Step 2: Set Up Row Level Security (RLS) Policies

### Why RLS Policies?
RLS policies ensure users can only upload to their own folder and prevent unauthorized access.

### Apply the Policies

1. In Supabase Dashboard, navigate to **SQL Editor** (left sidebar)

2. Click **"New query"**

3. Copy and paste the following SQL:

```sql
-- Policy 1: Allow authenticated users to upload to their own folder
CREATE POLICY "Users can upload own profile picture"
ON storage.objects FOR INSERT
TO authenticated
WITH CHECK (
  bucket_id = 'profile-pictures' AND
  (storage.foldername(name))[1] = auth.uid()::text
);

-- Policy 2: Allow users to update their own images
CREATE POLICY "Users can update own profile picture"
ON storage.objects FOR UPDATE
TO authenticated
USING (
  bucket_id = 'profile-pictures' AND
  (storage.foldername(name))[1] = auth.uid()::text
);

-- Policy 3: Allow users to delete their own images
CREATE POLICY "Users can delete own profile picture"
ON storage.objects FOR DELETE
TO authenticated
USING (
  bucket_id = 'profile-pictures' AND
  (storage.foldername(name))[1] = auth.uid()::text
);

-- Policy 4: Allow public viewing (needed for profile display)
CREATE POLICY "Public profile pictures are viewable"
ON storage.objects FOR SELECT
TO public
USING (bucket_id = 'profile-pictures');
```

4. Click **"Run"** to execute the SQL

5. Verify success message appears

---

## Step 3: Verify Setup

### Check Bucket Settings

1. Go to **Storage** → **profile-pictures** bucket
2. Verify "Public" badge is shown
3. Click bucket settings (gear icon) and confirm:
   - ✅ Public bucket is enabled
   - File size limit is appropriate

### Check RLS Policies

1. Go to **Authentication** → **Policies**
2. Find `storage.objects` table
3. Verify you see all 4 policies:
   - "Users can upload own profile picture" (INSERT)
   - "Users can update own profile picture" (UPDATE)
   - "Users can delete own profile picture" (DELETE)
   - "Public profile pictures are viewable" (SELECT)

---

## Step 4: Test Upload

### Manual Test in Supabase Dashboard

1. Go to **Storage** → **profile-pictures**
2. Click **"Upload file"**
3. Upload a test image
4. Verify it appears in the bucket
5. Click the image → Copy public URL
6. Paste URL in browser → Verify image displays

### Test from Application

1. Start your frontend: `cd frontend && npm run dev`
2. Sign in to the application
3. Navigate to Profile page
4. Click "Change Picture"
5. Upload an image
6. Verify upload completes successfully
7. Check Supabase Storage dashboard - image should appear in your user's folder

---

## File Structure

Images are stored with this structure:
```
profile-pictures/
  ├── {user-id-1}/
  │   ├── profile-1705158400.jpg
  │   └── profile-1705159500.jpg
  ├── {user-id-2}/
  │   └── profile-1705160600.png
  └── ...
```

**Format**: `{user_id}/profile-{timestamp}.{ext}`

**Benefits**:
- Each user has their own folder
- Timestamp prevents naming conflicts
- Easy to find and manage user images

---

## Troubleshooting

### Problem: "Policy violation" error during upload

**Cause**: RLS policies not applied or incorrect

**Solution**:
1. Go to SQL Editor
2. Re-run the policy SQL from Step 2
3. Check that user is authenticated (signed in)

---

### Problem: "Bucket not found" error

**Cause**: Bucket name mismatch

**Solution**:
1. Verify bucket is named exactly `profile-pictures`
2. Check `frontend/src/lib/storage.js` - bucket name should match
3. Restart frontend after changes

---

### Problem: Image uploads but can't view it

**Cause**: Bucket is not public

**Solution**:
1. Go to Storage → profile-pictures → Settings
2. Enable "Public bucket"
3. Re-run Policy 4 (SELECT policy) from Step 2

---

### Problem: "Storage quota exceeded"

**Cause**: Free tier limit reached (1GB)

**Solution**:
1. Upgrade Supabase plan, OR
2. Delete old unused images:
   - Go to Storage → profile-pictures
   - Select old files and delete

---

### Problem: Images don't compress properly

**Cause**: Browser canvas API issues

**Solution**:
1. Try different browser (Chrome recommended)
2. Check browser console for errors
3. Try smaller initial image (<5MB)

---

## Security Best Practices

### ✅ DO:
- Keep bucket public for image display
- Use RLS policies to restrict uploads
- Validate file types and sizes client-side
- Use unique filenames (timestamp-based)
- Clean up old/unused images periodically

### ❌ DON'T:
- Store sensitive documents in this bucket
- Allow uploads without authentication
- Skip file type validation
- Use predictable filenames
- Share service role key in frontend

---

## Next Steps

### Optional Enhancements:

1. **Image Optimization**:
   - Add Supabase Image Transformation
   - Automatically create thumbnails
   - Serve images via CDN

2. **Storage Management**:
   - Add cleanup job for old images
   - Implement storage usage dashboard
   - Set up automated backups

3. **Advanced Features**:
   - Multiple profile photos gallery
   - Image cropping before upload
   - AI-powered background removal

---

## Resources

- [Supabase Storage Documentation](https://supabase.com/docs/guides/storage)
- [RLS Policies Guide](https://supabase.com/docs/guides/auth/row-level-security)
- [Image Transformation](https://supabase.com/docs/guides/storage/serving/image-transformations)

---

## Quick Reference

### Environment Variables
```env
# Already configured in .env
VITE_SUPABASE_URL=https://liayecrnqlgkiiiltohy.supabase.co
VITE_SUPABASE_ANON_KEY=your-anon-key
```

### Bucket Configuration
- **Name**: `profile-pictures`
- **Public**: Yes
- **Max size**: 2MB (enforced client-side)
- **Allowed types**: image/jpeg, image/png, image/webp, image/gif

### API Usage
```javascript
import { uploadProfilePicture } from './lib/storage';

// Upload
const url = await uploadProfilePicture(file, userId);

// Use in database
await mentorAPI.updateMe({ profile_picture_url: url });
```

---

**Setup Complete!** 🎉

Your Supabase Storage is now ready for profile picture uploads. Users can upload images directly from their computer during onboarding or from their profile page.
