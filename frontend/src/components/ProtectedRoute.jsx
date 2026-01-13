import { Navigate } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext';

/**
 * ProtectedRoute component that requires authentication
 * Redirects to sign-in page if user is not authenticated
 */
export const ProtectedRoute = ({ children, requireProfile = false }) => {
  const { user, userProfile, loading } = useAuth();

  // Show loading state while checking authentication
  if (loading) {
    return (
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh'
      }}>
        <p>Loading...</p>
      </div>
    );
  }

  // Redirect to sign-in if not authenticated
  if (!user) {
    return <Navigate to="/signin" replace />;
  }

  // If profile is required but doesn't exist, redirect to signup
  if (requireProfile && !userProfile) {
    return <Navigate to="/signup" replace />;
  }

  // User is authenticated, render children
  return children;
};

/**
 * PublicRoute component that redirects authenticated users away
 * Useful for signin/signup pages
 */
export const PublicRoute = ({ children, redirectTo = '/app/home' }) => {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div style={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        height: '100vh'
      }}>
        <p>Loading...</p>
      </div>
    );
  }

  // If authenticated, redirect to app
  if (user) {
    return <Navigate to={redirectTo} replace />;
  }

  // Not authenticated, show public page
  return children;
};
