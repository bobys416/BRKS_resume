from pathlib import Path

import streamlit as st 
from PIL import Image

# -- path setting ----#

current_dir= Path(__file__).parent if "_file_" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir/"assets"/"Rishabh Kumar Sharma.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"




# -- General settings ---- #

Page_Title = "Resume | Rishabh Kumar Sharma"
Page_Icon=":random:"
Name="Rishabh Kumar Sharma"
Description=""" Data Analyst , assiting enterprises by supporting data-driven decision-making"""
Email = "bobys416@hotmail.com"
Contact = "+918853043355/+918318125818"
Social_Media_Links= {
    "skype":"bobys416@hotmail.com",
    "instagram":"https://www.instagram.com/brks.sharma415",
    "github": "https://github.com/bobys416"
} 

Projects = {
    "Project 1": "https://github.com",
    "Project 2": "https://github.com",
    "Project 3": "https://github.com"
}

st.set_page_config(page_title=Page_Title, page_icon=Page_Icon)

#--- Load css, PDF & Profile Pic ------
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html= True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte= pdf_file.read()

profile_pic=Image.open(profile_pic) 

# -- HERO Section ----
col1, col2 = st.columns(2, gap="small")
with col1:
     st.image(profile_pic, width=230)

with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label=" Download Resume",
        data=PDFbyte,
        file_name="Rishabh Kumar Sharma Resume.pdf",
        mime="application/octet-stream",
    )

    st.write("📬",Email)

    # -- Social Links ---

    st.write("#")
    cols=st.columns(len(Social_Media_Links))
    for index, (platform, link) in enumerate(Social_Media_Links.items()):
        cols[index].write(f"[{platform}]({link})")

#--- Experience & Qualifications---
        
st.write("#")
st.subheader("Experience & Qualifications")
st.write("""
 🧑‍💻  Data Analyst in Digivatelabs                                                                    Feb '22 - Nov '23 
    - Grid Infocom Pvt.Ltd Gurugram, IN 
   - • Utilized data visualization tools to effectively communicate business insights. 
   - • Analysed transactions to build logical business intelligence model for real-time reporting needs. 
   - • Exhibited respect, friendliness and willingness to help wherever needed. 
   - • Examined information to determine and resolve issues, providing effective solutions. 
   - • Worked flexible hours across night, weekend, and holiday shifts to ensure coverage and meet customer needs. 
   - • Produced monthly reports using Advanced Excel spreadsheet functions. 
   - • Conceived various Excel documents to assist with pulling metrics data and presenting information to stakeholders for concise 
     explanations of best placement for needed resources. 
   - • Determined, analysed and interpreted trends or patterns in complex data sets. 

 -  🧑‍💻 Technical Support Engineer                                                      
   -  Grid Infocom Pvt.Ltd Gurugram, IN 
   - Projects- DQF NG, DQF Legacy, Anota, Peregrine, and CSPI 
   -  System Administrator and Application Support 
   -  OS used: CentOS, Ubuntu and Windows 
   - • Configure full application and database according to project requirement. 
   - • Troubleshooting L1 issues involves identifying and resolving basic issues with the server or application. 
   - • Escalating L2 and L3 issues: If the issue is more complex, it may need to be escalated to a higher level team for resolution. 
   - • Configuring and troubleshooting databases : This includes both SQL and Non-SQL databases. 
   - • Supporting Linux and Windows servers: This includes configuring and fixing the operating system and related software. 
   - • Technical Support Engineer :- Web and server based Application, Python ,Angular, React based application 
   - • Quality Assurance :- Writing Manual test cases and testing applications 
   - • Installed important security and functionality patches to maintain optimal protections against intrusion and system reliability. 
   - • Established network specifications and analysed workflow, access, information and security requirements. 
   - • Monitored temperature and power draw to immediately detect faults and failures. 
   - • Achieved maximum system availability by designing and implementing contingency plans. 
   - • Monitored networks and network devices to resolve technical problems quickly. 
   - • Performed backup of servers and systems, including restoring dumps and applying patches. 
   - • Manage and configure Outlook settings to optimize functionality and resolve bugs and configure Outlook settings to optimize functionality and resolve bugs
""")

#--- Education Section ----
st.write("#")
st.subheader("Education")
st.write("""
         - Advance Certification in Data Science Nov '22 - Sep '23 
         - IIIT Bangalore & upGrad Bengaluru, IN 
            • Course Modules: 
            - -○ Data Analysis using SQL | Introduction to Python | Introduction to Machine Learning and Linear Regression 
            - ○ Time Series Analysis | Telecom Churn Case Study | Lexical Processing | Syntactic Processing 
            - ○ Business Problem Assignment | PowerBi and Tableau  
        - Bachelor of Technology in Computer Science                Jul '16 - Sep '21 
        -    Babu Banarasi Das Engineering College Lucknow , IN 
        - Higher Secondary School                                   Apr '16 - Jul '17 
        - Saraswati Intermediate College Naharapur Gorakhpur Gorakhpur, IN 
        - Senior Secondary School                                   Apr '14 - Jul '15 
        -  Kendriya Viyalaya No.2 F.C.I Gorakhpur Gorakhpur, IN
    """)


#--SKills---
st.write("#")
st.subheader("Technical Skills")
st.write("""
 - Tools/Languages: Python, C/C++, Java, SQL, PowerBi , Tableau ,Oracle Analytics , NodeJs, MERN/MEAN stack ,MS Office, Apache Spark 
 - Database: MongoDb, MS SQL Server, MySQL, PostgreSQL, SQLite 
 - Operating System :Windows ,Linux , Unix 
 - MS Excel (Advance), Outlook 
 - Cloud : AWS and Azure 
 - Technology used : Databricks, Visual Studio Code , Eclipse, Unity, Visual Studio, MS Sql server, Github , Oracle Analytics Cloud """)