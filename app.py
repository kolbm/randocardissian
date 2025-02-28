import streamlit as st
import random

# Streamlit app
def randomize_selection():
    st.title("Randomize Selection from Text File")
    
    # File uploader to input a text file
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    
    if uploaded_file is not None:
        # Read the content of the uploaded text file
        text = uploaded_file.getvalue().decode("utf-8")
        
        # Split the text content into lines
        items = text.splitlines()
        
        if items:
            # Randomly select an item from the list
            random_item = random.choice(items)
            
            # Display the randomly selected item
            st.write(f"Randomly selected item: {random_item}")
        else:
            st.write("The file is empty!")
    else:
        st.write("Please upload a text file.")

if __name__ == "__main__":
    randomize_selection()

