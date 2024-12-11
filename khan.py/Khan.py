import streamlit as st
import random

# Game data with online images
game_data = [
    {
        "word": "apple",
        "images": [
            "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/f/fa/Apple_logo_black.svg",
            "https://upload.wikimedia.org/wikipedia/commons/1/1e/Golden_delicious_apple.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/8/82/Apple_shot_broken.jpg",
        ],
    },
    {
        "word": "cat",
        "images": [
            "https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/b/b6/Felis_catus-cat_on_snow.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/5/51/Cat_lying_down.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/3/3d/Cat_sitting_on_a_chair.jpg",
        ],
    },
    {
        "word": "car",
        "images": [
            "https://upload.wikimedia.org/wikipedia/commons/8/85/Ford_Mustang_GT.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/6/6b/Toyota_Yaris.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/0/02/Tesla_Model_S_P90D.jpg",
            "https://upload.wikimedia.org/wikipedia/commons/2/24/Lamborghini_Aventador.jpg",
        ],
    },
]

# Initialize game state
if "current_word" not in st.session_state:
    st.session_state.current_word = random.choice(game_data)
    st.session_state.attempts = 0
    st.session_state.score = 0

def reset_game():
    """Reset the game to start fresh."""
    st.session_state.current_word = random.choice(game_data)
    st.session_state.attempts = 0

# Game title
st.title("🖼️ 4 Pics 1 Word")
st.markdown("Guess the word that links the four images!")

# Display the images
cols = st.columns(2)
for i, img_url in enumerate(st.session_state.current_word["images"]):
    with cols[i % 2]:
        st.image(img_url, use_column_width=True)

# Input for the user's guess
user_guess = st.text_input("Enter your guess:", "").strip().lower()

if st.button("Submit Guess"):
    st.session_state.attempts += 1
    correct_word = st.session_state.current_word["word"]
    if user_guess == correct_word:
        st.success(f"🎉 Correct! The word is **{correct_word.upper()}**.")
        st.session_state.score += 1
        reset_game()
    else:
        st.error("❌ Incorrect! Try again.")

# Display score and attempts
st.markdown(f"**Score**: {st.session_state.score}")
st.markdown(f"**Attempts**: {st.session_state.attempts}")

# Restart game
if st.button("New Game"):
    reset_game()
