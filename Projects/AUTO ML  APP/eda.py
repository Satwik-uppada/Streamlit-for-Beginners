import streamlit as st    
import ml
 

#ANCHOR - EDA function  
def EDA(data):
    import ydata_profiling
    from ydata_profiling import ProfileReport
    import time
    from streamlit_pandas_profiling import st_profile_report
    
    st.info("Welcome to NxtGen EDA Insights",icon="✴️")
    st.header("📶 Automated Exploratory Data Analysis",divider='rainbow')
    
    
    # with st.status(":blue-background[Exploring 🔍..]", expanded=True) as status:
        # 
        # text = st.text("1️⃣. 👨🏼‍💻 Analyzing Overview of  data...")
        # time.sleep(2)
        # text.text("2️⃣. 🤔 Understanding features and thier datatypes.")
        # time.sleep(2)
        # text.text("3️⃣. 🪄 Visualizing the relations...")
        # time.sleep(1)
        # text.text("✅ Done with EDA ➡️",help=":blue-background[Report will generate in a while]")
        # status.update(label= ":blue-background[📑 Generating your report]", state='running',expanded=True)
        # pr = ProfileReport(data, minimal=True, explorative=True,title="Profiling Report")
        # export = pr.to_html()
        # status.update(label="Summarize dataset 📝",state='running',expanded=True)
        # time.sleep(1)
        # status.update(label="Generate report structure 📋",state='running',expanded=True)
        # time.sleep(2)
        # status.update(label="Render HTML 🌐",state='running', expanded=True)
        # st_profile_report(pr)
        # 
        # 
        # 
        # 
        # status.update(label=":green-background[📝 Report❗]", state="complete", expanded=False) 
        # 
        # st.info("✅ Check the report and solve the issue then try with cleaned data to train ML models")
    
    # st.download_button(label="── :red[☆]⋅ ⬇️ Download ⋅:red[☆] ──", file_name='Report.html',data=export, mime="text/html",help="📩 :rainbow[Download Full Report]")
        
    train_button = st.button("── :red[☆]⋅ Train ML model⋅:red[☆] ──", help="👇 :rainbow[Click this to train ml model and compare them]")
    if train_button:
        try:
            st.toast(":rainbow[Let the magic begins....]",icon="🪄")
            ml.ML(st.session_state.data)
        except Exception as e:
            st.warning(f"⚠️ Problem with EDA funtion: {e}")
        
    else:
        train_button = True