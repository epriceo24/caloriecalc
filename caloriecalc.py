import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

bur = 0
mac = 0
dog = 0
pep = 0
ham = 0
pbj = 0
fries = 0
can = 0
energy = 0
milkshake = 0

menu_options_counter = 0
pepperoni_option_counter = 0
activity_option_counter = 0

def menu():
    st.write("### Menu:")
    st.write("1. Hamburger")
    st.write("2. Big Mac")
    st.write("3. Hot dog")
    st.write("4. Slice of pizza")
    st.write("5. Ham sandwich")
    st.write("6. Peanut butter & jelly sandwich")
    st.write("7. French fries")
    st.write("8. Can of Coke")
    st.write("9. Sports/Energy drink (16 oz)")
    st.write("10. Milkshake")

menu()

menu_options_counter += 1
option = st.number_input("Select some items for your meal or 11 to choose activity:", min_value=0, value=0, key=f"meal_option_{menu_options_counter}")

while option != 0:
    if option == 1:
        bur = bur + 250
    elif option == 2:
        mac = mac + 563
    elif option == 3:
        dog = dog + 272
    elif option == 4:
        new = st.number_input("Slice with pepperoni? \n 16 for yes or 17 for no:", min_value=16, max_value=17, value=16, key=f"pepperoni_option_{pepperoni_option_counter}")
        if new == 16:
            pep = pep + 309
        elif new == 17:
            pep = pep + 277
    elif option == 5:
        ham = ham + 447
    elif option == 6:
        pbj = pbj + 376
    elif option == 7:
        fries = fries + 400
    elif option == 8:
        can = can + 140
    elif option == 9:
        energy = energy + 52
    elif option == 10:
        milkshake = milkshake + 690
    elif option == 11:
        act = st.selectbox("Select activity:", ["Walking", "Running", "Biking", "Sitting on couch"], key="act_option")
        if act == "Walking":
            nact = 177
        elif act == "Running":
            nact = 596
        elif act == "Biking":
            nact = 650
        elif act == "Sitting on couch":
            nact = 68

        tot = bur + pep + mac + dog + ham + pbj + fries + can + energy + milkshake
        hr = tot / nact
        walking = tot / 177
        running = tot / 596
        biking = tot / 650
        sitting = tot / 68

        walkb = round(walking, 1)
        runb = round(running, 1)
        bikeb = round(biking, 1)
        sitb = round(sitting, 1)

        st.write("Time to burn off:", hr, "hours")
        xs = ["Walking", "Running", "Biking", "Sitting"]
        tops = [walkb, runb, bikeb, sitb]
        st.bar_chart(dict(zip(xs, tops)))

    st.write()
    menu()
    menu_options_counter += 1
    option = st.number_input("Select some items for your meal or 11 to choose activity:", min_value=0, value=0, key=f"meal_option_{menu_options_counter}")