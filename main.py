import streamlit as st

from tensorflow import keras

import numpy as np

st.set_page_config(
     page_title="Plant.AI App",
     page_icon="☘",
     layout="wide",
     initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/leopold-terpereau',
         'About': "# I'm Léopold Terpereau. An *engineering french student*. "
     }
 )

st.markdown("# Plant.AI")

st.title("")

st.text(" Welcome to the Plant.AI app ! ")
st.write("We developped this app to let you get an automatic diagnosis of your plant's health:")
st.write("- Choose a species among those in Select your plant's species")
st.write("- Take a picture of one of your plant's leaves, with a neutral background (grey is perfect)")
st.write("- Drop your photo")
st.write("- Get an automatic diagnosis by clicking on Determine health or species")
st.subheader("Et voilà ✨")


choice_list = ["Species recognition (Work in progress)", "Cherry tree 🍒","Strawberry plant 🍓","Corn plant 🌽","Bell pepper plant 🔔","Apple tree 🍏","Grape vine 🍇","Tomato plant 🍅"]
folder_list = ["ResNet50", "Cerise","Fraise","Maïs","Poivron","Pomme","Raisin","Tomate"]

with st.container():
    st.write(" ")
    st.write(" ")
    st.write(" ")


col1,col2,col3=st.columns(3)

with col1:
    choice = st.selectbox("Select your plant's species",choice_list,index=5)

if choice == "Species recognition (Work in progress)":
     st.write("Work in progress")
    #folder = folder_list[0]
    #file = "/resnet50.h5"
    #resnet = True
else:
    for i in range(1,len(choice_list)):
        if choice_list[i] == choice:
            folder = folder_list[i]
            file = "/model"
            resnet = False

model = keras.models.load_model("models/" + folder + file)

with col2:
    image = st.file_uploader("Select an image", type=["jpg","jpeg","png"], accept_multiple_files=False, key=None, help=None)

with col3:
    st.write("")
    st.write("")
    st.write("")
    button = st.button("Determine health or species")

HEALTH_CLASSES = {
    0: 'the leaf comes from an healthy plant ✔',
    1: 'the leaf comes from an unhealthy plant 🤒'
}

SPECIES_CLASSES = {
    0: 'the leaf comes from a apple tree 🍎',
    1: 'the leaf comes from a apple tree 🍏',
    2: 'the leaf comes from a apple tree 🍎',
    3: 'the leaf comes from a apple tree 🍏',
    4: 'the plant is not recognized ❌',
    5: 'the leaf comes from a cherry tree 🍒',
    6: 'the leaf comes from a cherry tree 🍒',
    7: 'the leaf comes from a corn plant 🌽',
    8: 'the leaf comes from a corn plant 🌽',
    9: 'the leaf comes from a corn plant 🌽',
    10: 'the leaf comes from a corn plant 🌽',
    11: 'the leaf comes from a grape vine 🍇',
    12: 'the leaf comes from a grape vine 🍇',
    13: 'the leaf comes from a grape vine 🍇',
    14: 'the leaf comes from a grape vine 🍇',
    15: 'the plant is not recognized ❌',
    16: 'the plant is not recognized ❌',
    17: 'the plant is not recognized ❌',
    18: 'the leaf comes from a bell pepper plant 🌶',
    19: 'the leaf comes from a bell pepper plant 🌶',
    20: 'the plant is not recognized ❌',
    21: 'the plant is not recognized ❌',
    22: 'the plant is not recognized ❌',
    23: 'the plant is not recognized ❌',
    24: 'the plant is not recognized ❌',
    25: 'the plant is not recognized ❌',
    26: 'the leaf comes from a strawberry plant 🍓',
    27: 'the leaf comes from a strawberry plant 🍓',
    28: 'the leaf comes from a tomato plant 🍅',
    29: 'the leaf comes from a tomato plant 🍅',
    30: 'the leaf comes from a tomato plant 🍅',
    31: 'the leaf comes from a tomato plant 🍅',
    32: 'the leaf comes from a tomato plant 🍅',
    33: 'the leaf comes from a tomato plant 🍅',
    34: 'the leaf comes from a tomato plant 🍅',
    35: 'the leaf comes from a tomato plant 🍅',
    36: 'the leaf comes from a tomato plant 🍅',
    37: 'the leaf comes from a tomato plant 🍅',
}


if image!=None:
    st.subheader("Selected image")
    st.image(image, width=256, clamp=False, channels="RGB", output_format="auto")
    image = keras.preprocessing.image.load_img(image, target_size=(256, 256))
    image = np.asarray(image)
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))

    if button == True:



        if resnet == True:
            classes = SPECIES_CLASSES
        else :
            classes = HEALTH_CLASSES
            image = image / 255

        prediction = model.predict(image)[0]

        best = 0
        index = 0
        for i in range(len(prediction)):
            if prediction[i] > best:
                best = prediction[i]
                index = i

        st.header("The model predicts that " + str(classes[index]))
