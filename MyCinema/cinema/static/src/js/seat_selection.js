// File: seat_selection.js

let selectedSeats = [];
let totalPrice = 0;
let seatDetails = {}; // Object để lưu trữ loại ghế và tên ghế

// Hàm để cập nhật ghế được chọn
function selectSeat(button) {
    const seatName = button.getAttribute("data-seat-name");
    const seatPrice = parseFloat(button.getAttribute("data-seat-price"));
    const seatType = button.getAttribute("data-seat-type");
    // Kiểm tra xem ghế đã được chọn chưa
    const index = selectedSeats.indexOf(seatName);

    if (index === -1) {
        // Thêm ghế nếu chưa được chọn
        // Lưu lại màu nền ban đầu nếu chưa lưu
        if (!button.getAttribute("data-original-color")) {
            const originalColor = window.getComputedStyle(button).backgroundColor;
            button.setAttribute("data-original-color", originalColor);
        }
        selectedSeats.push(seatName);
        totalPrice += seatPrice;
        button.style.backgroundColor = "green"; // Đổi màu ghế khi đã chọn

        // Thêm thông tin ghế vào object seatDetails
        if (!seatDetails[seatType]) {
            seatDetails[seatType] = {seats: [], price: seatPrice};
        }
        seatDetails[seatType].seats.push(seatName);
    } else {
        // Bỏ chọn ghế nếu đã có trong danh sách
        selectedSeats.splice(index, 1);
        totalPrice -= seatPrice;
        button.style.backgroundColor = button.getAttribute("data-original-color"); // Đặt lại màu ban đầu của ghế
        // Xóa ghế khỏi seatDetails
        seatDetails[seatType].seats.splice(seatDetails[seatType].seats.indexOf(seatName), 1);
        if (seatDetails[seatType].seats.length === 0) {
            delete seatDetails[seatType]; // Xóa loại ghế nếu không còn ghế
        }
    }

    // Cập nhật danh sách ghế hiển thị
    displaySelectedSeats();
    // Hiển thị tổng tiền nếu có ghế được chọn, ngược lại hiển thị thông báo
    if (totalPrice > 0) {
        document.getElementById("totalPriceSection").style.display = "block";  // Hiển thị phần tổng tiền và nút mua
        document.getElementById("noSeatMessage").style.display = "none";  // Ẩn thông báo
        document.getElementById("totalPrice").innerHTML = totalPrice.toLocaleString('vi-VN') + ' VND'; // Cập nhật tổng tiền
    } else {
        document.getElementById("totalPriceSection").style.display = "none";  // Ẩn phần tổng tiền và nút mua
        document.getElementById("noSeatMessage").style.display = "block";  // Hiển thị thông báo
    }

    // Hàm hiển thị ghế đã chọn theo định dạng yêu cầu
    function displaySelectedSeats() {
        const seatDisplay = document.getElementById("selectedSeats");
        seatDisplay.innerHTML = ''; // Xóa nội dung cũ

        const seatEntries = Object.entries(seatDetails);
        const totalEntries = seatEntries.length;

        seatEntries.forEach(([seatType, data], index) => {
            if (data.seats.length > 0) {
                const seatCount = data.seats.length;
                const seatNames = data.seats.join(", ");
                const seatPrice = data.price * seatCount;

                const seatInfo = `${seatCount} x ghế ${seatType} ${seatNames} ${seatPrice.toLocaleString('vi-VN')} VND`;
                seatDisplay.innerHTML += `<p>${seatInfo}</p>`;

                // Thêm thẻ <hr> giữa các dòng, không thêm sau dòng cuối cùng
                if (index < totalEntries - 1) {
                    seatDisplay.innerHTML += `<hr style="border-style: dashed; border-width: 1px;">`; // Thêm thẻ <hr> giữa các dòng
                }
            }
        });
    }
}
