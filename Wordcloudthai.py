from pythainlp import word_tokenize
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
from collections import Counter

# สร้างหน้าใน Streamlit
# st.title("Thai Word Cloud from Most Frequent Words")
    # ฟังก์ชันช่วยนับพยางค์ (สามารถใช้จำนวนสระเป็นตัวแทนได้)
def count_syllables(word):
    vowels = "ะาิีึืุูเแโใไ"
    return sum(1 for char in word if char in vowels)
# อัปโหลดไฟล์ข้อความ
# uploaded_file = st.file_uploader("Choose a file", type="txt")
def ThaiWordCloud (thai_text):

    # อ่านไฟล์ข้อความ
    # thai_text = uploaded_file.read().decode('utf-8')

    # แยกคำภาษาไทย
    tokenized_words = word_tokenize(thai_text, engine='newmm')

    # นับจำนวนคำที่ใช้บ่อย
    word_counts = Counter(tokenized_words)


    # กรองคำที่ใช้มากกว่า 2 ครั้ง
    # filtered_word_counts = {word: count for word, count in word_counts.items() if count > 2}

    # กรองคำที่ใช้มากกว่า 2 ครั้งและมีมากกว่า 2 พยางค์
    filtered_word_counts = {word: count for word, count in word_counts.items() if count > 2 and count_syllables(word) > 1}


    # เลือก 10 คำที่ใช้บ่อยที่สุดจากคำที่ผ่านการกรอง
    common_words = dict(Counter(filtered_word_counts).most_common(300))

    # แปลง common_words ให้เป็นข้อความ
    # common_words_text = ', '.join([f'{word}: {count}' for word, count in common_words.items()])
    common_words_text = ', '.join([f'{word}' for word, count in common_words.items()])

    return common_words_text