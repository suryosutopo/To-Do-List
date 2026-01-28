import os
import json
from datetime import datetime

class TodoList:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        """Muat tugas dari file JSON"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_tasks(self):
        """Simpan tugas ke file JSON"""
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=2)
    
    def add_task(self, description):
        """Tambah tugas baru"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Tugas '{description}' berhasil ditambahkan!")
    
    def view_tasks(self):
        """Tampilkan semua tugas"""
        if not self.tasks:
            print("\n📭 Tidak ada tugas. Tambahkan tugas baru!")
            return
        
        print("\n" + "="*60)
        print(f"{'ID':<5} {'Status':<10} {'Tugas':<35} {'Dibuat':<10}")
        print("="*60)
        
        for task in self.tasks:
            status = "✓ Selesai" if task['completed'] else "⏳ Aktif"
            print(f"{task['id']:<5} {status:<10} {task['description']:<35} {task['created_at']:<10}")
        
        print("="*60 + "\n")
    
    def mark_completed(self, task_id):
        """Tandai tugas sebagai selesai"""
        for task in self.tasks:
            if task['id'] == task_id:
                task['completed'] = True
                self.save_tasks()
                print(f"✓ Tugas '{task['description']}' ditandai selesai!")
                return
        print("❌ Tugas tidak ditemukan!")
    
    def delete_task(self, task_id):
        """Hapus tugas"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                description = task['description']
                self.tasks.pop(i)
                self.save_tasks()
                print(f"✓ Tugas '{description}' berhasil dihapus!")
                return
        print("❌ Tugas tidak ditemukan!")
    
    def get_statistics(self):
        """Tampilkan statistik tugas"""
        total = len(self.tasks)
        completed = sum(1 for task in self.tasks if task['completed'])
        active = total - completed
        
        print("\n" + "="*40)
        print("📊 STATISTIK TUGAS")
        print("="*40)
        print(f"Total Tugas: {total}")
        print(f"Selesai: {completed}")
        print(f"Aktif: {active}")
        if total > 0:
            percentage = (completed / total) * 100
            print(f"Progress: {percentage:.1f}%")
        print("="*40 + "\n")

def main():
    todo = TodoList()
    
    while True:
        print("\n" + "="*40)
        print("📝 APLIKASI TO-DO LIST")
        print("="*40)
        print("1. Lihat Semua Tugas")
        print("2. Tambah Tugas Baru")
        print("3. Tandai Selesai")
        print("4. Hapus Tugas")
        print("5. Lihat Statistik")
        print("6. Keluar")
        print("="*40)
        
        choice = input("Pilih menu (1-6): ").strip()
        
        if choice == '1':
            todo.view_tasks()
        
        elif choice == '2':
            description = input("Masukkan deskripsi tugas: ").strip()
            if description:
                todo.add_task(description)
            else:
                print("❌ Deskripsi tugas tidak boleh kosong!")
        
        elif choice == '3':
            todo.view_tasks()
            try:
                task_id = int(input("Masukkan ID tugas yang selesai: ").strip())
                todo.mark_completed(task_id)
            except ValueError:
                print("❌ ID harus berupa angka!")
        
        elif choice == '4':
            todo.view_tasks()
            try:
                task_id = int(input("Masukkan ID tugas yang akan dihapus: ").strip())
                todo.delete_task(task_id)
            except ValueError:
                print("❌ ID harus berupa angka!")
        
        elif choice == '5':
            todo.get_statistics()
        
        elif choice == '6':
            print("👋 Terima kasih! Sampai jumpa lagi!")
            break
        
        else:
            print("❌ Pilihan tidak valid! Silakan pilih 1-6.")

if __name__ == "__main__":
    main
