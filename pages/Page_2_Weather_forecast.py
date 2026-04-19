import streamlit as st
import numpy as np
import pickle as pkl
from sklearn.preprocessing import StandardScaler

# Load model and scaler
with open('weather_model.sav', 'rb') as file:
    model = pkl.load(file)

with open('weather_scaler.pkl', 'rb') as file:
    scaler = pkl.load(file)

st.title("🌦️ Weather Prediction App")

# --- Input Widgets ---
Temperature = st.number_input('🌡️ Temperature (°C)', 4.9, 49.6, 25.0)
Humidity = st.number_input('💧 Humidity (%)', 20, 99, 60)
Pressure = st.number_input('🌪️ Pressure (hPa)', 986.0, 1038.9, 1000.0)
Wind_Speed = st.number_input('🌬️ Wind Speed (km/h)', 0.1, 40.0, 10.0)
Wind_Direction = st.number_input('🧭 Wind Direction (°)', 0, 359, 180)
Precipitation = st.number_input('🌧️ Precipitation (mm)', 0.0, 15.3, 2.0)
Cloud_Cover = st.number_input('☁️ Cloud Cover (%)', 0, 99, 50)
Visibility = st.number_input('👁️ Visibility (km)', 1.0, 20.0, 10.0)
Hour = st.number_input('⏰ Hour of Day', 0.0, 23.0, 12.0)

# --- Weather Labels ---
weather_labels = {
    0: "☁️ Cloudy Weather: Perfect for a walk or light activity.",
    1: "☔ Rainy Weather: Carry an umbrella or raincoat.",
    2: "☀️ Sunny Weather: Stay hydrated and wear sunscreen.",
    3: "🌁 Foggy Weather: Stay warm and drive carefully.",
    4: "⛈️ Stormy Weather: Avoid outdoor activities. Stay safe!"
}

# --- Prediction button ---
if st.button('Predict Weather Forecast'):
    user_input = np.array([[Temperature, Humidity, Pressure, Wind_Speed,
                            Wind_Direction, Precipitation, Cloud_Cover,
                            Visibility, Hour]])
    scaled_input = scaler.transform(user_input)
    prediction = model.predict(scaled_input)[0]

    st.session_state['weather_pred'] = prediction

# --- Display results ---
if 'weather_pred' in st.session_state:
    pred = st.session_state['weather_pred']


    # --- Dynamic Background based on Prediction ---
    if pred in [0, 'Cloudy']:
        bg_color = "#B0BEC5"  # Grayish blue for cloudy
    elif pred in [1, 'Rainy']:
        bg_color = "#90CAF9"  # Light blue for rainy
    elif pred in [2, 'Sunny']:
        bg_color = "#FFF59D"  # Yellow for sunny
    elif pred in [3, 'Foggy']:
        bg_color = "#CFD8DC"  # Light gray for foggy
    elif pred in [4, 'Stormy']:
        bg_color = "#78909C"  # Dark gray-blue for stormy
    else:
        bg_color = "#E1BEE7"  # Purple for unknown
    
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {bg_color};
            color: #1A237E;
            transition: background-color 0.5s ease;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("## 🌈 Your Forecast Summary:")

    if pred in [0, 'Cloudy']:
        st.info("☁️ It's Cloudy! Perfect time for a peaceful walk or reading a book.")
    elif pred in [1, 'Rainy']:
        st.warning("☔ It's Rainy! Don’t forget your umbrella or raincoat.")
    elif pred in [2, 'Sunny']:
        st.success("☀️ It's Sunny! Stay hydrated and wear sunscreen.")
    elif pred in [3, 'Foggy']:
        st.info("🌁 It's Foggy! Be careful if you’re heading out — visibility is low.")
    elif pred in [4, 'Stormy']:
        st.error("⛈️ It's Stormy! Stay indoors and stay safe.")
    else:
        st.write("🌈 Unknown weather condition.")

        

    # st.success(weather_labels.get(pred, "🌈 Unknown weather condition."))
    st.subheader(f"Predicted Weather Code: {pred}")

st.markdown('----')
