import streamlit as st
import requests
from streamlit_cookies_manager import EncryptedCookieManager

# ---------------- COOKIE ----------------
cookies = EncryptedCookieManager(
    prefix="myapp",
    password="secret_key"
)

if not cookies.ready():
    st.stop()

# Auto login bằng cookie
if "idToken" not in st.session_state:
    if "idToken" in cookies and cookies["idToken"]:
        st.session_state["idToken"] = cookies["idToken"]

API_KEY = "_____________________________"

st.title("📝 Note App with Firebase Login")

# =========================================================
# ---------------- CHƯA LOGIN ----------------
# =========================================================
if "idToken" not in st.session_state:

    st.subheader("🔐 Login / Sign Up")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns(2)

    # -------- LOGIN --------
    with col1:
        if st.button("Login"):
            url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={API_KEY}"

            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": True
            }

            res = requests.post(url, json=payload)

            if res.status_code == 200:
                data = res.json()
                st.session_state["idToken"] = data["idToken"]

                cookies["idToken"] = data["idToken"]
                cookies.save()

                st.success("Login success!")
                st.rerun()
            else:
                st.error("Login failed")

    # -------- SIGN UP --------
    with col2:
        if st.button("Sign Up"):
            url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={API_KEY}"

            payload = {
                "email": email,
                "password": password,
                "returnSecureToken": True
            }

            res = requests.post(url, json=payload)

            if res.status_code == 200:
                st.success("Account created! Now login.")
            else:
                st.error("Sign up failed")

# =========================================================
# ---------------- ĐÃ LOGIN ----------------
# =========================================================
else:

    token = st.session_state["idToken"]

    st.subheader("📋 Your Notes")

    # -------- LOGOUT --------
    if st.button("Logout"):
        del st.session_state["idToken"]

        cookies["idToken"] = ""
        cookies.save()

        st.success("Logged out")
        st.rerun()

    # -------- ADD NOTE --------
    st.subheader("➕ Add Note")
    note = st.text_input("Enter note")

    if st.button("Add Note"):
        requests.post(
            "http://127.0.0.1:8000/notes",
            json={"content": note},
            headers={"Authorization": f"Bearer {token}"}
        )
        st.success("Added!")
        st.rerun()

    # -------- LOAD NOTES --------
    res = requests.get(
        "http://127.0.0.1:8000/notes",
        headers={"Authorization": f"Bearer {token}"}
    )

    if res.status_code == 200:
        notes = res.json()

        for n in notes:
            col1, col2 = st.columns([4, 1])

            with col1:
                st.write(n["content"])

            with col2:
                if st.button("❌", key=n["id"]):
                    requests.delete(
                        f"http://127.0.0.1:8000/notes/{n['id']}",
                        headers={"Authorization": f"Bearer {token}"}
                    )
                    st.rerun()
