import pandas as pd
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import inspect, select
from src.repository.database import get_session, initialize_database, engine
from src.repository.models import Base
import os


async def export_all_tables_to_excel():
    # Определяем текущую директорию, где находится скрипт
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Папка для сохранения Excel-файлов (на уровень выше)
    output_dir = os.path.join(script_dir, "exported_data")
    os.makedirs(output_dir, exist_ok=True)

    # Для получения метаданных используем асинхронное соединение
    async with engine.connect() as conn:
        # Используем run_sync для получения инспектора
        table_names = await conn.run_sync(
            lambda sync_conn: inspect(sync_conn).get_table_names()
        )

    # Инициализируем асинхронную сессию для выполнения запросов
    async with get_session() as session:
        for table_name in table_names:
            # Получаем таблицу из метаданных
            table = Base.metadata.tables.get(table_name)

            if table is not None:
                # Асинхронно выполняем запрос для получения всех строк
                result = await session.execute(select(table))
                rows = result.fetchall()

                # Преобразуем строки результата в словари
                data_dicts = [dict(row._mapping) for row in rows]

                # Конвертируем данные в DataFrame
                df = pd.DataFrame(data_dicts)

                # Путь к Excel-файлу (на уровень выше)
                output_path = os.path.join(output_dir, f"{table_name}.xlsx")

                # Сохраняем в Excel
                df.to_excel(output_path, index=False, engine="openpyxl")
