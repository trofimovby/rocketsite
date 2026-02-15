import os
import time
from carvekit.api.high import HiInterface

# --- НАСТРОЙКИ ---
INPUT_DIR = "input_images"
OUTPUT_DIR = "output_images"
EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.bmp'}


def main():
    # 1. Подготовка папок
    if not os.path.exists(INPUT_DIR):
        os.makedirs(INPUT_DIR)
        print(f"📁 Создана папка '{INPUT_DIR}'. Положи туда фото!")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 2. Поиск файлов
    files = [f for f in os.listdir(INPUT_DIR) if os.path.splitext(f)[1].lower() in EXTENSIONS]

    if not files:
        print(f"⚠️ Папка '{INPUT_DIR}' пуста. Добавь фото.")
        return

    print(f"🚀 Инициализация нейросети CarveKit... (первый запуск скачает ~150Мб)")

    # Загружаем модель (используем CPU, так как на Mac это надежнее всего)
    interface = HiInterface(object_type="object", batch_size_seg=1, batch_size_matting=1, device='cpu')

    start_time = time.time()

    for idx, filename in enumerate(files, 1):
        try:
            input_path = os.path.join(INPUT_DIR, filename)
            output_filename = f"{os.path.splitext(filename)[0]}.png"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            print(f"[{idx}/{len(files)}] Обработка: {filename}...")

            # Магия удаления фона
            images = interface([input_path])
            images[0].save(output_path)

        except Exception as e:
            print(f"❌ Ошибка с {filename}: {e}")

    elapsed = time.time() - start_time
    print(f"\n✅ Готово! Обработано за {elapsed:.2f} сек.")
    print(f"📂 Результаты здесь: {os.path.abspath(OUTPUT_DIR)}")


if __name__ == "__main__":
    main()