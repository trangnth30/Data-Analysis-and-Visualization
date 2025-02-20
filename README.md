# Khám Phá Dữ Liệu Bán Hàng Của Doanh Nghiệp Chuyên Nhận Order

## Thành viên thực hiện

### **Giảng viên hướng dẫn**
- **Th.S Nguyễn Thanh Sơn**

### **Nhóm sinh viên thực hiện**
- **Nguyễn Diệu Phương**
- **Nguyễn Thị Mai Trinh**
- **Nguyễn Thị Huyền Trang**

## Giới thiệu

Ngày nay, hình thức mua hàng hộ từ nước ngoài ngày càng trở nên phổ biến. Tuy nhiên, không chỉ đơn thuần là dịch vụ mua hàng, doanh nghiệp ngày càng quan tâm đến việc **hiểu rõ thị trường, dự đoán tiềm năng sản phẩm** và **đáp ứng nhu cầu của khách hàng** một cách tốt nhất.

Dự án này tập trung vào việc **phân tích và khám phá dữ liệu bán hàng** của một doanh nghiệp chuyên nhận order hàng từ nước ngoài. Bằng cách thu thập, làm sạch, phân tích dữ liệu và xây dựng mô hình dự đoán, nhóm đã tiến hành kiểm tra tính khả thi của việc áp dụng các mô hình học máy trong **dự báo doanh thu và xu hướng mua sắm**.

## Mục tiêu của dự án

- **Khám phá bộ dữ liệu bán hàng** của một doanh nghiệp nhỏ chuyên nhận order hàng hiệu.
- **Phân tích và trực quan hóa dữ liệu** để tìm ra xu hướng quan trọng.
- **Xây dựng mô hình dự đoán doanh thu**, giúp doanh nghiệp lập kế hoạch kinh doanh hiệu quả hơn.
- **Sử dụng các mô hình Machine Learning phổ biến** như **Linear Regression, Ridge Regression, Random Forest, Decision Tree, Gradient Boosting, KNeighborsRegressor**, và kiểm chứng mô hình với kỹ thuật **GridSearchCV** và **cross-validation**.

## Bộ dữ liệu

- **Nguồn dữ liệu**: Được thu thập từ doanh nghiệp **Hàng Mỹ Nga Hoàng**.
- **Ngày thu thập**: 23/09/2023.
- **Số lượng dữ liệu**: **1966 đơn hàng** (sau xử lý còn **1640 đơn hàng**).
- **Các thuộc tính chính**:
  - `date`: Ngày khách hàng yêu cầu đơn hàng.
  - `name_web`: Trang web nơi đặt hàng.
  - `category`: Danh mục sản phẩm (giày, túi xách, quần áo, mỹ phẩm...).
  - `amount`: Số lượng sản phẩm đặt hàng.
  - `purchase_price_unit`: Giá mua một sản phẩm.
  - `sale_price_unit`: Giá bán một sản phẩm.
  - `revenue`: Tổng lợi nhuận.

## Các phương pháp sử dụng

1. **Xử lý dữ liệu**
   - Chuẩn hóa dữ liệu (loại bỏ lỗi nhập liệu, chuẩn hóa danh mục sản phẩm, xử lý dữ liệu khuyết).
   - Phát hiện và xử lý **outliers**.
   - Chuyển đổi dữ liệu thành dạng dễ sử dụng cho mô hình.

2. **Phân tích dữ liệu**
   - Trực quan hóa dữ liệu để tìm hiểu xu hướng.
   - Đánh giá tương quan giữa các biến với biến mục tiêu (`revenue`).
   - Phân tích các yếu tố ảnh hưởng đến doanh thu.

3. **Xây dựng mô hình dự đoán**
   - Áp dụng nhiều mô hình Machine Learning:
     - **Linear Regression**
     - **Ridge Regression**
     - **Lasso Regression**
     - **Random Forest Regressor**
     - **Decision Tree Regressor**
     - **Gradient Boosting Regressor**
     - **KNeighbors Regressor**
   - Tối ưu hóa tham số bằng **GridSearchCV** và kiểm chứng mô hình với **cross-validation (5 folds)**.
   - So sánh hiệu suất mô hình dựa trên thang đo **R²**.

## Kết quả đạt được

- Mô hình **Ridge Regression** và **Random Forest Regression** cho kết quả **dự đoán doanh thu chính xác nhất**, với **R² > 0.9**.
- **Các yếu tố ảnh hưởng mạnh đến doanh thu**:
  - **Số lượng sản phẩm đặt hàng (`amount`)** có tương quan mạnh nhất với doanh thu.
  - **Giá bán sản phẩm (`sale_price`)** cũng đóng vai trò quan trọng.
  - **Loại sản phẩm và trang web đặt hàng** có ảnh hưởng đáng kể.
- Dữ liệu sau xử lý có **cấu trúc tốt hơn**, giúp mô hình hoạt động hiệu quả.

## Hướng phát triển trong tương lai

- **Mở rộng dữ liệu**: Thu thập thêm dữ liệu từ các doanh nghiệp khác để tăng tính tổng quát.
- **Tích hợp thêm yếu tố bên ngoài** như **xu hướng thị trường, mùa vụ, chiến dịch marketing** để cải thiện dự báo.
- **Phát triển hệ thống dự đoán real-time**, giúp doanh nghiệp đưa ra quyết định nhanh chóng hơn.
- **Tăng cường tính cá nhân hóa**: Dự đoán sở thích khách hàng dựa trên lịch sử mua hàng.
