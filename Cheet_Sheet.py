# -----> Required libraries 
import streamlit as st
import pandas as pd
import numpy as np


# -----> Modifying page configurations 
st.set_page_config(layout='wide')

# -----> All functions 

def find_info(obj, function_ask):
    return st.write(getattr(obj,function_ask))
        
def get_help_text(obj, method_name):
    return st.write(getattr(obj, method_name))

def get_configure_column(obj,method_name):
    return st.write(getattr(obj, method_name))

# ---------------------------------------------------------------------------- #
home_tab, heading_tab, write_tab, caption_tab, code_tab, divider_tab, echo_tab, latex_tab, text_tab, data_tab, chart_tab, widgets_tab, pop_over_tab = st.tabs([
    '🏠 Home', '🔠 Heading Elements', '📝 Write Elements', '📑 Caption Element', '💻 Code Element', 
    '➖ Divider Element', '🔍 Echo Element', '📚 Latex Element', '✏️ Text Element', '📊 Data Elements', '📶 Chart Elements',
    '🎛️ Widgets', '📋 Popover Element'
])

with home_tab:
    # -----> page content 
    # Set's the app title
    st.title(":orange[Streamlit Cheat Sheet for Beginners] 📜")
    st.write("꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")

    # For heading
    st.header(":blue[Streamlit - Cheat Sheet]")

    # For Sub heading
    st.subheader(":green[For Absolute Beginners]")

    # You can display any format of text using write() function
    st.write("In this Cheat sheet, I'll cover every function and some basic web codes.")

    # Markdown gives customization for your text like HTML, JS
    st.markdown(":blue[**Streamlit**:] is a widely used open source Python framework, facilitates the creation and "
                "deployment of web apps for Machine Learning and Data Science.")

    st.markdown(":link: Visit [Streamlit](https://streamlit.io/) to learn more about Streamlit.")
    st.error("Streamlit reruns the entire script every time a widget's state changes.")
    st.write(":information_source: Before going further, we need to install Streamlit")

    install_code = '''pip install streamlit'''
    st.code(install_code, language='command')

    st.header(":hammer: Let's try to build some basic Web app.")
    st.subheader(":rocket: How to build a basic Web app to print 'Hello world!' on the web...")

    # -----> code element 
    # CODE = it displays the code as you write
    sample_app = '''
    import streamlit as st
    st.write("Hello world!")
    '''
    st.code(sample_app, language='python')

    st.markdown(":desktop_computer: Now open your terminal and run this code using ***streamlit run filename.py***")

    st.write(":tada: Hurray!.. we just created a web application using Streamlit.")

    st.write("---")
    st.subheader("🔍 Explore the Streamlit library............", help="Expand the list!")
    streamlit_fun = dir(st)
    
    st.code('st.help()')

    # -----> function information code
    st.write("---")
    with st.container(border=True):
        st.subheader(":orange[Need help with any function] 🤔")
        select_option = st.selectbox("Select Option:",streamlit_fun ,index=None)

        if select_option:
            st.subheader(f"Information about '{select_option}'")
            find_info(st,select_option)

with heading_tab:
    # -----> Heading elements 
    st.header("🔠 Heading Elements")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")
    st.write("Streamlit has three types of headings, let's see...")

    st.header("1. Title")
    st.code('''import streamlit as st
st.title(body="output: This is title", help="tool tip", anchor=None)
# body: content of the title
# help: tool tip next to the title
# anchor: link for particular portion in the webpage.-->when we touch the heading, it will navigate to the particular line
''')
    st.write("output: ")
    st.title(body="This is title", help="tool tip", anchor=None)
    st.divider()

    st.header("2. Header")
    st.code('''
            import streamlit as st
    st.header("This is first type, called header.", help="header demo", divider="blue", anchor=None)
    # help: display question mark icon to the right. when we click on it, it will display content for more information or specific reason for that heading
    # divider: draw horizontal line after heading with specified color, by default divider = False)
    ''')
    st.info("divider : bool or “blue”, “green”, “orange”, “red”, “violet”, “gray/grey”, or “rainbow”")
    st.write("output: ")
    st.header("This is first type, called header.", help="header demo", divider='blue', anchor=None)
    st.divider()

    st.header("3. Subheader")
    st.code('''
    import streamlit as st
    st.subheader("This is :blue-background[second type], called :red[sub header].", anchor="https://docs.streamlit.io/get-started", divider="rainbow", help="This is demo of how to use subheader.")
    # :blue-background[content] : display the content with specified background color
    # :red[] : display the text in specified color
    # Note: only below mentioned colors will work
    # colors: [blue, green, orange, red, violet, gray/grey, rainbow]
    # help: display question mark icon to the right. when we click on it, it will display content for more information or specific reason for that heading
    # divider: draw horizontal line after heading with specified color, by default divider = False)
    ''')
    st.write("output: ")
    st.subheader("This is :blue-background[second type], called :red[sub header].", anchor="https://docs.streamlit.io/get-started", divider='rainbow', help="This is demo of how to use subheader.")

    st.write("---")
    st.write("Let's see customized header with markdown")
    st.header("Markdown header",divider='grey')
    st.info("You can provide html format code in the markdown element.")
    with st.echo():
        st.markdown("<h1>This is markdown header h1</h1>", unsafe_allow_html=True)
        st.markdown("<h2>This is markdown header h2</h2>", unsafe_allow_html=True)
        st.markdown("<h3>This is markdown header h3</h3>", unsafe_allow_html=True)
        st.markdown("<h4>This is markdown header h4</h4>", unsafe_allow_html=True)
        st.markdown("<h5>This is markdown header h5</h5>", unsafe_allow_html=True)
        st.markdown("<h6>This is markdown header h6</h6>", unsafe_allow_html=True)
    with st.echo():
        import streamlit as st
        # code taken from Streamlit documentation
        st.markdown("*Streamlit* is **really** ***cool***.") # bold(**content**), italic (*content*) ,bold and italic (***content***)
        st.markdown('''
            :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
            :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''') # colored text
        st.markdown("Here's a bouquet &mdash; :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:") # emojis

