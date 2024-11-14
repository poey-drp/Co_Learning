import streamlit as st
import Web_present  # import module ที่ compile แล้ว


# st.set_page_config(
#     layout="wide",
# )

st.set_page_config(
    page_title="CONNECTIVE LEARNING",
    layout="wide",
    initial_sidebar_state="auto"
)

# สมมติว่า Web_present มีฟังก์ชันที่เรียกว่า display_data
# st.title("การแสดงผลข้อมูลจากไฟล์ Web_present.so")
# result = Web_present.display_data()
result = Web_present.Web_present()
# st.write(result)
