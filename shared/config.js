// shared/config.js

const config = {
    environment: process.env.REACT_APP_ENV || 'development',
    apiBaseUrl: process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api',
    websocketUrl: process.env.REACT_APP_WEBSOCKET_URL || 'ws://localhost:8000/ws',
    debugMode: process.env.DEBUG_MODE === 'true',
};

export const getConfig = (key, defaultValue = null) => config[key] ?? defaultValue;

export const isFeatureEnabled = (featureKey) => {
    const features = {
        experimentalUI: false,
        detailedLogging: config.debugMode,
    };
    return features[featureKey] || false;
};

export const getEnvironment = () => process.env.NODE_ENV || config.environment;

