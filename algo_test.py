import numpy as np
import my_sorts
import time
import sys
import matplotlib.pyplot as plt

sys.setrecursionlimit(2000000)

def benchmark_sorting():
    # 1. Load toàn bộ bộ dữ liệu
    print("Đang load dữ liệu...")
    data = np.load("data.npy", allow_pickle=True)
    
    # Danh sách các thuật toán ông muốn test
    # Lưu dưới dạng: (tên_hàm, hàm_thực_thi)
    # Ví dụ tôi có hàm my_quick_sort và np.sort (để so sánh với hàng xịn của thư viện)
    algorithms = [
        ("Numpy Built-in Sort", np.sort),
        ("My Quick Sort", my_sorts.quick_sort), 
        ("My Merge Sort", my_sorts.merge_sort),
        ("My Heap Sort", my_sorts.heap_sort),
    ]

    labels = [
        "Thực - Tăng dần", "Thực - Giảm dần", "Thực - Ngẫu nhiên 1", 
        "Thực - Ngẫu nhiên 2", "Thực - Ngẫu nhiên 3", "Nguyên - Ngẫu nhiên 1",
        "Nguyên - Ngẫu nhiên 2", "Nguyên - Ngẫu nhiên 3", "Nguyên - Ngẫu nhiên 4", "Nguyên - Ngẫu nhiên 5"
    ]

    results_dict = {name: [] for name, _ in algorithms}

    for algo_name, algo_func in algorithms:
        print(f"\nĐANG TEST: {algo_name}")
        
        for i in range(len(data)):
            # QUAN TRỌNG: Phải copy mảng để tránh việc dãy sau khi sort xong 
            # sẽ bị lưu đè vào file gốc hoặc làm sai lệch kết quả lần test sau
            arr_test = data[i].copy()
            
            start_time = time.time()
            algo_func(arr_test) # Chạy thuật toán
            end_time = time.time()
            
            duration = end_time - start_time
            results_dict[algo_name].append(duration)
            print(f"Dãy {i+1} ({labels[i]}): {duration:.5f} giây")
    
    # 3. VẼ BIỂU ĐỒ TỰ ĐỘNG
    print("\nĐang vẽ biểu đồ...")
    num_algos = len(algorithms)
    num_datasets = len(labels)
    
    bar_width = 0.2
    index = np.arange(num_datasets)
    
    plt.figure(figsize=(15, 8))
    
    # Màu sắc tự động cho các cột
    colors = plt.cm.get_cmap('viridis', num_algos)

    for i, (name, _) in enumerate(algorithms):
        plt.bar(index + i * bar_width, results_dict[name], bar_width, 
                label=name, color=colors(i))

    plt.xlabel("Loại Dữ liệu", fontsize=12)
    plt.ylabel("Thời gian chạy (giây)", fontsize=12)
    plt.title("Kết quả Benchmark Thuật toán Sắp xếp (Dữ liệu thực tế)", fontsize=14)
    plt.xticks(index + bar_width * (num_algos - 1) / 2, labels, rotation=30)
    plt.legend()
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    
    plt.tight_layout()
    
    # Lưu ảnh và hiển thị
    plt.savefig("benchmark_result.png")
    print("✅ Đã lưu biểu đồ vào file 'benchmark_result.png'")
    plt.show()

if __name__ == "__main__":
    benchmark_sorting()