import streamlit as st
import pandas as pd

# Function to load menu from Excel file
def load_menu():
    try:
        menu_df = pd.read_excel('menu.xlsx')
    except FileNotFoundError:
        menu_df = pd.DataFrame(columns=['Day', 'Menu'])
    return menu_df

# Function to save menu to Excel file
def save_menu(menu_df):
    menu_df.to_excel('menu.xlsx', index=False)

# Student Page
def student_page():
    st.title("Student Menu")

    menu_df = load_menu()
    st.write(menu_df)

# Manager Page
def manager_page():
    st.title("Manager Menu")

    menu_df = load_menu()
    
    # Option to add new item to menu
    st.header("Add Item to Menu")
    new_day = st.text_input("Day:")
    new_menu = st.text_input("Menu:")
    if st.button("Add"):
        menu_df = menu_df.append({'Day': new_day, 'Menu': new_menu}, ignore_index=True)
        save_menu(menu_df)
        st.success("Item added successfully!")

    # Option to delete item from menu
    st.header("Delete Item from Menu")
    delete_index = st.selectbox("Select index to delete:", menu_df.index)
    if st.button("Delete"):
        menu_df = menu_df.drop(delete_index)
        save_menu(menu_df)
        st.success("Item deleted successfully!")

    # Option to update item in menu
    st.header("Update Item in Menu")
    update_index = st.selectbox("Select index to update:", menu_df.index)
    new_day = st.text_input("Day:", value=menu_df.loc[update_index, 'Day'])
    new_menu = st.text_input("Menu:", value=menu_df.loc[update_index, 'Menu'])
    if st.button("Update"):
        menu_df.loc[update_index, 'Day'] = new_day
        menu_df.loc[update_index, 'Menu'] = new_menu
        save_menu(menu_df)
        st.success("Item updated successfully!")

    st.write(menu_df)

# Main App
def main():
    page = st.sidebar.radio("Navigation", ["Student", "Manager"])

    if page == "Student":
        student_page()
    elif page == "Manager":
        manager_page()

if __name__ == "__main__":
    main()
