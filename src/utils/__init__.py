import logging
import sys
import os

# User data directory for logs, config, and data
def get_user_data_dir() -> str:
    """Returns the user data directory for the application."""
    return os.path.join(os.path.expanduser("~"), ".lumen-x")


def get_log_dir() -> str:
    """Returns the log directory."""
    log_dir = os.path.join(get_user_data_dir(), "logs")
    os.makedirs(log_dir, exist_ok=True)
    return log_dir


def setup_logging(level=logging.INFO, log_file=None):
    """Configures the logging system."""
    handlers = []
    
    # If no log file specified, use default in user directory
    if log_file is None:
        log_file = os.path.join(get_log_dir(), "app.log")
    
    # 如果指定了日志文件，添加文件处理器
    if log_file:
        # 确保日志目录存在
        log_dir = os.path.dirname(log_file)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
        
        file_handler = logging.FileHandler(log_file, mode='a', encoding='utf-8')
        file_handler.setFormatter(
            logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        )
        handlers.append(file_handler)
    
    # 添加控制台处理器（会被重定向到日志文件）
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    )
    handlers.append(console_handler)
    
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=handlers
    )


def get_logger(name):
    """Returns a logger with the specified name."""
    return logging.getLogger(name)

