from babel.dates import format_datetime


async def format_tasks(tasks):
    if not tasks:
        return "У вас нет задач."

    formatted_tasks = ""
    for task in tasks:
        formatted_date = format_datetime(task.date_created, "dd MMMM yyyy HH:mm", locale='ru_RU')

        formatted_tasks += f"Задача: {task.description}\n"
        formatted_tasks += f"Была создана: {formatted_date}\n"
        formatted_tasks += f"Удалить: /del_{task.id}\n\n"

    return formatted_tasks
