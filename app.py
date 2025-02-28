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
            # Initialize session state to store the list of randomizations
            if 'randomization_history' not in st.session_state:
                st.session_state.randomization_history = []
            
            # Randomly select an item and add it to the history
            if st.button("Randomize"):
                random_item = random.choice(items)
                st.session_state.randomization_history.append(random_item)
            
            # Display the randomization history (latest first, in bold for the most recent)
            st.markdown("### Randomization History:")
            # Display the latest randomization in large and bold
            if st.session_state.randomization_history:
                latest_item = st.session_state.randomization_history[-1]
                st.markdown(f"#### **Latest Randomization:**")
                st.markdown(f"##### **{latest_item}**")
                
                # Display the previous randomizations in reverse order
                for idx, item in enumerate(reversed(st.session_state.randomization_history[:-1]), 1):
                    st.markdown(f"{len(st.session_state.randomization_history) - idx}. {item}")
            
        else:
            st.write("The file is empty!")
    else:
        st.write("Please upload a text file.")

if __name__ == "__main__":
    randomize_selection()
