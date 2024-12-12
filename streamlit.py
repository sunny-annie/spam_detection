import streamlit as st
from main import predict


st.title("Спам или не спам?")
text = st.text_area("Введите текст для проверки:", height=150)

if st.button("Проверить"):
    if text.strip():  # Проверяем, что текст не пустой
        result = predict(text)
        st.success(f"Результат: **{result}**")
    else:
        st.warning("Введите текст для проверки!")