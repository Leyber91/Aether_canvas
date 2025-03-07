// shared/error_utils.js

export const createError = (code, message, context = {}) => ({
    code,
    message,
    context,
    timestamp: new Date().toISOString(),
});

export const isNetworkError = (error) => error.message && error.message.includes('Network');

export const isAuthError = (error) => error.response?.status === 401;

export const formatErrorMessage = (error) =>
    error.message || 'An unknown error occurred.';