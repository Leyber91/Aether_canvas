// shared/constants.js

export const NodeTypes = Object.freeze({
    INPUT: 'input',
    PROCESSOR: 'processor',
    OUTPUT: 'output',
});

export const EdgeTypes = Object.freeze({
    DATA_FLOW: 'data_flow',
    CONTROL_FLOW: 'control_flow',
});

export const MessageRoles = Object.freeze({
    USER: 'user',
    ASSISTANT: 'assistant',
    SYSTEM: 'system',
});

export const API_ENDPOINTS = Object.freeze({
    GRAPHS: '/graphs',
    NODES: '/nodes',
    EXECUTIONS: 'executions',
});