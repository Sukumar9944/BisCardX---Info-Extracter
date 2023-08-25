# Importing necessary libraries
import streamlit as st
import time
import pandas as pd
from PIL import Image
import io
import easyocr
import numpy as np
import re
import mysql.connector

# Setting Webpage Configurations
st.set_page_config(page_icon="📀",page_title="BisCardX", layout="wide")

# Title
st.title(':red[BisCardX] - Info Extracter 🛡️')

# Extract information
def extract(upload):
    images = Image.open(upload)

    black_image = images.convert('L')
    black_img_np = np.array(black_image)
    read = easyocr.Reader(['en'])
    result = read.readtext(black_img_np,detail = 0)

    phone_list = []
    
    # Patterns
    phonepattern = re.compile(r'\+|[0-9]+[-\s][0-9]+[-\s][0-9]+')
    webpattern = re.compile(r'[Ww]{3}')
    mailpattern = re.compile(r'@')
    addpattern = re.compile(r'\d+\s[a-zA-Z]+')
    pinpattern = re.compile(r'\d{5,6}|(\d{3}\s\d{3})')
    
    names = result[0]

    designations = result[1]
    
    for i in result:
        phone = phonepattern.search(i)
        if phone:
            phone_list.append(i)
                
 
    for i in result:
        mail = mailpattern.search(i)
        if mail:
            mail_ids = i
                  
      
    for i in result:
        web = webpattern.search(i)
        if web:
            websites = i
           
                   
    for i in result:
        add = addpattern.search(i)
        if add:
            addresss = i
                     
      
    for i in result:
        pin= pinpattern.finditer(i)
        for i in pin:
            pincodes = i.group()
           
                       
    return names,designations,'|'.join(phone_list),mail_ids,websites,addresss,pincodes


add_selectbox = st.sidebar.selectbox("HomePage",("Card info Extractor 📀","Extract details","Insert into MySQL Database","View | Update | Delete"))

file_uploader = st.file_uploader('Upload your image')

if file_uploader is not None:
    try:
        file_contents = file_uploader.read()

        # Create a BytesIO object from the file content
        image_bytes = io.BytesIO(file_contents)

        # Open the image using PIL
        open_image = Image.open(image_bytes)

        # Display the uploaded image
        st.image(open_image)
    except Exception as e:
        st.write('Error',e)
else:
    st.write('Please Upload an Image')
    


# Extracted Information
name,designation,phone_no,email_id,website,address,pincode = extract(file_uploader)


extract_button = st.button('Extract') 

if extract_button:
    data = [name,designation,phone_no,email_id,website,address,pincode]
    list1 = []
    list1.append(data) 

    df = pd.DataFrame(list1,columns = ['Name','Designation','Phone_no','Email_id','Website','Address','Pincode'])
    st.dataframe(df)  
                
    st.subheader(f':red[Name] : {name}')
    st.subheader(f':red[Designation] : {designation}')
    st.subheader(f':red[Phone no] : {phone_no}')
    st.subheader(f':red[Email_id] : {email_id}')
    st.subheader(f':red[Website] : {website}')
    st.subheader(f':red[Address] : {address}')
    st.subheader(f':red[Pincode] : {pincode}')


        
if add_selectbox == "Extract details":
    button = st.button('Extract')
    extract_progress_text = "Extraction in progress."

   
    
    with st.spinner('Wait for it...'):
        time.sleep(3)

    data = [name,designation,phone_no,email_id,website,address,pincode]
    list1 = []
    list1.append(data)  

    if button:
        if data:
            extract_bar = st.progress(0, text=extract_progress_text)
            for percent_complete in range(100):
                time.sleep(0.1)
                extract_bar.progress(percent_complete + 1, text=extract_progress_text)

            df = pd.DataFrame(list1,columns = ['Name','Designation','Phone_no','Email_id','Website','Address','Pincode'])
            st.dataframe(df)  
                
            st.subheader(f':red[Name] : {name}')
            st.subheader(f':red[Designation] : {designation}')
            st.subheader(f':red[Phone no] : {phone_no}')
            st.subheader(f':red[Email_id] : {email_id}')
            st.subheader(f':red[Website] : {website}')
            st.subheader(f':red[Address] : {address}')
            st.subheader(f':red[Pincode] : {pincode}')


elif add_selectbox == "Insert into MySQL Database":
    if name:
        st.write(name)       
# try:
#     connection = mysql.connector.connect(
#         host = "localhost",
#         port=3306,
#         user = "root",
#         password = 'Sukumar1234',
#         database = "ocr")
# except:
#     print('Please Check your internet Connection')

