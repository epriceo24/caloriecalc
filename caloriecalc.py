import streamlit as st

walk = 177; run = 596; bike = 650; sit = 68

def menu():
    st.title("Calorie Calculator")
    calories_dictionary = {
        "Hamburger": 250,
        "Big Mac": 563,
        "Hot dog": 272,
        "Slice of pizza": 277,
        "Slice of pepperoni pizza": 309,
        "Ham sandwich": 447,
        "Peanut butter & jelly sandwich": 376,
        "French fries": 400,
        "Can of Coke": 140,
        "Sports/Energy drink (16 oz)": 52,
        "Milkshake": 690
    }

    total_calories = 0

    st.write("Select the items and quantity:")
    for item in calories_dictionary.keys():
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown(f"**{item}**")
        with col2:
            quantity = st.number_input("", min_value=0, max_value=10, value=0, key=f"{item}_input")
            total_calories += quantity * calories_dictionary[item]

    #display total calories
    st.write(f"Total calories: **{total_calories}**")
    st.write("Walking: **{}** hours".format(round(total_calories/walk)))
    st.write("Running: **{}** hours".format(round(total_calories/run)))
    st.write("Biking: **{}** hours".format(round(total_calories/bike)))
    st.write("Sitting: **{}** hours".format(round(total_calories/sit)))

if __name__ == "__main__":
    menu()
