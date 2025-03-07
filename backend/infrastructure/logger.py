import structlog

def setup_logging():
    structlog.configure(
        processors=[
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.JSONRenderer()
        ]
    )

def get_logger(name):
    setup_logging()
    return structlog.get_logger(name)
