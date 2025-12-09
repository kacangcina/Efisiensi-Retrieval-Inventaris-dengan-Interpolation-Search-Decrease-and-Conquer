import time
import random
import sys

# Meningkatkan batas rekursi (opsional, karena implementasi di bawah bersifat iteratif)
sys.setrecursionlimit(2000)

class InventoryItem:
    """
    Merepresentasikan item fisik di gudang E-commerce.
    """
    def __init__(self, sku_id, product_name, aisle_location):
        self.sku_id = sku_id            # Key untuk pencarian (Integer)
        self.product_name = product_name
        self.aisle_location = aisle_location # Metadata lokasi

    def __repr__(self):
        # PERBAIKAN: Mengembalikan string representasi yang valid
        return f"<SKU: {self.sku_id} | {self.product_name}>"

def interpolation_search(arr, x):
    
    # Implementasi Algoritma Interpolation Search.
    # Strategi: Decrease and Conquer (Variable-Size-Decrease).
    # Complexity: O(log(log n)) pada data uniform, O(n) worst case.
    lo = 0
    hi = len(arr) - 1
    iterations = 0
    
    # Loop utama: Pastikan lo <= hi dan x berada dalam rentang nilai array
    while lo <= hi and x >= arr[lo].sku_id and x <= arr[hi].sku_id:
        iterations += 1
        
        # Hitung posisi probe menggunakan rumus interpolasi
        numerator = float(hi - lo)
        denominator = arr[hi].sku_id - arr[lo].sku_id
        
        # Penanganan edge case: pembagian dengan nol (jika elemen lo dan hi sama)
        if denominator == 0:
            if arr[lo].sku_id == x:
                return lo, iterations
            else:
                return -1, iterations
                
        # Rumus Inti Decrease and Conquer
        # Estimasi posisi relatif x terhadap rentang nilai
        pos = lo + int((numerator / denominator) * (x - arr[lo].sku_id))
        
        # Verifikasi temuan
        if arr[pos].sku_id == x:
            return pos, iterations
        
        # Logika reduksi masalah (Decrease)
        if arr[pos].sku_id < x:
            # x berada di bagian kanan (Upper Part)
            lo = pos + 1
        else:
            # x berada di bagian kiri (Lower Part)
            hi = pos - 1
            
    return -1, iterations

def binary_search(arr, x):

    # Implementasi Binary Search sebagai pembanding.
    # Strategi: Decrease and Conquer (Decrease-by-half).
    # Complexity: O(log n)
    lo = 0
    hi = len(arr) - 1
    iterations = 0
    
    while lo <= hi:
        iterations += 1
        mid = (lo + hi) // 2
        
        if arr[mid].sku_id == x:
            return mid, iterations
        elif arr[mid].sku_id < x:
            lo = mid + 1
        else:
            hi = mid - 1
            
    return -1, iterations

def linear_search(arr, x):

    # Implementasi Linear Search sebagai baseline.
    # Complexity: O(n)
    iterations = 0
    for i in range(len(arr)):
        iterations += 1
        if arr[i].sku_id == x:
            return i, iterations
    return -1, iterations

# --- Modul Pengujian (Driver Code) ---
def run_experiment():
    print("=== MULAI EKSPERIMEN PENCARIAN INVENTARIS ===")
    
    # PERBAIKAN: Mengisi list ukuran data untuk pengujian
    DATA_SIZES = [1000, 5000, 10000, 50000]
    
    for size in DATA_SIZES:
        print(f"\n--- Ukuran Dataset: {size} Items ---")
        
        # 1. Generate Data Seragam (Uniform Distribution)
        # PERBAIKAN: Inisialisasi list kosong
        data = [] 
        current_sku = 1000000 # Start SKU ID
        
        for i in range(size):
            # step kecil (1-3) membuat data terdistribusi cukup seragam (bagus untuk Interpolation)
            step = random.randint(1, 3) 
            current_sku += step
            data.append(InventoryItem(current_sku, f"Prod_{i}", f"Rack_{i%100}"))
            
        # Pilih target pencarian di dekat akhir array 
        # (Worst case untuk Linear, biasanya Best case untuk Interpolation jika uniform)
        target_idx = size - 100 
        target_sku = data[target_idx].sku_id
        
        # --- Eksekusi Linear Search ---
        start = time.time_ns()
        _, iter_lin = linear_search(data, target_sku)
        time_lin = time.time_ns() - start
        
        # --- Eksekusi Binary Search ---
        start = time.time_ns()
        _, iter_bin = binary_search(data, target_sku)
        time_bin = time.time_ns() - start
        
        # --- Eksekusi Interpolation Search ---
        start = time.time_ns()
        _, iter_inter = interpolation_search(data, target_sku)
        time_inter = time.time_ns() - start
        
        # Output Hasil (Format ns = nanoseconds)
        print(f"Linear Search        | Waktu: {time_lin:10} ns | Iterasi: {iter_lin}")
        print(f"Binary Search        | Waktu: {time_bin:10} ns | Iterasi: {iter_bin}")
        print(f"Interpolation Search | Waktu: {time_inter:10} ns | Iterasi: {iter_inter}")
        
if __name__ == "__main__":
    run_experiment()
