import streamlit as st
import client


cls = client.create_class()


if __name__ == "__main__":
    st.write(f"# Created class: \n\n      {cls}")
