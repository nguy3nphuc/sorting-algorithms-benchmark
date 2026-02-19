import numpy as np

def generate_data(filename="data"):
    n = 1_000_000
    all_arrays = []

    # --- 5 DÃY SỐ THỰC (FLOAT) ---
    # Dãy 1: Tăng dần
    all_arrays.append(np.sort(np.random.uniform(0, 1e6, n)))
    # Dãy 2: Giảm dần
    all_arrays.append(np.sort(np.random.uniform(0, 1e6, n))[::-1])
    # Dãy 3, 4, 5: Ngẫu nhiên
    for _ in range(3):
        all_arrays.append(np.random.uniform(0, 1e6, n))

    # --- 5 DÃY SỐ NGUYÊN (INT) ---
    # Dãy 6, 7, 8, 9, 10: Ngẫu nhiên (từ 0 đến 1 triệu)
    for _ in range(5):
        all_arrays.append(np.random.randint(0, 1_000_000, n))

    # Chuyển list thành một mảng lớn (Object array để chứa các mảng con)
    final_data = np.array(all_arrays, dtype=object)

    # Lưu file nhị phân
    np.save(filename, final_data)
    print(f"Đã tạo và lưu xong 10 dãy vào file: {filename}")

generate_data()