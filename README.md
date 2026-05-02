# Note App (FastAPI + Streamlit + Firebase)

## 1. Hướng dẫn cài đặt environment

### Bước 1: Clone project

``` bash
git clone <your-repo-link>
cd lab2-api-firebase
```

### Bước 2: Tạo virtual environment

``` bash
python -m venv venv
```

### Bước 3: Kích hoạt venv

**Windows:**

``` bash
venv\Scripts\activate
```

**Mac/Linux:**

``` bash
source venv/bin/activate
```

### Bước 4: Cài thư viện

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 2. Hướng dẫn chạy backend

### Di chuyển vào thư mục backend:

``` bash
cd backend
```

### Chạy server FastAPI:

``` bash
uvicorn app.main:app --reload
```

### Truy cập:

-   API Docs: http://127.0.0.1:8000/docs

------------------------------------------------------------------------

## 3. Hướng dẫn chạy frontend

### Di chuyển vào thư mục frontend:

``` bash
cd frontend
```

### Chạy Streamlit:

``` bash
streamlit run app.py
```

### Truy cập:

-   http://localhost:8501

------------------------------------------------------------------------

## 🎥 4. Video demo

Dán link video demo của bạn vào đây:

    https://your-video-link

------------------------------------------------------------------------

##  Công nghệ sử dụng

-   FastAPI
-   Streamlit
-   Firebase Authentication
-   Firebase Firestore

------------------------------------------------------------------------

## Tính năng

-   Đăng ký tài khoản (Sign up)
-   Đăng nhập (Login)
-   Ghi nhớ đăng nhập (Cookie)
-   Thêm ghi chú
-   Xem danh sách ghi chú
-   Xóa ghi chú
