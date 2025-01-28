import streamlit as st
from matplotlib import pyplot as plt

import preprocessor
import helper

st.sidebar.title("WhatsApp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Upload a File")
if uploaded_file is not None:
    bytes_data = uploaded_file.getvalue()
    # Convert to the String from Stream
    data = bytes_data.decode("utf-8")
    df = preprocessor.preprocess(data)
    st.dataframe(df)


    # Fetch Unique Users
    user_list = df['user'].unique().tolist()
    # user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")
    selected_user = st.sidebar.selectbox("Show analysis wrt", user_list)

    if st.sidebar.button("Show Analysis"):
        num_messages, words = helper.fetch_stats(selected_user, df)
        col1, col2 = st.columns(2)

        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)


    if selected_user == "Overall":
        st.title("Overall Statistics")

        x, new_df = helper.fetch_most_busy_users(df)
        fig, ax = plt.subplots()

        col1, col2  = st.columns(2)

        with col1:
            ax.bar(x.index, x.values, color='red')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        with col2:
            st.dataframe(new_df)


    df_wc = helper.create_wordcloud(selected_user, df)
    fig, ax = plt.subplots()
    ax.imshow(df_wc)
    st.pyplot(fig)