with write_tab:
    # -----> Write elements 
    st.header("📝 Write Elements")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")

    st.subheader("Write")
    with st.echo():
        import streamlit as st
        st.write("It used to display any type of content like string, dataframes, tables, functions, emojis, graphs, also supports HTML content using unsafe_allow_html.")

    st.subheader("Write_stream")
    with st.echo():
        import time
        import streamlit as st  

        sample_text = "This text will display in the typewriter format. Like chatgpt, the entire text is displayed as specified with a time delay."

        def stream_data():
            for char in sample_text: # we can specify as character or word or customized content like upto , or @ 
                yield char 
                time.sleep(0.02)

        if st.button("Stream the text"):
            st.write_stream(stream_data)

with caption_tab:
    # -----> Streamlit captions
    st.header("📑 Caption Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")
    st.info("caption which is used to explain the above content, supports italic, bold, italic_bold text, emojis 😎, colored text, background for text, HTML using unsafe_allow_html parameter.")
    with st.echo():
        import streamlit as st
        st.caption("This is the caption which is used to explain the above content, supports *italic*,**bold**, ***italic_bold***, emojis 😎, :rainbow[colored text], :red-background[background] for text, HTML using unsafe_allow_html parameter.")

with code_tab:
    # -----> Code element
    st.header("💻 Code Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")
    st.info("Display a code block with optional syntax highlighting.")
    st.code("""
    import streamlit as st

    code = '''def hello():
        print("Hello, Streamlit!")'''
    st.code(code, language='python')
                """, language='python')

with divider_tab:
    # -----> Divider element
    st.header("➖ Divider Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦")
    st.info("Draw a horizontal line")
    with st.echo():
        import streamlit as st
        st.divider()

    st.write("You can achieve the same with the write element.")
    with st.echo():
        import streamlit as st
        st.write("---")

    st.write("You can also achieve the same with the magic element.")
    with st.echo():
        "---"    
    st.caption("Above horizontal lines are outputs of the codes")

    st.write("---")

with echo_tab:
    # -----> Echo element
    st.header("🔍 Echo Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦")
    st.info("Use in a with block to draw some code on the app, then execute it.")
    with st.echo():
        import streamlit as st
        with st.echo():# code for echo element, always in the "with block"
            st.write("This content will display on the web app as well as this line of code will also be displayed.")

with latex_tab:
    # -----> Latex element
    st.header("📚 Latex Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦")
    st.info("Display mathematical expressions formatted as LaTeX.")
    with st.echo():
        import streamlit as st
        st.latex("(a+b)^2 = a^2+b^2+2ab", help="display formula using latex element")
    
    st.subheader("Latex with markdown element",divider='grey')
    with st.echo():
        import streamlit as st
        st.markdown("$$ (a+b)^2 = a^2+b^2+2ab $$",help="display formula using markdown element") # $$ indicates latex

with text_tab: 
    # -----> Text element
    st.header("✏️ Text Element")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦")
    st.write("Write fixed width and preformatted text.")
    with st.echo():
        st.text("This is the output of streamlit text element.")
    
    st.markdown("<h3 style='font-weight: bold; text-decoration: underline wavy orange;'>💡Pro Tip </h3>",unsafe_allow_html=True)

    with st.echo():
        import streamlit as st  
        import random
        text_element = st.text("sample text.")
        list_of_texts = ['hi', "hello", "namasthe"]
        if st.button("Click for text change"):
            random_text = random.choice(list_of_texts)
            text_element.write(random_text)
            # by clicking the button, the text will change respectively.

with data_tab:    
    # -----> Data elements
    st.header("📊 Data Elements")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒷꒦")
    st.subheader("Dataframe", divider='grey')
    st.info("""You can display dataframes as a table on the web interface easily. users can sort, resize, search, and download the data""")
    with st.echo():
        import pandas as pd
        import streamlit as st
        df = pd.DataFrame(np.random.randn(10, 10), columns=("column %d" % i for i in range(10)))
        st.dataframe(df)
    
    st.info("You can also style the dataframe")
    st.subheader("How to highlight max values in each column", divider='grey')
    
    with st.echo():
        import pandas as pd
        import streamlit as st
        
        df = pd.DataFrame(np.random.randn(10, 10), columns=("column %d" % i for i in range(10)))
        st.dataframe(df.style.highlight_max(axis=0,color='pink'))
        explanation = """
         df.style.highlight_max() object filter the max value 
         axis = 0 means indicating columns [0: columns, 1: rows]
         df.style.highlight_max(axis=0) : highlight the max values of each column
        """
        
    st.header("Want to explore the style objects ❓")
    with st.container(border=True,):
        # Streamlit app layout
        st.subheader(":blue[DataFrame.style Methods Explorer]")
        style_methods = dir(df.style)
