import { useState, useRef } from 'react';
import { useAuth } from '../contexts/AuthContext';
import { validateImageFile, compressImage, formatBytes } from '../lib/imageUtils';
import { uploadProfilePicture, deleteProfilePicture } from '../lib/storage';

/**
 * ImageUpload Component
 * Reusable component for uploading and managing profile pictures
 *
 * @param {string|null} currentImageUrl - Existing image URL
 * @param {Function} onUploadComplete - Callback when upload completes (receives URL)
 * @param {Function} onError - Callback when error occurs (receives error message)
 * @param {number} maxSizeMB - Maximum file size in MB (default: 2)
 * @param {number} maxDimensionPx - Maximum image dimension in pixels (default: 1920)
 */
const ImageUpload = ({
  currentImageUrl = null,
  onUploadComplete,
  onError,
  maxSizeMB = 2,
  maxDimensionPx = 1920
}) => {
  const { user } = useAuth();
  const fileInputRef = useRef(null);

  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [error, setError] = useState(null);
  const [compressing, setCompressing] = useState(false);
  const [compressionInfo, setCompressionInfo] = useState(null);

  /**
   * Handle file selection
   */
  const handleFileSelect = async (event) => {
    const file = event.target.files?.[0];

    if (!file) {
      return;
    }

    // Reset states
    setError(null);
    setCompressionInfo(null);

    // Validate file
    const validation = validateImageFile(file, maxSizeMB);
    if (!validation.valid) {
      setError(validation.error);
      onError?.(validation.error);
      return;
    }

    // Set selected file and create preview
    setSelectedFile(file);
    const preview = URL.createObjectURL(file);
    setPreviewUrl(preview);
  };

  /**
   * Handle upload
   */
  const handleUpload = async () => {
    if (!selectedFile || !user) {
      return;
    }

    setError(null);
    setUploading(true);
    setUploadProgress(0);

    try {
      // Compress image if needed
      setCompressing(true);
      const compressionResult = await compressImage(selectedFile, maxSizeMB, maxDimensionPx);
      setCompressing(false);

      if (compressionResult.compressed) {
        setCompressionInfo({
          original: compressionResult.originalSize,
          compressed: compressionResult.newSize
        });
      }

      // Upload to Supabase Storage
      setUploadProgress(50); // Show progress
      const publicUrl = await uploadProfilePicture(
        compressionResult.file,
        user.id,
        (progress) => {
          // Map progress to 50-100% range (since compression was 0-50%)
          setUploadProgress(50 + (progress / 2));
        }
      );

      setUploadProgress(100);

      // Call success callback
      onUploadComplete?.(publicUrl);

      // Reset state
      setTimeout(() => {
        resetState();
      }, 500);

    } catch (err) {
      console.error('Upload error:', err);
      const errorMessage = err.message || 'Failed to upload image';
      setError(errorMessage);
      onError?.(errorMessage);
    } finally {
      setUploading(false);
      setCompressing(false);
    }
  };

  /**
   * Handle remove current image
   */
  const handleRemove = async () => {
    if (!currentImageUrl) {
      return;
    }

    const confirmed = window.confirm('Are you sure you want to remove your profile picture?');
    if (!confirmed) {
      return;
    }

    try {
      await deleteProfilePicture(currentImageUrl);
      onUploadComplete?.(null);
    } catch (err) {
      console.error('Delete error:', err);
      const errorMessage = 'Failed to delete image';
      setError(errorMessage);
      onError?.(errorMessage);
    }
  };

  /**
   * Reset component state
   */
  const resetState = () => {
    setSelectedFile(null);
    if (previewUrl) {
      URL.revokeObjectURL(previewUrl);
    }
    setPreviewUrl(null);
    setUploadProgress(0);
    setError(null);
    setCompressionInfo(null);
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  /**
   * Handle cancel
   */
  const handleCancel = () => {
    resetState();
  };

  return (
    <div style={{ marginTop: '0.5rem' }}>
      {/* Hidden file input */}
      <input
        ref={fileInputRef}
        type="file"
        accept="image/jpeg,image/jpg,image/png,image/webp,image/gif"
        onChange={handleFileSelect}
        style={{ display: 'none' }}
      />

      {/* Current or preview image */}
      {(previewUrl || currentImageUrl) && (
        <div style={{ marginBottom: '1rem', textAlign: 'center' }}>
          <img
            src={previewUrl || currentImageUrl}
            alt="Profile preview"
            style={{
              maxWidth: '100%',
              maxHeight: '300px',
              borderRadius: '8px',
              border: '2px solid #ddd',
              objectFit: 'cover'
            }}
          />
        </div>
      )}

      {/* File info */}
      {selectedFile && !uploading && (
        <div style={{ marginBottom: '1rem', fontSize: '0.9rem', color: '#666' }}>
          <div>Selected: {selectedFile.name}</div>
          <div>Size: {formatBytes(selectedFile.size)}</div>
          {compressionInfo && (
            <div style={{ color: '#28a745' }}>
              Compressed: {formatBytes(compressionInfo.original)} → {formatBytes(compressionInfo.compressed)}
            </div>
          )}
        </div>
      )}

      {/* Compression indicator */}
      {compressing && (
        <div style={{ marginBottom: '1rem', color: '#007bff', fontSize: '0.9rem' }}>
          <div>Compressing image...</div>
          <div style={{
            width: '100%',
            height: '4px',
            backgroundColor: '#e0e0e0',
            borderRadius: '2px',
            overflow: 'hidden',
            marginTop: '0.5rem'
          }}>
            <div style={{
              width: '100%',
              height: '100%',
              backgroundColor: '#007bff',
              animation: 'loading 1.5s ease-in-out infinite'
            }} />
          </div>
        </div>
      )}

      {/* Upload progress */}
      {uploading && !compressing && (
        <div style={{ marginBottom: '1rem' }}>
          <div style={{ fontSize: '0.9rem', marginBottom: '0.5rem', color: '#007bff' }}>
            Uploading... {Math.round(uploadProgress)}%
          </div>
          <div style={{
            width: '100%',
            height: '8px',
            backgroundColor: '#e0e0e0',
            borderRadius: '4px',
            overflow: 'hidden'
          }}>
            <div style={{
              width: `${uploadProgress}%`,
              height: '100%',
              backgroundColor: '#28a745',
              transition: 'width 0.3s ease'
            }} />
          </div>
        </div>
      )}

      {/* Error message */}
      {error && (
        <div style={{
          padding: '0.75rem',
          marginBottom: '1rem',
          backgroundColor: '#f8d7da',
          color: '#721c24',
          border: '1px solid #f5c6cb',
          borderRadius: '4px',
          fontSize: '0.9rem'
        }}>
          {error}
        </div>
      )}

      {/* Action buttons */}
      <div style={{ display: 'flex', gap: '0.5rem', flexWrap: 'wrap' }}>
        {!selectedFile && !uploading && (
          <>
            <button
              type="button"
              onClick={() => fileInputRef.current?.click()}
              style={{
                padding: '0.5rem 1rem',
                fontSize: '0.9rem',
                backgroundColor: '#007bff',
                color: 'white',
                border: 'none',
                borderRadius: '4px',
                cursor: 'pointer'
              }}
            >
              Choose Image
            </button>

            {currentImageUrl && (
              <button
                type="button"
                onClick={handleRemove}
                style={{
                  padding: '0.5rem 1rem',
                  fontSize: '0.9rem',
                  backgroundColor: '#dc3545',
                  color: 'white',
                  border: 'none',
                  borderRadius: '4px',
                  cursor: 'pointer'
                }}
              >
                Remove
              </button>
            )}
          </>
        )}

        {selectedFile && !uploading && (
          <>
            <button
              type="button"
              onClick={handleUpload}
              disabled={uploading}
              style={{
                padding: '0.5rem 1rem',
                fontSize: '0.9rem',
                backgroundColor: '#28a745',
                color: 'white',
                border: 'none',
                borderRadius: '4px',
                cursor: uploading ? 'not-allowed' : 'pointer',
                opacity: uploading ? 0.6 : 1
              }}
            >
              Upload
            </button>

            <button
              type="button"
              onClick={handleCancel}
              disabled={uploading}
              style={{
                padding: '0.5rem 1rem',
                fontSize: '0.9rem',
                backgroundColor: '#6c757d',
                color: 'white',
                border: 'none',
                borderRadius: '4px',
                cursor: uploading ? 'not-allowed' : 'pointer',
                opacity: uploading ? 0.6 : 1
              }}
            >
              Cancel
            </button>
          </>
        )}
      </div>

      {/* Loading animation CSS */}
      <style>{`
        @keyframes loading {
          0% { transform: translateX(-100%); }
          50% { transform: translateX(100%); }
          100% { transform: translateX(-100%); }
        }
      `}</style>
    </div>
  );
};

export default ImageUpload;
