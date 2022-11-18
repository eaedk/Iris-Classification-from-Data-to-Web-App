import streamlit as st
import pandas as pd
import os, pickle


# first line after the importation section
st.set_page_config(page_title="Iris Classification Web App", page_icon="🌼", layout="centered")
DIRPATH = os.path.dirname(os.path.realpath(__file__))

# Useful functions
@st.cache()  # stop the hot-reload to the function just below
def setup(tmp_df_file):
    "Setup the required elements like files, models, global variables, etc"
    # sepal_length (cm)	sepal_width (cm)	petal_length (cm)	petal_width (cm)
    pd.DataFrame(
        dict(
            sepal_length=[],
            sepal_width=[],
            petal_length=[],
            petal_width=[],
        )
    ).to_csv(tmp_df_file, index=False)

    

@st.cache(allow_output_mutation=True)
def load_ml_items():
    "Load ML items to reuse them"

    with open(os.path.join('ml','ML_items'), 'rb') as file:
        loaded_object = pickle.load(file)
    return loaded_object



#Config 
tmp_df_file = os.path.join(DIRPATH, "tmp", "data.csv")
setup(tmp_df_file)

loaded_object = load_ml_items()
if 'results' not in st.session_state:
    st.session_state['results'] = []


# Interface and logic
st.title("🌼🌸❀✿🌷 Iris Classification App")

st.sidebar.write(f"Iris Classification App")
st.sidebar.write(f"This classification app has been made with Streamlit.")

form = st.form(key="information", clear_on_submit=True)

# Form to retreive the inputs
with form:
    # First row
    cols = st.columns((1, 1))
    sepal_length = cols[0].number_input("Sepal length (cm)")
    sepal_width = cols[1].number_input("Sepal width (cm)")

    # Second row
    cols = st.columns((1, 1))
    petal_length = cols[0].number_input("Petal length (cm)")
    petal_width = cols[1].number_input("Petal width (cm)")
    
    #Submit button
    submitted = st.form_submit_button(label="Submit")

# Logic when the inputs are submitted
if submitted:

    # Inputs formatting
    dict_input = {'sepal length (cm)': [sepal_length],
    'sepal width (cm)': [sepal_width],
    'petal length (cm)': [petal_length],
    'petal width (cm)': [petal_width]}

    df = pd.DataFrame.from_dict(dict_input)
    
    # Preprocessing
    _ = loaded_object['scaler'].transform(df)

    # Prediction
    output = loaded_object['model'].predict_proba(_)

    # print(type(output))
    # print(output)
    # print(output.shape)

    # Format the prediction output
    pred_class = output.argmax(axis=-1)
    confidence_score = output[0, pred_class] # np.array[axis_0, axis_1 ]

    df["confidence score"] = confidence_score # [0.8]
    df["predicted class"] = pred_class # [0]
    st.session_state['results'].append(df)
    # Add pred label later

    
    # Display prediction results
    st.balloons()
    st.success(f"Predicted class: {pred_class[0]}")
    st.success(f"Confidence score: {confidence_score[0]}")

    # Area to visualize the previous predictions 
    expander = st.expander("See the predictions done until now..")
    with expander:
        result = pd.concat(st.session_state['results'],)
        st.dataframe(result, use_container_width=True)