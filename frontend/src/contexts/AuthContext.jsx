import { createContext, useContext, useEffect, useState } from 'react';
import { supabase } from '../lib/supabase';
import { userAPI } from '../lib/api';

const AuthContext = createContext({});

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [userProfile, setUserProfile] = useState(null);
  const [session, setSession] = useState(null);
  const [loading, setLoading] = useState(true);

  // Fetch user profile from backend
  const fetchUserProfile = async () => {
    try {
      const profile = await userAPI.getMe();
      setUserProfile(profile);
      return profile;
    } catch (error) {
      // If profile doesn't exist (404), that's okay - user needs to complete signup
      if (error.status === 404) {
        console.log('User profile not found - needs to complete signup');
        setUserProfile(null);
        return null;
      }
      console.error('Error fetching user profile:', error);
      setUserProfile(null);
      return null;
    }
  };

  // Initialize auth state
  useEffect(() => {
    // Get initial session
    supabase.auth.getSession().then(({ data: { session } }) => {
      setSession(session);
      setUser(session?.user ?? null);

      // If we have a session, fetch the user profile
      if (session) {
        fetchUserProfile().finally(() => setLoading(false));
      } else {
        setLoading(false);
      }
    });

    // Listen for auth changes
    const {
      data: { subscription },
    } = supabase.auth.onAuthStateChange((_event, session) => {
      setSession(session);
      setUser(session?.user ?? null);

      if (session) {
        fetchUserProfile();
      } else {
        setUserProfile(null);
      }
    });

    return () => subscription.unsubscribe();
  }, []);

  // Sign in with email/password
  const signInWithEmail = async (email, password) => {
    const { data, error } = await supabase.auth.signInWithPassword({
      email,
      password,
    });

    if (error) throw error;

    // Fetch user profile after successful sign in
    if (data.session) {
      await fetchUserProfile();
    }

    return data;
  };

  // Sign up with email/password
  const signUpWithEmail = async (email, password, metadata = {}) => {
    const { data, error } = await supabase.auth.signUp({
      email,
      password,
      options: {
        data: metadata,
      },
    });

    if (error) throw error;
    return data;
  };

  // Sign in with OAuth provider (LinkedIn)
  const signInWithOAuth = async (provider, options = {}) => {
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider,
      options: {
        redirectTo: `${window.location.origin}/signup`,
        ...options,
      },
    });

    if (error) throw error;
    return data;
  };

  // Sign out
  const signOut = async () => {
    const { error } = await supabase.auth.signOut();
    if (error) throw error;

    setUser(null);
    setUserProfile(null);
    setSession(null);

    // Clear any localStorage data
    localStorage.clear();
  };

  // Refresh user profile (call after updating profile)
  const refreshProfile = async () => {
    return await fetchUserProfile();
  };

  const value = {
    user,
    userProfile,
    session,
    loading,
    signInWithEmail,
    signUpWithEmail,
    signInWithOAuth,
    signOut,
    refreshProfile,
  };

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
};