# cursor = connection.cursor()

# st.subheader(':red[Upload extracted data into MySql]')

# id = st.text_input('Create a User Id')
# password = st.text_input('Create a Password')

# submit1 = st.button('Upload into MySQL')

# if submit1:
#     if id and password is not None:
#         try:
#             query = 'INSERT INTO biscard_data (id,name,designation,phone_no,website,mail_id,address,pincode,password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);'
#             values = (id,name,designation,phone_no,website,email_id,address,pincode,password)
#             cursor.execute(query,values)
#             connection.commit()    
#             st.success('Data Uploaded Successfully')
#         except:
#             st.error('User Id already exists',icon='🚨')


    

# your_id = st.text_input('Enter your Id')
# your_password = st.text_input('Enter your Password')

# submit2 = st.button('View Details')
# if your_id and your_password is not None:
#     if submit2:
#         query1 = 'select name,designation,phone_no,website,mail_id,address,pincode from biscard_data where id = %s and password = %s;'
#         values = (your_id,your_password)
#         cursor.execute(query1,values)
#         row_data = cursor.fetchall()
#         st.image(resize)
#         df = pd.DataFrame(row_data,columns = cursor.column_names)
#         st.dataframe(df) 
#         st.success('Data fetched Succesfully')

# st.subheader(':red[Update your details]')

# select_options = st.selectbox('select any one field that you want to update',options=['Select any one','name','designation','phone_no','website','mail_id','address','pincode'])

# if select_options == 'name':
#     name = st.text_input('Enter your name')
#     update = st.button('Update your details')
#     if update:
#         update_query = f'UPDATE biscard_data SET name = %s WHERE id = %s and password = %s;'
#         values = (name,your_id,your_password)
#         cursor.execute(update_query,values)
#         connection.commit()
#         st.success('Data Updated Successfully')

# elif select_options == 'designation':
#     designation = st.text_input('Enter your designation')
#     update = st.button('Update your details')
#     if update:
#         update_query = f'UPDATE biscard_data SET designation = %s WHERE id = %s and password = %s;'
#         values = (designation,your_id,your_password)
#         cursor.execute(update_query,values)
#         connection.commit()
#         st.success('Data Updated Successfully')

# elif select_options == 'phone_no':
#     phone_no = st.text_input('Enter your phone_no')
#     update = st.button('Update your details')
#     if update:
#         update_query = f'UPDATE biscard_data SET phone_no = %s WHERE id = %s and password = %s;'
#         values = (phone_no,your_id,your_password)
#         cursor.execute(update_query,values)
#         connection.commit()
#         st.success('Data Updated Successfully')

# elif select_options == 'website':
#     website = st.text_input('Enter your phone_no')
#     update = st.button('Update your details')
#     if update:
#         update_query = f'UPDATE biscard_data SET website = %s WHERE id = %s and password = %s;'
#         values = (website,your_id,your_password)
#         cursor.execute(update_query,values)
#         connection.commit()
#         st.success('Data Updated Successfully')

# elif select_options == 'mail_id':
#     mail_id = st.text_input('Enter your mail_id')
#     update = st.button('Update your details')
#     if update:
#         update_query = f'UPDATE biscard_data SET mail_id = %s WHERE id = %s and password = %s;'
#         values = (mail_id,your_id,your_password)
#         cursor.execute(update_query,values)
#         connection.commit()
#         st.success('Data Updated Successfully')

# elif select_options == 'address':
#     address = st.text_input('Enter your address')
#     update = st.button('Update your details')
#     if update:
#         update_query = f'UPDATE biscard_data SET address = %s WHERE id = %s and password = %s;'
#         values = (address,your_id,your_password)
#         cursor.execute(update_query,values)
#         connection.commit()
#         st.success('Data Updated Successfully')

# elif select_options == 'pincode':
#     pincode = st.text_input('Enter your pincode')
#     update = st.button('Update your details')
#     if update:
#         update_query = f'UPDATE biscard_data SET pincode = %s WHERE id = %s and password = %s;'
#         values = (pincode,your_id,your_password)
#         cursor.execute(update_query,values)
#         connection.commit()
#         st.success('Data Updated Successfully')

# st.subheader(':red[Delete your details]')
# delete_id = st.text_input('Enter your id')
# delete = st.button('Delete your details')
# if delete:
#     delete_query = 'DELETE FROM biscard_data where id = %s;'
#     values = (delete_id,)
#     cursor.execute(delete_query,values)
#     connection.commit()
#     st.success('Data deleted Successfully')

    

    
    




    




