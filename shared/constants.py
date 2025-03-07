class NodeTypes:
    INPUT = 'input'
    PROCESSOR = 'processor'
    OUTPUT = 'output'

class EdgeTypes:
    DATA_FLOW = 'data_flow'
    CONTROL_FLOW = 'control_flow'

class MessageRoles:
    USER = 'user'
    ASSISTANT = 'assistant'
    SYSTEM = 'system'

class ExecutionStatus:
    PENDING = 'pending'
    RUNNING = 'running'
    SUCCESS = 'success'
    FAILED = 'failed'
