import os
from PIL import Image

# --- НАСТРОЙКИ ---
INPUT_FOLDER = "input"  # Имя папки с оригиналами
OUTPUT_FOLDER = "output"  # Имя папки для результата
CROP_HEIGHT = 80  # Сколько пикселей отрезать снизу (подбери под свой лого)


# -----------------

def process_images():
    # Проверяем, существуют ли папки
    if not os.path.exists(INPUT_FOLDER):
        print(f"Ошибка: Папка '{INPUT_FOLDER}' не найдена!")
        return

    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)

    # Список расширений, которые мы ищем
    extensions = ('.jpg', '.jpeg', '.png', '.webp')

    files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(extensions)]

    if not files:
        print("В папке 'input' нет подходящих изображений.")
        return

    print(f"Найдено файлов: {len(files)}. Начинаю обработку...")

    for filename in files:
        input_path = os.path.join(INPUT_FOLDER, filename)
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        try:
            with Image.open(input_path) as img:
                width, height = img.size

                # Обрезаем только низ: (лево, верх, право, низ)
                # Оставляем ширину как есть, а высоту уменьшаем на CROP_HEIGHT
                area = (0, 0, width, height - CROP_HEIGHT)

                cropped_img = img.crop(area)

                # Сохраняем. Если это JPEG, ставим качество повыше
                if filename.lower().endswith(('.jpg', '.jpeg')):
                    cropped_img.save(output_path, quality=95, subsampling=0)
                else:
                    cropped_img.save(output_path)

                print(f"✔️ Обработан: {filename}")
        except Exception as e:
            print(f"❌ Ошибка в файле {filename}: {e}")

    print("\nГотово! Все чистые фото лежат в папке 'output'.")


if __name__ == "__main__":
    process_images()