from groq import Groq

groq_client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def get_recipe_suggestions(items):
    ingredients = ", ".join(items)

    response = groq_client.chat.completions.create(
        model="llama3-8b-8192",  # 🚀 Free model on Groq
        messages=[
            {"role": "system", "content": "You are a smart recipe assistant."},
            {"role": "user", "content": f"Suggest 3 quick, easy recipes using these ingredients: {ingredients}. Include steps & measurements."}
        ]
    )

    return response.choices[0].message.content