# 
        # Dropdown to select a method
        selected_method = st.selectbox("Select a method/attribute:",style_methods,index=None)
        with st.container(border=True):
            # Display detailed help information
            if selected_method:
                st.subheader(f"Information about '{selected_method}'")
               # Capture the help text and display it
                get_help_text(df.style, selected_method)
                
    # -----> dataframes styles 
    st.subheader("Normal Dataframe", divider='grey')
    with st.echo():
        import pandas as pd
        import streamlit as st
        
        df = pd.DataFrame({
            "name" : ['Pushpa-The Rule', 'RRR', 'Bahubali-The beginning','Bahubali- The conclusion'],
            "Rating": [7,8,9,9],
            "Views": [[random.randint(1000, 500000) for _ in range(30)] for _ in range(4)]
        })
        
        st.dataframe(df)
        
    # -----> Custom Dataframe     
    st.subheader("Customized Dataframe using style objects", divider='grey')
    with st.echo():
        import pandas as pd
        import streamlit as st
        
        df = pd.DataFrame({
            "name" : ['Pushpa-The Rule', 'RRR', 'Bahubali-The beginning','Bahubali- The conclusion'],
            "Rating": [7,8,9,9],
            "Views": [[random.randint(1000, 500000) for _ in range(30)] for _ in range(4)]
        })
        st.dataframe(df, column_config={
            "name": "Movie_Name",
            "Rating": st.column_config.NumberColumn(
                "Movie_Rating (out of 10)",
                help="No.of stars for Movie",
                format="%d ⭐"),
            "Views": st.column_config.AreaChartColumn("Views(past 30 days)",y_min=1000,y_max=500000,)

        },hide_index=True)
    
    # -----> Selection of rows and columns 
    st.subheader("Selection of rows and columns",divider='grey')
    st.info("**Usage: ** Display a DataFrame and enable selection of multiple rows and columns, storing selection state in `st.session_state` for persistent changes.")
    with st.echo():
        import streamlit as st
        import pandas as pd 
        
        df = pd.DataFrame({
            "name" : ['Pushpa-The Rule', 'RRR', 'Bahubali-The beginning','Bahubali- The conclusion'],
            "Rating": [7,8,9,9],
            "Views": [[random.randint(1000, 500000) for _ in range(30)] for _ in range(4)]
        })
        
        
        if "df" not in st.session_state:
            st.session_state.df = df
        event = st.dataframe(st.session_state.df,on_select="rerun", selection_mode=['multi-column','multi-row'],key='data')   
        event.selection
    
    st.markdown(":link: Visit [Streamlit Dataframes](https://docs.streamlit.io/develop/api-reference/data/st.dataframe) to learn more about Streamlit Dataframes.")
    
    # -----> Data Editor 
    st.subheader("Data Editor", divider='grey')
    st.info("**Usage: ** Display a user-friendly interface for viewing and editing tabular data.")
    st.write("You can edit dataframe using this element.")
    with st.echo():
        import streamlit as st  
        
        data = {"name": ['satwik', 'pardhi', 'bujji', 'lokesh'], "bday": [13, 11, 30, 11]}
        st.data_editor(data) 
    
    # -----> Column 
    st.subheader("Dynamic rows for dataframe using st.column_config.Column",divider='grey')
    st.info("**Usage: ** Configure dynamic rows for displaying and editing DataFrame columns.")
    with st.echo():
        import streamlit as st
        
        data = {"name": ['satwik', 'pardhi', 'bujji', 'lokesh'], "bday": [13, 11, 30, 11]}
        st.data_editor(data,
                       column_config={
                               "name": st.column_config.Column(
                               "User Name", # New column name
                               help='Names of the user(hover effect)',
                               width='medium',#[large, medium, small] # width of that column
                               required= True # specifies whether the edited cell can be empty or required any value
                               )
                       }
                       ,hide_index=True
                       ,num_rows="dynamic" # ['dynamic','fixed'(by defualt)] 
                       # specifies the interactivity of dataframe like actions for add or remove rows 
                       )
    st.info("+ ➕ icon indicates --> add row. You can delete row, by selecting it and click delete icon on top right corner.")
    
    # -----> Text column 
    st.subheader("Configuration of Text Column",divider='grey')
    st.info("**Usage: ** Display and edit text values, with validation for entered input text.")
    with st.echo():
        import streamlit as st
        import pandas as pd
        
        data = pd.DataFrame({
            "Email": ['uppadasatwik@gmail.com','satwikuppada@gmail.com','lokesh69@gmail.com', 'uppada_12111298@gmail.com']
        })
        
        st.data_editor(
            data,
            column_config={
                "Email": st.column_config.TextColumn(
                    "Email Address",
                    help="Enter your email address",
                    default='@gmail.com', # add DEFAULT TEXT in new rows
                    max_chars=50,
                    validate="^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$", # It wont save if the text don't obey this format
                    required=True # Specifies compuslary requirement of filling details in the cell
                )
            },
            hide_index=True,
            num_rows="dynamic"
        )
    
    # -----> Number Column
    st.subheader("Configuration of Number Column",divider='grey')
    st.info("**Usage: ** Display numerical values, allowing users to input and edit numbers.")
    with st.echo():
        import streamlit as st
        import pandas as pd
        data = pd.DataFrame({
            "Age": [20, 21, 22, 23],
            "salary":[20000,30000,40000,50000]
            })
        
        st.data_editor(
            data,
            column_config={
                "Age": st.column_config.NumberColumn(
                    "User Age",
                    help="Enter your age",
                    min_value=2,
                    max_value=100,
                    step=1,
                    format='%d years',
                    required=True
                ),
                "salary":st.column_config.NumberColumn(
                    "Salary (in USD)",
                    format="$ %d",
                )
            },
            num_rows='dynamic',
            hide_index= True    
        )
        
    # ----->  Checkbox Column
    st.subheader("Configuration of Checkbox Column",divider='grey')
    st.info("**Usage: **Display True/False column in the form of checkboxes.")
    with st.echo():
        import streamlit as st
        import pandas as pd
        
        data_df = pd.DataFrame(
            {
            "Trip_List": ["Clothes_package", "Food_package", "Traveling_Tickets", "Cab_booking"],
            "Done/Will Done": [False, False, True, True],
            }
        )

        st.data_editor(data_df,
                       column_config={
                           "Done/Will Done": st.column_config.CheckboxColumn(
                               "Done/Will Done ?",
                               help="Select the one which you **Done**",
                               default=False),  
                       },
                       disabled=['Trip_list'],
                       hide_index=True,
                       num_rows="dynamic" # YOU CAN ADD NEW ITEMS
                       )
    
    # -----> Selectbox Column
    st.subheader("Configuration of Selectbox Column",divider='grey')
    st.info("**Usage: ** Display a column as a dropdown (select box) with predefined options. Users need to select an option from the list.")
    st.caption("**Double click on the cell to display the drop down for already filled cells.**")
    with st.echo():
        import pandas as pd
        import streamlit as st

        data_df = pd.DataFrame(
            {
                "Course": ["CSE","MEC",'ECE','EEE','IT','CE']
            }
        )

        st.data_editor(
            data_df,
            column_config={
                "Course": st.column_config.SelectboxColumn(
                    "Course",
                    help="The category of the Course in B.Tech",
                    width="medium",
                    options= ["CSE","MEC",'ECE','EEE','IT','CE'], # You can only insert content specified in the list
                    required=True,
                )
            },
            hide_index=True,
            num_rows="dynamic"
        )
    
    # -----> Datetime Column
    st.subheader("Configuration of Datetime Column",divider='grey')
    st.info("**Usage: ** Display the column content in date-time format. Allow users to input data using a calendar and time selector, which will then be converted into date-time format.")
    with st.echo():
        import pandas as pd
        import streamlit as st
        from datetime import datetime
        
        data = pd.DataFrame({"Name":["Satwik","Lokesh"],
                             "DOB":[datetime(2003, 8, 13, 12, 30),datetime(2005,5,11,18,0)]})
        
        st.data_editor(data, 
                       column_config={
                           "DOB":st.column_config.DatetimeColumn(
                               "DOB",
                               min_value=datetime(1990,1,1),
                               max_value=datetime(2030,12,31),
                               format="D MMM YYYY, h:mm a",
                               step=60,
                           )},hide_index=True, num_rows="dynamic")
        
    # -----> Date Column
    st.subheader("Configuration of Date Column",divider='grey')
    st.info("**Usage: ** Display the column content in date format. Allow users to input data using a calendar, which will then be converted into date format.")
    with st.echo():
        import pandas as pd
        import streamlit as st
        from datetime import date
        
        data = pd.DataFrame({"Name":["Satwik","Lokesh"],
                             "DOB":[datetime(2003, 8, 13),datetime(2005,5,11)]})
        
        st.data_editor(data, 
                       column_config={
                           "DOB":st.column_config.DateColumn(
                               "DOB",
                               min_value=datetime(1990,1,1),
                               max_value=datetime(2030,12,31),
                               format="DD-MM-YYYY",
                               step=1,
                           )},hide_index=True, num_rows="dynamic")
        
    # ----->  Time Column
    st.subheader("Configuration of Time Column",divider='grey')
    st.info("**Usage: ** Display the column-content in time format. Allow users to input data using time selector, which willl then be converted into time format.")
    with st.echo():
        import pandas as pd
        import streamlit as st
        from datetime import time
        
        data = pd.DataFrame({"Train_No":['16031','16032','21533'],
                             "Arrival": [time(3,30),time(12,25),time(9,50)]})
        
        st.data_editor(data,
                       column_config={
                           "Arrival": st.column_config.TimeColumn(
                               "Arrival",
                               min_value=time(0,0),
                               max_value=time(23,59),
                               format="HH:mm a",
                               step=60,
                           )
                       },hide_index=True,num_rows='dynamic')

    # -----> List Column
    st.subheader("Configuration of List Column",divider='grey')
    st.info("**Usage: ** Display the content as list-like values, allowing users to view multiple values within a single cell(read-only format).")
    with st.echo():
        import pandas as pd
        import streamlit as st
        
        data = {
            'Name': ['Satwik', 'Lokesh', 'Pardhi'],
            'Hobbies': [['Coding', 'Cycling'], ['Cooking'], ['Cooking', 'Drawing']],
            'Age': [21, 20, 21]
            }
        
        st.data_editor(data,column_config={
            "Hobbies": st.column_config.ListColumn(
                "Hobbies",
                help="Hobbies of each individual",
                width="medium",
            )
        },hide_index=True,num_rows='dynamic')
      
    st.warning("**:grey[Listcolumn is not able to add new rows. and not editable.]**")
    
    # -----> Link column
    st.subheader("Configuration of Link Column",divider='grey')
    st.info("**Usage: ** Display the content as hyperlinks.")
    with st.echo():
        import pandas as pd
        import streamlit as st
        
        data = pd.DataFrame({"Name": ['Satwik','Pardhiva'],
                             "Linkedin_Profiles":['https://www.linkedin.com/in/satwik-uppada/','https://www.linkedin.com/in/pardhiva-mallu/']}
                            )
        st.data_editor(data,column_config={
            "Linkedin_Profiles": st.column_config.LinkColumn(
                "Linkedin Profile",
                help="Linkedin Profile of each individual",
                validate="^https://www.linkedin.com/in/+[A-z_0-9]+/", 
                # structure of the input that can be considered for saving
                max_chars= 50, # length of the input in this column
                display_text="Open Profile" # display alter text for complete links
            )
        },hide_index=True,num_rows='dynamic')
        
    # ----->  Image Column
    st.subheader("Configuration of Image column",divider='grey')
    st.info("**Usage: ** Display a column containing images.")
    with st.echo():
        import pandas as pd
        import streamlit as st

        data_df = pd.DataFrame(
            {
                "images": [
                    "https://www.shutterstock.com/shutterstock/photos/2190358695/display_1500/stock-photo-a-woman-s-hand-and-a-fern-leaf-man-and-nature-2190358695.jpg",
                    "https://www.shutterstock.com/shutterstock/photos/1957579246/display_1500/stock-photo-early-morning-sunrise-over-the-sea-some-clouds-1957579246.jpg"
                ]
            }
        )

        st.data_editor(
            data_df,
            column_config={
                "images": st.column_config.ImageColumn(
                    "Preview Image", help="Streamlit allow you to preview the images",
                    width= 300 # column width
                )
            },
            hide_index=True,
        )
    
    # -----> Chart Columns
    with st.container(border=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.subheader("Configuration of Area Chart Column",divider='grey')
            with st.echo():
                import pandas as pd
                import streamlit as st

                df = pd.DataFrame({
                    "name" : ['Pushpa-The Rule', 'RRR', 'Bahubali-The beginning','Bahubali- The conclusion'],
                    "Rating": [7,8,9,9],
                    "Views": [[random.randint(1000, 500000) for _ in range(30)] for _ in range(4)]
                })
                st.dataframe(df, column_config={
                    "name": "Movie_Name",
                    "Rating": st.column_config.NumberColumn(
                        "Movie_Rating (out of 10)",
                        help="No.of stars for Movie",
                        format="%d ⭐",width='small'),
                    "Views": st.column_config.AreaChartColumn("Views(past 30 days)",y_min=1000,y_max=500000,width='large')

                },hide_index=True, width=700)

        with col2:
            st.subheader("Configuration of Line Chart Column",divider='grey')
            with st.echo():
                import pandas as pd
                import streamlit as st

                df = pd.DataFrame({
                    "name" : ['Pushpa-The Rule', 'RRR', 'Bahubali-The beginning','Bahubali- The conclusion'],
                    "Rating": [7,8,9,9],
                    "Views": [[random.randint(1000, 500000) for _ in range(30)] for _ in range(4)]
                })
                st.dataframe(df, column_config={
                    "name": "Movie_Name",
                    "Rating": st.column_config.NumberColumn(
                        "Movie_Rating (out of 10)",
                        help="No.of stars for Movie",
                        format="%d ⭐",width='small'),
                    "Views": st.column_config.LineChartColumn("Views(past 30 days)",y_min=1000,y_max=500000,width='large')

                },hide_index=True, width=700)

        with col3:
            st.subheader("Configuration of Bar Chart Column",divider='grey')
            with st.echo():
                import pandas as pd
                import streamlit as st

                df = pd.DataFrame({
                    "name" : ['Pushpa-The Rule', 'RRR', 'Bahubali-The beginning','Bahubali- The conclusion'],
                    "Rating": [7,8,9,9],
                    "Views": [[random.randint(1000, 500000) for _ in range(30)] for _ in range(4)]
                })
                st.dataframe(df, column_config={
                    "name": "Movie_Name",
                    "Rating": st.column_config.NumberColumn(
                        "Movie_Rating (out of 10)",
                        help="No.of stars for Movie",
                        format="%d ⭐",width='small'),
                    "Views": st.column_config.BarChartColumn("Views(past 30 days)",y_min=1000,y_max=500000,width='large')

                },hide_index=True, width=700)
        
    # -----> Progress bar
    st.subheader("Configuration of ProgressBar Column",divider='grey')
    st.info("Show the number input in the form of progress bar.")
    st.warning(":red[**NOTE**]: Progress columns are not editable.")
    
    with st.echo():
        import streamlit as st
        import pandas as pd
        data = pd.DataFrame({
            "Name": ['Satwik','Lokesh','Pardhi','Chinni'],
            'Marks':[50,85,90,100]
        })
        
        st.data_editor(data,column_config={
            'Marks':st.column_config.ProgressColumn(
                'Marks(out of 100)',
                help='Marks gained in exam',
                format='%d%% marks',
                min_value=0,
                max_value=100,width='medium'
            )
        },
        hide_index=True,
        num_rows='dynamic' 
        # Only names can be editable and dynamic, progress column is not editable and will not take user input
        )
    
    
    st.error("You can see that, ProgressBar column is not editable and will not take new values")
    
    
    # -----> Column config search 
    with st.container(border=True):
        st.success("**These functions are used for both *:red[st.dataframe]* and *:red[st.data_editor]***")
        st.subheader(":orange[Need help with any Method/function in column_config] 🤔")
        streamlit_column_config_fun = dir(st.column_config)
        select_option = st.selectbox("Select Option:",streamlit_column_config_fun ,index=None)
        with st.container(border=True):
            if select_option:
                st.subheader(f"Information about '{select_option}'")
                get_configure_column(st.column_config,select_option)

    
    # -----> Add rows using table element
    st.header("Table",divider='grey')
    st.subheader("Adding rows to the existed dataframe")
    st.info("**Usage: ** Add rows to an existing DataFrame displayed in a table.")
    with st.echo():
        import streamlit as st
        import pandas as pd 
        
        df_1 = pd.DataFrame({
            "name" : ['Pushpa-The Rule', 'RRR', 'Bahubali-The beginning','Bahubali- The conclusion'],
            "Rating": [7,8,9,9],
            "Views": [[random.randint(1000, 500000) for _ in range(30)] for _ in range(4)]
        })
        
        my_table = st.table(df_1)
        
        df_2 = pd.DataFrame({
            "name" : ['Jawan', 'Kalki-2898 AD', 'Salar','Bee Keeper'],
            "Rating": [7,9,9,6],
            "Views": [[random.randint(1000, 500000) for _ in range(30)] for _ in range(4)]
        })
        
        my_table.add_rows(df_2)
    
    # -----> add data to plots 
    st.header("Adding more data to plots",divider='grey')
    st.subheader("Initial Data points")
    with st.echo():
        import streamlit as st
        import pandas as pd 
        df_1 = pd.DataFrame([1,5,2,4])
        
        st.line_chart(df_1)
    st.subheader("Chart after adding new data points")
    with st.echo():
        import streamlit as st
        import pandas as pd 

        df_1 = pd.DataFrame([1,5,2,4])
        df_2 = pd.DataFrame([3,6,9,8])

        my_chart = st.line_chart(df_1)
        my_chart.add_rows(df_2)
        
    # -----> Metric elements
    st.header("Metric elements",divider='grey')
    st.info("Displays a metric value with an optional delta to show changes. It can indicate positive and negative trends with colored indicators.")

    with st.echo():
        import streamlit as st
        with st.container(border = True):
            col1, col2, col3,col4,col5,col6 = st.columns(6)
            col1.metric(label=":red[positive delta]", value="25 °C", delta="1°C") 
            col2.metric(label=":blue[negative delta]",value="58%",delta='-1%')
            col3.metric(label=":green-backgroundp[delta_color_ inverse]",value = "9 mph",delta="- 8%", delta_color = "inverse")
            col4.metric(label=":green-backgroundp[delta_color_off]",value = "9 mph",delta="- 8%", delta_color = "off")
            col5.metric(label="Active users",value=45,delta=2,label_visibility='collapsed',help="Label is collapsed")
            col6.metric(label="Active users",value=45,delta=2,label_visibility='hidden',help="label is hidden")
            info = """
            label: title of the metric
            value: current value of the metric
            delta: change in the metric (neg values show down arrow(red color), positive show up arrow(green color))
            delta_color: color of the delta (normal, inverse(reverse the delta(change to opposite color)), off)
            label_visibility: visibility of the label (visible(show the container), collapsed(remove that container), hidden(hide the container))
            """
    
    # -----> Json element
    st.header("Json element",divider='grey')
    st.info("Display object or string as a pretty-printed JSON string.")
    with st.echo():
        import streamlit as st

        st.json({
            "name":"satwik",
            "college": "LPU",
            "Reg No": 12111298,
            "courses_in_sem_5":['Machine Learning','Deep Learning','Cloud computing','Statistics']
        },expanded=True # expanded: specifies the whether list is to be expand or collapse [True, False]
        )

# -----> Chart tab 
with chart_tab:
    st.header("📶 Chart Elements")
    st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")
    area,bar,line,map,scatter,altair,bokeh,graphviz,plotly,pydeck,pyplot,vega_lite =st.tabs(
["Area Chart",
"Bar Chart",
"Line_chart",
"Map",
"Scatter_chart",
"Altair_chart",
"Bokeh_chart",
"Graphviz_chart",
"Plotly_chart",
"Pydeck_chart",
"Pyplot",
"Vega_lite_chart"])
    with area:
        with st.container(border=True):
            # -----> Area chart
            st.subheader("Area Chart", divider="grey")
            st.info("Display Area chart for the given data.")
            with st.echo():
                import streamlit as st
                import pandas as pd

                # Creating a dummy DataFrame
                data = {
                    'Month': ['January', 'February', 'March', 'April', 'May'],
                    'Product A': [100, 150, 200, 250, 300],
                    'Product B': [80, 130, 180, 230, 280],
                }

                df = pd.DataFrame(data)

                # Plotting the area chart
                st.area_chart(df.set_index('Month'))
            with st.expander("Want to learn more about Area Charts"): 
                st.subheader("How to change default colours of the graph with custom colors?",divider='orange')
                with st.echo():
                    st.area_chart(df, x = 'Month',y='Product A',color='#1995ad')# specify color of the plot
                st.subheader("How to assign different colors according to category by default?",divider='orange')
                with st.echo():
                    st.area_chart(df, x='Month', y=['Product A','Product B'],color='Month')# gives random default colors
                    info = """
                    color: gives random default colors for n no.of months
                    width: specifies the width of the plot
                    use_container_width : specifies the use of width you specified or width of the parent container. [True, False]"""
                st.subheader("How to assign custom colors to categories",divider='orange')
                with st.echo():
                    st.area_chart(df, x='Month', y=['Product A','Product B'],color=['#f7f7','#1995ad']) # specified custom colors

                st.subheader("How to customize the plot height, width and direction?",divider='orange')
                with st.echo():
                    st.area_chart(df.set_index("Month").T,height=500, width=700,use_container_width=False)
                    info = "T stands for transpose"

    with bar:
        with st.container(border=True):  
                  
            # -----> Bar charts 
            st.subheader('Bar Chart',divider='grey')
            st.info("Display bar graph for the given data.")
            with st.echo():
                import streamlit as st
                import pandas as pd

                # Creating a dummy DataFrame
                data = {
                    'Month': ['January', 'February', 'March', 'April', 'May'],
                    'Product A': [100, 150, 200, 250, 300],
                    'Product B': [80, 130, 180, 230, 280],
                }

                df = pd.DataFrame(data) 
                
                # Plotting the bar chart
                st.bar_chart(df.set_index("Month"))
                
            with st.expander("Want to learn more about Bar Charts"):   
                st.subheader("How to change default colours of the graph with custom colors?",divider='orange')
                with st.echo():
                    st.bar_chart(df, x = 'Month',y='Product A',color='#1995ad',width=700,use_container_width=False)# specify color of the plot

                st.subheader("How to assign different colors according to category by default?",divider='orange')
                with st.echo():
                    st.bar_chart(df, x='Month', y=['Product A','Product B'],color='Month',width=700,use_container_width=False)

                st.subheader("How to assign custom colors to categories",divider='orange')
                with st.echo():
                    st.bar_chart(df, x='Month', y=['Product A','Product B'],color=['#f7f7','#1995ad'],width=700,use_container_width=False) # specified custom colors

                st.subheader("How to customize the plot height and width?",divider='orange')
                with st.echo():
                    st.bar_chart(df.set_index("Month").T,height=500,width=700,use_container_width=False)

    with line:
        with st.container(border = True):
                                                
                                                                                                                                    
            st.subheader("Line Chart",divider = "grey")
            with st.echo(): 
                import streamlit as st
                import pandas as pd
                import numpy as np
                
                np.random.seed(42)
                dates = pd.date_range(start='2023-01-01', periods=100)
                data = {
                    'Date': dates,
                    'Product A Sales': np.random.randint(50, 200, size=100),
                    'Product B Sales': np.random.randint(30, 180, size=100),
                    'Product C Sales': np.random.randint(20, 150, size=100),
                    'Product D Sales': np.random.randint(10, 120, size=100),
                    'Revenue': np.random.randint(1000, 5000, size=100),
                    'Cost': np.random.randint(500, 3000, size=100)
                }
                
                df = pd.DataFrame(data)
                
                st.line_chart(df.set_index('Date')[['Product A Sales', 'Product B Sales', 'Product C Sales', 'Product D Sales']])
            with st.expander("Want to learn more about line charts"):
                with st.echo():
                    import pandas as pd
                    import streamlit as st

                    # Sample data
                    df = pd.DataFrame({'x': [1, 2, 3, 4, 5,6,7,8,9,10], 'y1': [2, 5, 7, 1, 3, 10, 9, 8, 6, 4], 'y2': [4, 6, 2, 8, 1, 7, 10, 5, 9, 3]})

                    # Customize line colors
                    colors = ['#ff9999', '#66b3ff']  # Red and blue for y1 and y2

                    st.line_chart(df, x='x', y=['y1', 'y2'], height=500, width=900, color=colors, use_container_width=False)                                                                               
    with map:
        with st.container(border = True):
            with st.echo():
                import streamlit as st  
                import pandas as pd
                import random
                
                # Define state names
                states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh"]

                # Generate random population data
                population = [37878176, 1327174, 32753261, 95143727, 22631084]  # Millions

                # Generate random latitude and longitude (adjust ranges as needed)
                lat = [15.9240905, 28.0937702, 26.4073841, 25.6440845, 21.6637359 ]
                lon = [80.1863809, 94.5921326, 93.2551303, 85.906508, 81.8406351 ]

                # Create DataFrame
                df = pd.DataFrame({
                    "State": states,
                    "Population": population,
                    "Lat": lat,
                    "Lon": lon
                })
                
                st.dataframe(df.style.set_properties(align='center'))
                
                st.title("India State Population Distribution")
                st.map(df, latitude='Lat', longitude='Lon', zoom=4, color='#ff9999')


                

    with scatter:
        with st.container(border = True):
            pass
    with altair:
        with st.container(border = True):
            pass
    with bokeh:
        with st.container(border = True):
            pass
    with graphviz:
        with st.container(border = True):
            pass
    with plotly:
        with st.container(border = True):
            pass
    with pydeck:
        with st.container(border = True):
            pass
    with pyplot:
        with st.container(border = True):
            pass
    with vega_lite:
        with st.container(border = True):
            pass

# ---------------------------------------------------------------------------- #
# -----> Widgets
with widgets_tab:
    st.error("Streamlit reruns the entire script every time a widget's state changes.")

    buttons_tab, selections_tab, numeric_tab, data_time_tab, text_input_tab, media_tab = st.tabs(['Buttons', 'Selections', 'Numeric', 'Date & time', 'Text', 'Media & Files'])
    with buttons_tab:
        st.title("🅱 Streamlit Buttons")

        st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦")
        st.header("Button",divider="grey")
        st.info("Display a button widget.")
        with st.container(border = True):
            
            
            # -----> Primary button 
            st.subheader("1. Primary Button",divider="rainbow")
            st.info("Button widget with additional visual emphasis. - used for important actions")
            with st.echo():

                result = st.button("Primary Button",type='primary')
                st.write("Current state of button: ",result)
                if result:
                    st.success("Button clicked, You can see the state changed to True")

            # -----> Secondary button 
            st.subheader("Secondary button", divider='rainbow')
            st.info("Button with less emphasis")
            with st.echo():
                @st.experimental_fragment
                def function_name_1():
                    st.snow()

                st.button(label="Secondary Button!", help="help uses for hover effect to display information", on_click= function_name_1,type="secondary")

                info = '''
                label:  button name(we can use emojis, text color, background color).
                key:    unique key for a specific button.
                type:   [primary(having additional emphasis) or secondary(default)].
                help:   it gives specialized content on hovering over the button.
                on_click: it's a callable function.
                args:    gives function arguments in the form of a tuple.
                kwargs:     gives function arguments in the form of a dictionary.
                disabled:   which disables the button (True, False)
                use_container_width:     specifies the button width as default or width of the parent container (True, False[default])
                '''
            
        st.header("Download Button",divider='grey')
                    
        st.info("Display the download button widget")
        with st.container(border=True):
            
            
            st.subheader("Download a string as a file",divider='rainbow')
            with st.echo():
                st.download_button(label="Download", data="This is the demo file for download button, this is how the text data will download as a file.", file_name="hello.txt", mime='text/csv',type='primary')
                info = '''
                label:  button name(we can use emojis, text color, background color).
                data: content of the file to downloaded.
                file_name: file_name which the downloaded content saved as.
                mime: specifing that content is text/image with its file extension
                key:    unique key for a specific button.
                type:   [primary(having additional emphasis) or secondary(default)].
                help:   it gives specialized content on hovering over the button.
                on_click: it's a callable function.
                args:    gives function arguments in the form of a tuple.
                kwargs:     gives function arguments in the form of a dictionary.
                disabled:   which disables the button (True, False)
                use_container_width:     specifies the button width as default or width of the parent container (True, False[default])
                '''
            st.subheader("Download image as a file",divider='rainbow')
            with st.echo(""):
                with open("C:\\Users\\uppada satwik\\Downloads\\car.jpg",'rb') as image:
                    st.download_button(label="Download", data=image,file_name="Thankyou_image.jpg",type='secondary')
                    
            st.subheader("Download binary file",divider='rainbow')
            with st.echo():
                example_text = b'a b c d e f'
                st.download_button("Download",data = example_text)
            
            st.subheader("Download dataframe as a csv file",divider='rainbow')
            with st.echo():
                data = pd.DataFrame({
                                     'Name':['satwik','pardhi','lokesh','chinni'],
                                     'age': [21,21,20,22]
                                    }
                                   )
                data = data.to_csv()
                
                st.download_button('Download',data,file_name='dataset.csv',mime='text/csv')
            
    with selections_tab:
        st.header("🗳️ Streamlit Selections")
        st.write("꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷")
        
        with st.echo():
            pass
            
# ---------------------------------------------------------------------------- #
with pop_over_tab:
    popover = st.popover("Filter items")
    red = popover.checkbox("Show red items.", True)
    blue = popover.checkbox("Show blue items.", True)

    if red:
        st.write(":red[This is a red item.]")
    if blue:
        st.write(":blue[This is a blue item.]")

    code ="""
    popover = st.popover("Filter items")
    red = popover.checkbox("Show red items.", True)
    blue = popover.checkbox("Show blue items.", True)

    if red:
        st.write(":red[This is a red item.]")
    if blue:
        st.write(":blue[This is a blue item.]")
    """
    st.code(code, language='python')
