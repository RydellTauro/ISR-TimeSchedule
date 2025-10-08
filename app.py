# app.py
import streamlit as st
import TimeScheduleGenerator as tsg

st.title("Train Schedule Generator")
st.write("Click the button to generate the train schedule Gantt chart:")

if st.button("Generate Schedule"):
    try:
        html_content = tsg.generate_schedule_html()

        # Display chart in browser
        st.components.v1.html(html_content, height=800, scrolling=True)

        # Download button
        html_bytes = html_content.encode("utf-8")
        st.download_button(
            label="Download Schedule HTML",
            data=html_bytes,
            file_name="time_schedule_gantt_colored1.html",
            mime="text/html"
        )

        st.success("Schedule generated successfully!")

    except Exception as e:
        st.error(f"Error generating schedule: {e}")
