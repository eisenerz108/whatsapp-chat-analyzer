from wordcloud import WordCloud
def fetch_stats(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user].shape[0]


    #1. Fetch Numbers of Messages
    num_messages = df.shape[0]

    #2. Fetch Numbers of Words
    words = []
    for message in df['message']:
        words.extend(message.split())

    return num_messages,len(words)


def fetch_most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / len(df))*100, 2).reset_index().rename(
        columns={'index': 'name', 'user': 'percentage'}
    )
    return x, df


def create_wordcloud(selected_user, df):
    if selected_user != "Overall":
        df = df[df['user'] == selected_user].shape[0]

    wc = WordCloud(
        width=800,
        height=400,
        min_font_size=10,
        background_color='white'
    )

    df_wc = wc.generate(df['message'].str.cat(sep= " "))
    return df_wc