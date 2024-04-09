import pandas as pd
import numpy as np 
import streamlit as st

# Load the data
df = pd.read_csv('comment_filtered.csv')

# Create random comment picker instagram that contain a button, when the button is clicked will randomly select a comment from the data and display it on the screen with the photo profile
st.title('PEMENANG GIVEAWAY RAPSPOINT 10 JUTA!')
st.write('Pemenang Giveaway!')

# Create a button
if st.button('Pick a Random Comment'):
    # Create randoming animation
    st.write('Here is the lucky winner!')
    random_number = np.random.randint(0, df.shape[0])
    # Load image with external url with rounded corner using st.markdown
    # st.markdown(f'<img src="{df["avatarUrl"][random_number]}" style="border-radius:50%; width: 100px; height: 100px;">', unsafe_allow_html=True)
    # st.write bold text using st.markdown
    st.markdown(f'<h2>{df["userName"][random_number]}</h2>', unsafe_allow_html=True)
    st.markdown(f'<h3>{df["text"][random_number]}</h3>', unsafe_allow_html=True)
    # st.write(df['text'][random_number])

    # Create button to the url account (open in new tab)
    st.write('Kunjungi Akun:')
    st.markdown(f'<a href="https://instagram.com/{df["userName"][random_number]}" target="_blank">Click Here!</a>', unsafe_allow_html=True)


# # Create a button to show the data
# if st.button('Show the Data'):
#     st.write(df[['userName', 'text']])