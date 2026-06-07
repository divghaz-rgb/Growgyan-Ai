import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. एआई कॉन्फ़िगरेशन (यहाँ अपनी असली Gemini API Key डालें)
GOOGLE_API_KEY = "AQ.Ab8RN6I0sR8SFe46_MQ8ktwdkA6dejtPq7HNk_OvY62u8ys9zQ"
genai.configure(api_key=AQ.Ab8RN6LmwXMWIEvbwumLYZ-FXe7jKLbDTbZFd0Os-a-9NhUwQQ)

# ऐप सेटअप
st.set_page_config(page_title="GrowGyan AI", page_icon="🌱", layout="centered")

# सेशन स्टेट (लॉगिन याद रखने के लिए)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------- स्क्रीन 1: लॉगिन सिस्टम -----------------
if not st.session_state.logged_in:
    st.title("🔐 GrowGyan AI - Login System")
    st.write("कृपया ऐप का उपयोग करने के लिए लॉगिन करें।")
    
    username = st.text_input("Phone Number or Email (फ़ोन नंबर या ईमेल):")
    password = st.text_input("Password (पासवर्ड):", type="password")
    
    if st.button("Login (लॉगिन करें)"):
        if username and password:
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("कृपया फोन नंबर/ईमेल और पासवर्ड दोनों भरें!")

# ----------------- स्क्रीन 2: मुख्य ऐप (Gemini AI स्टाइल) -----------------
else:
    # साइडबार विकल्प
    lang = st.sidebar.selectbox("🌐 भाषा चुनें / Language", ["Hindi", "English"])
    if st.sidebar.button("Logout (लॉगआउट)"):
        st.session_state.logged_in = False
        st.rerun()

    # नाम और डिज़ाइन सेटअप
    if lang == "Hindi":
        st.title("🌱 GrowGyan AI")
        st.subheader("आपका पर्सनल खेती-बाड़ी एआई दोस्त")
        prompt_label = "पूछें: फोटो खींचें, लिखकर या बोलकर समस्या बताएं..."
        btn_label = "जवाब ढूँढें ✨"
        voice_msg = "🎤 वॉइस असिस्टेंट चालू है... अपनी समस्या बोलें!"
        system_instruction = "इस पौधे की पत्ती को देखकर बताएं कि इसमें कौन सी बीमारी है और इसका घरेलू या वैज्ञानिक इलाज क्या है? जवाब हिंदी में दें।"
    else:
        st.title("🌱 GrowGyan AI")
        st.subheader("Your Personal Agriculture AI Friend")
        prompt_label = "Ask anything: Take a photo, type, or speak your problem..."
        btn_label = "Find Solution ✨"
        voice_msg = "🎤 Voice Assistant is active... Speak now!"
        system_instruction = "Identify the crop disease or answer the farming question based on the input."

    st.write("---")

    # 1. लाइव कैमरा इनपुट (सबसे ऊपर सीधे कैमरा खुलेगा)
    cam_image = st.camera_input("कैमरा / Camera 📸")
    
    # 2. वॉइस असिस्टेंट बटन (कैमरे के ठीक नीचे)
    if st.button("बोलकर पूछें / Speak 🎤"):
        st.info(voice_msg)
        # भविष्य में यहाँ वॉइस-टू-टेक्स्ट कोड जुड़ेगा

    # 3. चैट बॉक्स इनपुट (लिखकर पूछने के लिए)
    user_query = st.text_input(prompt_label, placeholder="यहाँ टाइप करें...")

    # 4. प्रोसेसिंग और एआई रिजल्ट (सब कुछ एक ही जगह)
    if st.button(btn_label):
        # अगर सिर्फ फोटो खींची है
        if cam_image and not user_query:
            image = Image.open(cam_image)
            st.image(image, caption="Uploaded Crop", use_container_width=True)
            st.info("🔄 AI जांच कर रहा है...")
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content([system_instruction, image])
                st.success("🤖 GrowGyan AI:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}. Please check your API Key.")
                
        # अगर फोटो के साथ कुछ लिखा भी है या सिर्फ सवाल पूछा है
        elif user_query:
            inputs = [user_query]
            if cam_image:
                image = Image.open(cam_image)
                st.image(image, use_container_width=True)
                inputs.append(image)
                
            st.info("🔄 AI विचार कर रहा है...")
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(inputs)
                st.success("🤖 GrowGyan AI:")
                st.write(response.text)
            except Exception as e:
                st.error(f"Error: {e}. Please check your API Key.")
        else:
            st.warning("कृपया पहले फोटो खींचें या कुछ टाइप करें!")
            
