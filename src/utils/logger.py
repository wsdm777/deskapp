import logging


def setup_logger(name="my_logger", log_file="app.log", level=logging.DEBUG):
    # Создаём обработчики для вывода
    handler = logging.FileHandler(log_file)
    handler.setLevel(level)

    # Создаём форматтер для логов
    formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] --- %(message)s (%(filename)s:%(lineno)s)"
    )
    handler.setFormatter(formatter)

    # Создаём логгер
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
