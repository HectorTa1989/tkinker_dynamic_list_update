import tkinter as tk
from tkinter import ttk

# Hàm tính toán dựa trên giá trị của dropdown1
def compute_dropdown2_options(value):
    # Thực hiện tính toán dựa trên giá trị của dropdown1
    # Ví dụ: return một list các options mới
    if value == "Option 1":
        return ["Option 1.1", "Option 1.2", "Option 1.3"]
    elif value == "Option 2":
        return ["Option 2.1", "Option 2.2"]
    elif value == "Option 3":
        return ["Option 3.1", "Option 3.2", "Option 3.3", "Option 3.4"]
    else:
        return []

# Hàm cập nhật nội dung của dropdown2 khi dropdown1 thay đổi
def update_dropdown2(*args):
    value = dropdown1.get()
    options = compute_dropdown2_options(value)
    dropdown2['values'] = options

#  create tkinter window
root = tk.Tk()
root.title("Dropdown Lists")

# create dropdown1
dropdown1_label = ttk.Label(root, text="Dropdown 1:")
dropdown1_label.grid(row=0, column=0)
dropdown1 = ttk.Combobox(root, state="readonly", values=["Option 1", "Option 2", "Option 3"])
dropdown1.grid(row=0, column=1)
dropdown1.current(0)  # Thiết lập giá trị mặc định cho dropdown1
dropdown1.bind("<<ComboboxSelected>>", update_dropdown2)

# create dropdown2
dropdown2_label = ttk.Label(root, text="Dropdown 2:")
dropdown2_label.grid(row=1, column=0)
dropdown2 = ttk.Combobox(root, state="readonly")
dropdown2.grid(row=1, column=1)

# Gọi hàm update_dropdown2() để cập nhật nội dung cho dropdown2 ban đầu
update_dropdown2()

# Chạy ứng dụng
root.mainloop()
