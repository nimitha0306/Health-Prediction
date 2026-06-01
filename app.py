import streamlit as st
import pandas as pd
import re

from datetime import date

from database import *
from prediction import predict_health

create_table()

st.set_page_config(
    page_title="Health Prediction App",
    layout="wide"
)

st.title("🏥 Health Prediction Application")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Create",
        "View",
        "Update",
        "Delete"
    ]
)
if menu == "Create":

    st.subheader("Add Patient")

    full_name = st.text_input(
        "Full Name"
    )

    dob = st.date_input(
        "Date of Birth", min_value=date(1000, 1, 1)
    )

    email = st.text_input(
        "Email Address"
    )

    glucose = st.number_input(
        "Glucose"
    )

    haemoglobin = st.number_input(
        "Haemoglobin"
    )

    cholesterol = st.number_input(
        "Cholesterol"
    )

    if st.button("Predict & Save"):

        if dob > date.today():
            st.error(
                "DOB cannot be future date"
            )

        elif not re.match(
            r'^[\w\.-]+@[\w\.-]+\.\w+$',
            email
        ):
            st.error(
                "Invalid Email"
            )

        else:

            remarks = predict_health(
                glucose,
                haemoglobin,
                cholesterol
            )

            add_patient(
                full_name,
                str(dob),
                email,
                glucose,
                haemoglobin,
                cholesterol,
                remarks
            )

            st.success(
                "Patient Saved Successfully"
            )

            st.write(
                "AI Remarks:",
                remarks
            )
elif menu == "View":

    st.subheader("Patient Records")

    data = get_patients()

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Name",
            "DOB",
            "Email",
            "Glucose",
            "Haemoglobin",
            "Cholesterol",
            "Remarks"
        ]
    )

    st.dataframe(
        df,
        use_container_width=True
    )
elif menu == "Delete":

    data = get_patients()

    ids = [row[0] for row in data]

    patient_id = st.selectbox(
        "Patient ID",
        ids
    )

    if st.button(
        "Delete Patient"
    ):
        delete_patient(
            patient_id
        )

        st.success(
            "Deleted Successfully"
        )
elif menu == "Update":

    data = get_patients()

    ids = [row[0] for row in data]

    patient_id = st.selectbox(
        "Patient ID",
        ids
    )

    selected = None

    for row in data:
        if row[0] == patient_id:
            selected = row
            break

    full_name = st.text_input(
        "Full Name",
        value=selected[1]
    )

    dob = st.text_input(
        "DOB",
        value=selected[2]
    )

    email = st.text_input(
        "Email",
        value=selected[3]
    )

    glucose = st.number_input(
        "Glucose",
        value=float(selected[4])
    )

    haemoglobin = st.number_input(
        "Haemoglobin",
        value=float(selected[5])/100000
    )

    cholesterol = st.number_input(
        "Cholesterol",
        value=float(selected[6])
    )

    if st.button(
        "Update Patient"
    ):

        remarks = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        update_patient(
            patient_id,
            full_name,
            dob,
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        )

        st.success(
            "Updated Successfully"
        )