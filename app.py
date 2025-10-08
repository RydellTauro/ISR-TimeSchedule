import streamlit as st
import TimeScheduleGenerator as tsg
import os

st.title("Train Schedule Generator")

st.write("Click the button to generate the train schedule Gantt chart:")

if st.button("Generate Schedule"):
    try:
        html_file = tsg.generate_schedule()
        
        # Display chart in browser
        with open(html_file, "r", encoding="utf-8") as f:
            html_content = f.read()
            st.components.v1.html(html_content, height=800, scrolling=True)

        # Download button
        with open(html_file, "rb") as f:
            st.download_button(
                label="Download Schedule HTML",
                data=f,
                file_name=html_file,
                mime="text/html"
            )

        st.success("Schedule generated successfully!")

    except Exception as e:
        st.error(f"Error generating schedule: {e}")
