from openai import AzureOpenAI


gpt4_client = AzureOpenAI(
  #Enter Your Credentials here
  azure_endpoint = "endpoint", 
  api_key= "api-key",  
  api_version= "version"
)

def get_response(user_prompt):
    response = gpt4_client.chat.completions.create(
                #Enter your model's name
                model= "model-name",
                messages = [
                    {"role": "system", "content":"You are an expert in python packages"},
                    {"role": "user", "content":user_prompt}
                    ],
                temperature=0.1,
                top_p=0.60
                )
    return response.choices[0].message.content


#Front end
import streamlit as st

#UI config
st.set_page_config(page_title='PyVerify',layout="wide")
st.markdown(
    """
    <style>
    .custom-title {
        color: #28a745;  /* Green color */
        font-size: 50px;  /* Adjust the font size as needed */
        font-family: 'Georgia', serif;  /* Change to a more stylistic font */
        font-style: italic;  /* Italic font style */
    }

    .main{
        background-color: #90ee90;
        background-image: url('C:\\Users\\2106624\\Downloads\\alkov160700009.jpg')
        backgound-size: cover;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Use the custom class for the title
st.markdown('<h1 class="custom-title">Welcome to PyVerify!</h1>', unsafe_allow_html=True)

# Additional content
st.markdown("<h3> Your one stop app to validate your packages</h3>", unsafe_allow_html=True)

#UI -- User Query
user_input=st.text_input(placeholder='Enter your package name eg. openpyxl',label="Input_Package", label_visibility="hidden")

#UI Search button
if user_input!="":
    if st.button('Verify'):
        user_prompt=f"Is the below package supported the most commanly used package? If No return a comma separated list of alternatives :{user_input}"
        ui_op=get_response(user_prompt)
        st.markdown(f"**{ui_op}**")
