
import streamlit as st
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
groq_api_key = os.getenv('GROQ_API_KEY')

# Set up the page title
st.set_page_config(page_title="Food Plan", layout="wide")
st.title("🌿 Food Plan Generator - Your Wellness Guide")

# Initialize the language model
llm = ChatGroq(
    groq_api_key=groq_api_key,
    model="llama-3.1-8b-instant",
    temperature=0,
)

# Define the system message
system_message = """ Act like Luke Coutinho, a globally renowned holistic lifestyle coach.
            Based on the medical condition: {Acidity, Acne, ADHD, Alopecia, Anemia, Arthritis, Asthma, 
            Autism, Bloating/Flatulence, Bronchitis, Celiac Disease, CFS, Constipation, COPD, Cough, Cold, Fever,
            Dandruff, Diabetes, Dyslipidemia, Eczema, Endometriosis, Fibromyalgia, H Pylori, Hair fall, Hair regrowth, 
            Hypertension, IBD/Crohn's, IBS, Kidney Health, Liver health, Lung health, Menopause, Migraine, Multiple Sclerosis,
            Myasthenia gravis, Myopathy, Osteoporosis, PCOD, Peptic Ulcer, Pigmentation, Plantar Fasciitis, Premature Greying,
            Prostate,  Psoriasis, Sciatica, Sinus, Thyroid, Ulcerative Colitis, Uric Acid and Gout, Urticaria/ Hives, UTI,  Vitiligo
            }, 
            generate a comprehensive daily food and lifestyle plan that supports healing through natural, seasonal, and sustainable living. Use the following structure and tone:
            
            1.Mindset & Affirmations
            Start with a brief affirmation or mental approach specific to this condition. Highlight emotional healing and mind-body balance.

            2. Fueling Right Plan (Daily Meal Plan)
            Present the meal plan in the following table format:
            Example:
            | TestTime | Meal | Composition & Variations | Benefits & Notes |
           

            3. Supplement Stack
            If necessary, add gentle and natural supplements using this table:            
            Example:
            | Supplement | Dosage | Timing | Purpose |
           
            
            4. Movement Protocol
            Suggest suitable movement or yoga practices specific to the condition. Include duration, style (e.g. walking, yin yoga, strength training), and mindfulness elements.

            5. Key Lifestyle Guidelines
            Use this table for core habits that support healing:
            Example:
            | Aspect | Recommendations|
            

            6. Key Lifestyle Guidelines / Good to Add
            Use this table to clarify what's good to include or avoid:

            Make a proper markdown response.

            """
    
   
# Input section
condition = st.text_input("Enter your medical condition (e.g., Eczema, Diabetes, PCOD):")

# On button click
if st.button("Get Wellness Plan"):
    if condition:
        with st.spinner("Crafting your wellness plan... 🧘‍♂️"):
            # Prepare messages
            messages = [
                ("system", system_message),
                ("human", f"{condition}")
            ]
            
            # Get response
            response = llm.invoke(messages)

            # Display the markdown result
            st.markdown(response.content)
    else:
        st.warning("Please enter a medical condition to proceed.")
