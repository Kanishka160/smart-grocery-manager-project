import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from groq import Groq
from database_manager import setup_db, get_connection
import datetime

# ✅ Initialize DB
setup_db()

# ✅ Groq Client (FREE AI)
groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])

st.title("🛒 Smart Grocery Manager")

menu = ["Login", "Signup"]
choice = st.sidebar.selectbox("Menu", menu)

if "user_id" not in st.session_state:
    st.session_state.user_id = None

# ✅ SIGNUP
if choice == "Signup":
    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")

    if st.button("Create Account"):
        con = get_connection()
        cur = con.cursor()
        try:
            cur.execute("INSERT INTO users(username,password) VALUES(%s,%s)", (username, password))
            con.commit()
            st.success("✅ Account Created! Now Login")
        except:
            st.error("❌ Username already exists!")
        con.close()

# ✅ LOGIN
if choice == "Login":
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        con = get_connection()
        cur = con.cursor()
        cur.execute("SELECT id FROM users WHERE username=%s AND password=%s", (username, password))
        data = cur.fetchone()
        con.close()

        if data:
            st.session_state.user_id = data[0]
            st.success("✅ Login Successful")
        else:
            st.error("❌ Invalid Username or Password")

# ✅ DASHBOARD SCREEN — ONLY AFTER LOGIN
if st.session_state.user_id:
    st.subheader("➕ Add Grocery Item")
    name = st.text_input("Item Name")
    qty = st.number_input("Quantity", min_value=1)
    expiry = st.date_input("Expiry Date")
    category = st.text_input("Category (Ex: Dairy, Snacks, Fruits)", value="General")

    if st.button("Add Item"):
        con = get_connection()
        cur = con.cursor()
        cur.execute("INSERT INTO items(user_id,name,quantity,expiry,category) VALUES(%s,%s,%s,%s,%s)",
                    (st.session_state.user_id, name, qty, expiry, category))
        con.commit()
        con.close()
        st.success("✅ Item Added Successfully!")

    # ✅ DISPLAY ITEMS
    con = get_connection()
    df = pd.read_sql_query(
        f"SELECT name, quantity, expiry, category FROM items WHERE user_id={st.session_state.user_id}", con)
    con.close()

    st.subheader("📋 Your Grocery Items")

    if not df.empty:

        df['expiry'] = pd.to_datetime(df['expiry'])
        df['Alert'] = df['expiry'].apply(
            lambda x: "⚠ Expiring Soon" if (x - pd.Timestamp.today()).days <= 3 else "")
        st.dataframe(df)

        # ✅ EXPIRY STATUS CHART
        df['status'] = df['expiry'].apply(
            lambda x: 'Expired' if x.date() < pd.Timestamp.today().date()
            else ('Expiring Soon' if (x.date() - pd.Timestamp.today().date()).days <= 3 else 'Fresh')
        )

        st.subheader("📊 Expiry Status Breakdown")
        status_count = df['status'].value_counts()

        fig1, ax1 = plt.subplots()
        ax1.pie(status_count, labels=status_count.index, autopct='%1.1f%%')
        st.pyplot(fig1)

        # ✅ CATEGORY BAR CHART
        st.subheader("📈 Items by Category")
        category_count = df['category'].value_counts()
        fig2, ax2 = plt.subplots()
        ax2.bar(category_count.index, category_count.values)
        st.pyplot(fig2)

        # ✅ AI RECIPE SUGGESTIONS
        st.subheader("🍽️ AI Recipe Suggestions")
        expiring_items = df[df['Alert'] != ""]

        if st.button("Suggest Recipes 🍳"):
            if not expiring_items.empty:
                ingredients = ", ".join(expiring_items['name'].tolist())

                try:
                    response = groq_client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {"role": "system", "content": "You are a helpful chef providing short, easy recipes."},
                            {"role": "user", "content": f"Suggest 3 easy recipes using: {ingredients}. Include steps."}
                        ]
                    )

                    recipe_text = response.choices[0].message.content
                    st.success("Here are some recipes 😋")
                    st.write(recipe_text)

                except Exception as e:
                    st.error(f"⚠ AI Error: {e}")

            else:
                st.warning("⚠ No expiring items for recipe suggestions!")

    else:
        st.info("📦 No Items Yet — Start Adding!")
