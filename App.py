import streamlit as st
import google.generativeai as genai
from PIL import Image

# 1. एआई कॉन्फ़िगरेशन (अपनी असली Gemini API Key यहाँ डालें)
GOOGLE_API_KEY = "YOUR_GEMINI_API_KEY_HERE"
genai.configure(api_key=GOOGLE_API_KEY)

# ऐप सेटअप
st.set_page_config(page_title="GrowGyan AI", page_icon="🌱", layout="centered")

# सेशन स्टेट (ताकि ऐप याद रखे कि यूजर ने लॉगिन किया है या नहीं)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ----------------- स्क्रीन 1: लॉगिन सिस्टम -----------------
if not st.session_state.logged_in:
    st.title("🔐 GrowGyan AI - Login System")
    st.write("कृपया ऐप का उपयोग करने के लिए लॉगिन करें।")
    
    # इनपुट बॉक्स (आपके ब्लूप्रिंट के अनुसार)
    username = st.text_input("Phone Number or Email (फ़ोन नंबर या ईमेल):")
    password = st.text_input("Password (पासवर्ड):", type="password")
    
    if st.button("Login (लॉगिन करें)"):
        if username and password: # अभी टेस्टिंग के लिए कोई भी नाम-पासवर्ड चलेगा
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("कृपया फोन नंबर/ईमेल और पासवर्ड दोनों भरें!")

# ----------------- स्क्रीन 2: मुख्य ऐप (लॉगिन के बाद) -----------------
else:
    # भाषा का चयन (हिंदी और इंग्लिश)
    lang = st.sidebar.selectbox("🌐 Choose Language / भाषा चुनें", ["English", "Hindi"])
    
    # लॉगआउट बटन
    if st.sidebar.button("Logout (लॉगआउट)"):
        st.session_state.logged_in = False
        st.rerun()

    # हिंदी भाषा का इंटरफ़ेस
    if lang == "Hindi":
        st.title("🌱 GrowGyan AI (ग्रोग्यान एआई)")
        st.subheader("किसानों का सच्चा डिजिटल दोस्त")
        st.write("---")
        
        # फीचर्स की लिस्ट आपके नोट के हिसाब से
        tab1, tab2, tab3 = st.tabs(["📸 रोग पहचान", "💬 चैट बॉट", "🔊 वॉइस असिस्टेंट"])
        
        with tab1:
            st.header("फसल की बीमारी पहचानें")
            uploaded_file = st.file_uploader("फसल के बीमार हिस्से की फोटो अपलोड करें...", type=["jpg", "jpeg", "png"])
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, use_container_width=True)
                st.info("🔄 AI जांच कर रहा है...")
                # (यहाँ एआई मॉडल का कोड काम करेगा)
                
        with tab2:
            st.header("चैट बॉट (लिखकर सवाल पूछें)")
            user_msg = st.text_input("अपनी समस्या यहाँ लिखें:")
            if st.button("पूछें"):
                st.write("🤖 GrowGyan AI: आपकी मदद के लिए समाधान तैयार किया जा रहा है...")

        with tab3:
            st.header("वॉइस (बोलने वाला दोस्त)")
            st.warning("🎤 वॉइस असिस्टेंट फीचर पर अभी काम चल रहा है!")

    # इंग्लिश भाषा का इंटरफ़ेस
    else:
        st.title("🌱 GrowGyan AI")
        st.subheader("The Digital Friend of Farmers")
        st.write("---")
        
        tab1, tab2, tab3 = st.tabs(["📸 Scan Disease", "💬 Chat Bot", "🔊 Voice Assistant"])
        
        with tab1:
            st.header("Crop Disease Scanner")
            uploaded_file = st.file_uploader("Upload crop photo...", type=["jpg", "jpeg", "png"])
            
        with tab2:
            st.header("Chat Bot")
            user_msg = st.text_input("Type your question here:")
            
        with tab3:
            st.header("Voice Assistant")
            st.warning("🎤 Voice Feature coming soon!")
