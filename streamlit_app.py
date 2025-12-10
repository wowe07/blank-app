import streamlit as st

st.title("🎈Groceries List")
if "items" not in st.session_state:
    st.session_state["items"] = []


new_item = st.text_input("Add an item")

if st.button("Add"):
    if new_item.strip:
        st.session_state["items"].append(new_item)

if st.session_state["items"]:
    item_remove = st.selectbox("Choose an item to remove", st.session_state["items"])

    if st.button("Remove"):
        st.session_state["items"].remove(item_remove)


st.write(st.session_state["items"])
