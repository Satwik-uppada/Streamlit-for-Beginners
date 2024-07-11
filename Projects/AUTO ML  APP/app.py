import pandas as pd
import streamlit as st
import eda

st.set_page_config(page_title="QuickInsight",page_icon=':material/rocket:', layout= "wide", initial_sidebar_state= "expanded",menu_items= None)
# 
# st.session_state.eda_button = False
# st.session_state.train = False
st.session_state.data = None

#SECTION -  css styling
st.markdown("""
<style>
    [class="main st-emotion-cache-bm2z3a ea3mdgi8"]{
        background-image: linear-gradient(#ddd6f3 , #faaca8);
        # background-size: cover;
    }
    
    [class="st-emotion-cache-6qob1r eczjsme8"]{
        background-color: linear-gradient(#ddd6f3 , #faaca8);
        # background-size: cover;
    }
    
    [data-testid="stHeader"]{
        background-color: #ddd6f3;
        # visibility: hidden;
	}
 
    # [data-testid="baseButton-header"]{
        # visibility: hidden;
    # }
    
    .st-emotion-cache-183lzff {
    font-family: "Source Code Pro", "monospace";
    white-space: pre;
    font-size: 16px;
    overflow-x: auto;
    }
    
    .st-emotion-cache-1nuyb3h p {
    word-break: break-word;
    margin-bottom: 0px;
    font-size: 16px;
    }
    .st-emotion-cache-5drf04 {
    height: 4rem;
    max-width: 15rem;
    margin: 0.25rem 0.5rem 0.25rem 0px;
    z-index: 999990;
    }

</style>""",
unsafe_allow_html=True)

#!SECTION


def start():
    # ANCHOR - sidebar code
    with st.sidebar:
        # LOGO_URL_LARGE = "https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png"
        LOGO_URL_SMALL = "images/logo.png"
        st.logo(LOGO_URL_SMALL)
        st.title("QuickInsight")
        st.sidebar.image("images/main.png",caption="Automated Exploratary Data Analysis")
        st.divider()

        st.info("An AutoStreamML, this allows you to build an automated ML pipeline using streamlit, pandas Profilling, and PyCaret.")



    #ANCHOR - Starting of the app
    
    st.header("⬆️ Upload Your Data for Modelling!",divider='rainbow')
    file = st.file_uploader(label=":rainbow-background[Upload Here 👇]",type=['csv','xlsx'], label_visibility="visible", help="🗂️ :rainbow[Upload only csv or xlsx files]",key="file_uploader")



    if "data" not in st.session_state:
        st.session_state.data=""
    try: 
        if file:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file,index_col=None)
            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file, index_col=None)

            dataframe = st.dataframe(df,width=4000,height=500)

            st.session_state.data = df

            toast_message.toast(":rainbow[File Succuessfully Uploaded]",icon="✅")

            eda_button = st.button("── :red[☆]⋅ Click Me! ⋅:red[☆] ──", help="👇 :rainbow[Click to see Automated EDA Results]")
            if "eda_button" not in st.session_state:
                st.session_state.eda_button  = False

            if eda_button:
                try:
                    toast_message.toast(":rainbow[Let the magic begins....]",icon="🪄")
                    eda.EDA(st.session_state.data)
                except Exception as e:
                    st.warning(f"⚠️ Problem with EDA funtion: {e}")

    except Exception as e:
            st.warning(f"⚠️ Error in Uploading the file: {e}")


toast_message = st.toast(":rainbow[Welcome to QuickInsight...]",icon='🙏')
start()