Trong ví dụ này, chúng ta sử dụng ttk.Combobox để tạo dropdown list. Hàm compute_dropdown2_options tính toán nội dung của dropdown thứ hai dựa trên giá trị của dropdown thứ nhất. Hàm update_dropdown2 được gọi mỗi khi giá trị của dropdown thứ nhất thay đổi để cập nhật nội dung của dropdown thứ hai.

**Thay đổi dynamic và gọi hàm để tạo list cho dropdown 2:**

Khi người dùng thay đổi lựa chọn trong dropdown thứ nhất (dropdown1), sự kiện <<ComboboxSelected>> được kích hoạt. Chúng ta đã gán sự kiện này với hàm update_dropdown2() bằng cách sử dụng dropdown1.bind("<<ComboboxSelected>>", update_dropdown2).

Hàm update_dropdown2() được gọi mỗi khi dropdown thứ nhất thay đổi.

Trong hàm update_dropdown2(), chúng ta lấy giá trị hiện tại của dropdown thứ nhất (dropdown1.get()) và sử dụng nó để gọi hàm compute_dropdown2_options() để tính toán nội dung cho dropdown thứ hai (dropdown2). Sau đó, chúng ta cập nhật nội dung của dropdown thứ hai bằng cách thiết lập dropdown2['values'] thành danh sách các tùy chọn mới.

**Cập nhật nội dung của dropdown 2:**

Trong hàm update_dropdown2(), chúng ta cập nhật nội dung của dropdown thứ hai (dropdown2) bằng cách thiết lập dropdown2['values'] thành danh sách các tùy chọn mới, được tính toán từ hàm compute_dropdown2_options().

Như vậy, bằng cách gọi hàm update_dropdown2() khi dropdown thứ nhất thay đổi, chúng ta đảm bảo rằng nội dung của dropdown thứ hai sẽ được cập nhật dynamic dựa trên lựa chọn của dropdown thứ nhất.

