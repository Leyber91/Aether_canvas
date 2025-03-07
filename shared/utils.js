export const debounce = (func, wait) => {
    let timeout;
    return (...args) => {
        clearTimeout(timeout);
        timeout = setTimeout(() => func.apply(this, args), wait);
    };
};

export const deepClone = (obj) => JSON.parse(JSON.stringify(obj));

export const formatDate = (date, locale = 'en-US', options = {}) => {
    const formatter = new Intl.DateTimeFormat('en-US', options);
    return formatter.format(new Date(date));
};

export const validateSchema = (data, schema) => {
    const result = schema.validate(data);
    return result.error ? result.error.details : null;
};
