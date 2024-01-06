
import base64
import json
import os


import uuid
from flask import url_for
from tests.auto.generic_tests import generic_tests
from base64 import b64encode

class tests_sys_unit(generic_tests):
        
#===========================================================
#SYS_UNI
#===========================================================

    #====================
    
    def test_Sys_unit_001_create(self):
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
                "id": str(uuidCreate),
                "active": "S",
                "name": "Test"+str(uuidCreate),
                "sigla_unit": "TST"+str(uuidCreate)
            }
        
        response = self.client.post(url_for('sysunit.save'), json=req_post, headers=token)
        sys_unit_id1 = json.loads(response.data.decode())['id']
        self.session.set("sys_unit_id1",sys_unit_id1)
        
        self.assertEqual(response.status_code, 201,"Sys_unit_001 code 201") 

    #====================

    def test_Sys_unit_002_create(self):
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        
        req_post ={
                "id": str(uuidCreate) ,
                "active": "S",
                "name": "Test"+str(uuidCreate),
                "sigla_unit": "TST"+str(uuidCreate)
            }
        
        response = self.client.post(url_for('sysunit.save'), json=req_post, headers=token)
        sys_unit_id2 = json.loads(response.data.decode())['id']
        self.session.set("sys_unit_id2",sys_unit_id2)
        

        self.assertEqual(response.status_code, 201 ,"Sys_unit_002 code 201")
    
    #====================

    def test_Sys_unit_get(self):
        
        token = self.create_token()
        response = self.client.get(
            url_for('sysunit.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "Sys_unit_002 code 200") 

    #====================

    def test_Sys_unit_get_by_id(self):

            token = self.create_token()
            response = self.client.get(url_for('sysunit.find_by_id',id=self.session.get("sys_unit_id1")), headers=token)

            self.assertEqual(response.status_code, 200, "Sys_unit_001 code 200") 

    #====================

    def test_Sys_unit_delete(self):
        
        token = self.create_token()

        response = self.client.delete(url_for('sysunit.delete',id=self.session.get("sys_unit_id1")), headers=token)

        self.assertEqual(response.status_code, 204, "Sys_unit_001 code 204")  


#===========================================================
# SYS
#===========================================================

    #====================

    def test_Sys_001_create(self):
       
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
                 "id": str(uuidCreate),
                "name": "TST"
             }
    
        response = self.client.post(url_for('sys.save'), json=req_post, headers=token)
    
        tests_id1_sys = str( json.loads(response.data.decode())['id'])
        self.session.set("tests_id1_sys",tests_id1_sys)
        
        self.assertEqual(response.status_code, 201, "Sys_001 code 201")

    #====================

    def test_Sys_002_create(self):
        
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
                 "id": str(uuidCreate),
                "name": "TST"
            }
    
        response = self.client.post(url_for('sys.save'), json=req_post, headers=token)
    
        tests_id2_sys = str( json.loads(response.data.decode())['id'])
        self.session.set("tests_id2_sys",tests_id2_sys)
        
        self.assertEqual(response.status_code,201,  "Sys_002 code 201")

    #====================

    def test_Sys_get(self):
        token = self.create_token()
        response = self.client.get(
            url_for('sys.find_all'),
            headers=token
        )
        result = len(response.json)>0
        self.assertTrue(result, "Sys_unit_002 code 201")


    #====================
    def test_Sys_get_by_id(self):
        
          token = self.create_token()
          response = self.client.get(url_for('sys.find_by_id',id=self.session.get("tests_id1_sys")), headers=token)
          
          self.assertEqual(response.status_code, 200 ,"Sys_get_by_id code 201")


    #====================
    def test_delete_sys_2(self):
    
        token = self.create_token()

        response = self.client.delete(url_for('sys.delete',id=self.session.get("tests_id2_sys")), headers=token)


        self.assertEqual(response.status_code, 204, "Sys_delete code 204")

#===========================================================
# Sys_Document_Category
#===========================================================


    def test_Sys_Document_Category_001_create(self):
    
        
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
                  "active": "S",
                  "id": str(uuidCreate),
                  "name":"TST1"
            }
     
        response = self.client.post(url_for('sysdocumentcategory.save'), json=req_post, headers=token)
        tests_id1_sys_document_category = str(json.loads(response.data.decode())['id'])
        self.session.set("tests_id1_sys_document_category",tests_id1_sys_document_category)
        self.assertEqual(response.status_code, 201, "Sys_Document_Category_001 201")

#====================

    def test_Sys_Document_Category_002_create(self):
       
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
                  "active": "S",
                  "id": str(uuidCreate),
                  "name":"TST2"
            }
        response = self.client.post(url_for('sysdocumentcategory.save'), json=req_post, headers=token)
    
        tests_id2_sys_document_category = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_document_category",tests_id2_sys_document_category)
        self.assertEqual(response.status_code, 201, "Sys_Document_Category_001 201")

#====================

    def test_Sys_Document_Category_get(self):
        token = self.create_token()
        response = self.client.get(
            url_for('sysdocumentcategory.find_all'),
            headers=token
        )
        result = len(response.json)>0
        self.assertTrue(result, "Sys_Document_Category_create 200")

#====================

    def test_Sys_Document_Category_get_by_id(self):
          
          token = self.create_token()
          response = self.client.get(url_for('sysdocumentcategory.find_by_id',id=self.session.get("tests_id1_sys_document_category")), headers=token)
        

          self.assertEqual(response.status_code, 200 , "Sys_Document_Category_get_by_id 200")

#====================

    def test_Sys_Document_Category_delete(self):

        token = self.create_token()

        response = self.client.delete(url_for('sysdocumentcategory.delete',id=self.session.get("tests_id2_sys_document_category")), headers=token)


        self.assertEqual(response.status_code, 204, "Sys_Document_Category_delete 204")

#===========================================================
# Sys_Group
#===========================================================
    
    def test_Sys_Group_001_create(self):
        
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
                "id": str(uuidCreate),
                "name": str(uuidCreate),
            }
    
        response = self.client.post(url_for('sysgroup.save'), json=req_post, headers=token)
        tests_id1_sys_group_2 = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_group_2",tests_id1_sys_group_2)
        self.assertEqual(response.status_code, 201, "Sys_Group_001_create 201")

#====================

    def test_Sys_Group_002_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
    
        req_post ={
                "id": str(uuidCreate),
                "name": str(uuidCreate),
            }
    
        response = self.client.post(url_for('sysgroup.save'), json=req_post, headers=token)
        tests_id2_sys_group_2 = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_group_2",tests_id2_sys_group_2)

        self.assertEqual(response.status_code, 201, "Sys_Group_002_create 201")

#====================

    def test_get_Sys_Group(self):

        token = self.create_token()
        response = self.client.get(
            url_for('sysgroup.find_all'),
            headers=token
        )
        result = len(response.json)>0

        self.assertTrue(result, "Sys_Group_get")

#====================

    def test_Sys_Group_get_by_id(self):
          
          token = self.create_token()
          response = self.client.get(url_for('sysunit.find_by_id',id=self.session.get("tests_id1_sys_group_2")), headers=token)
    
          self.assertEqual(response.status_code, 200,"Sys_Group_get_by_id 200")

#====================

    def test_Sys_Group_delete(self): 

      
        token = self.create_token()

        response = self.client.delete(url_for('sysgroup.delete',id=self.session.get("tests_id2_sys_group_2")), headers=token)


        self.assertEqual(response.status_code, 204,"Sys_Group_delete 204")


#===========================================================
# sys_document_group
#===========================================================

    def test_Sys_Document_Group_001_create(self):
        
         uuidCreate = uuid.uuid4()
         token = self.create_token()
         req_post ={
                 "id": str(uuidCreate),
                 "document_fk_id": "fab74c36-47a2-4b90-91de-6618b00791e4",
                 "sys_group_fk_id":"4218d8f1-8595-4052-aace-ba36f772623e"
             }
    
         response = self.client.post(url_for('sysdocumentgroup.save'), json=req_post, headers=token)
         tests_id1_sys_document_group = json.loads(response.data.decode())['id']
         self.session.set("tests_id1_sys_document_group",tests_id1_sys_document_group)
         self.assertEqual(response.status_code, 201," Sys_Document_Group_001_create 201")

#====================

    def test_Sys_Document_Group_002_create(self):
         
         uuidCreate = uuid.uuid4()
         token = self.create_token()
    
         req_post ={
                 "id": str(uuidCreate),
                 "document_fk_id": "fab74c36-47a2-4b90-91de-6618b00791e4",
                 "sys_group_fk_id":"4218d8f1-8595-4052-aace-ba36f772623e"
             }
    
         response = self.client.post(url_for('sysdocumentgroup.save'), json=req_post, headers=token)
         tests_id2_sysdocumentgroup = json.loads(response.data.decode())['id']
         self.session.set("tests_id2_sysdocumentgroup",tests_id2_sysdocumentgroup)
         

         self.assertEqual(response.status_code, 201,"test_Sys_Document_Group_002_create")

#====================

    def test_Sys_Document_Group_get(self):

         token = self.create_token()
         response = self.client.get(
             url_for('sysdocumentgroup.find_all'),
             headers=token
         )
         result = len(response.json)>0

         self.assertTrue(result, "test_Sys_Document_Group_get 200")

#====================

    def test_Sys_Document_Group_get_by_id(self):
          
           token = self.create_token()
           response = self.client.get(url_for('sysdocumentgroup.find_by_id',id=self.session.get("tests_id2_sys_group_2")), headers=token)
    
           self.assertEqual(response.status_code, 200, "Sys_Document_Group_get_by_id 200")

#====================

    def test_Sys_Document_Group_delete(self):
  
         token = self.create_token()

         response = self.client.delete(url_for('sysdocumentgroup.delete',id=self.session.get("tests_id2_sysdocumentgroup")), headers=token)


         self.assertEqual(response.status_code, 204,"Sys_Document_Group_delete 204")

#===========================================================
# Sys_Document
#===========================================================

 #====================

    def test_Sys_Document_001_create(self):
       
         uuidCreate = uuid.uuid4()
         token = self.create_token()
         req_post ={
            "title":"TST"+str(uuidCreate),
             "submission_date":"12/05/2022",

             "filename":"test4.txt",
             "content_type":"application/txt",

             "description":"S",
             "active":"S",
             "archive_date":"12/05/2022",
             
             "sys_user_id":"e59fa8cb-6791-4880-8ea4-112f5283f1bf",
             "sys_category_id":"b1d0f6d8-448e-465e-ace8-c6c4eb8137d8"
             }
    
         response = self.client.post(url_for('sysdocument.save'), json=req_post, headers=token)
         
         tests_id1_Sys_Document = str(json.loads(response.data.decode())['id'])
         self.session.set("tests_id1_Sys_Document",tests_id1_Sys_Document)
         print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>"+tests_id1_Sys_Document)
         self.assertEqual(response.status_code, 201,"Sys_Document_001_create 201")

#====================
    
    def test_Sys_Document_002_create(self):
        
         uuidCreate = uuid.uuid4()
         token = self.create_token()
    
         req_post ={
            "title":"TST"+str(uuidCreate),
             "submission_date":"12/05/2022",

             "filename":"teste.pdf",
             "content_type":"application/pdf",

             "description":"S",
             "active":"S",
             "archive_date":"12/05/2022",
             
             "sys_user_id":"e59fa8cb-6791-4880-8ea4-112f5283f1bf",
             "sys_category_id":"b1d0f6d8-448e-465e-ace8-c6c4eb8137d8"
         }
    
         response = self.client.post(url_for('sysdocument.save'), json=req_post, headers=token)
    
         tests_id2_Sys_Document = str( json.loads(response.data.decode())['id'])
         self.session.set("tests_id2_Sys_Document",tests_id2_Sys_Document)
         

         self.assertEqual(response.status_code, 201, "Sys_Document_002_create 201")

#====================

    def test_Sys_Document_get(self):
    
         token = self.create_token()
         response = self.client.get(
             url_for('sysdocument.find_all'),
             headers=token
         )
         result = len(response.json)>0
    
         self.assertTrue(result, "Sys_Document_get 200")

#====================

    def test_Sys_Document_get_by_id(self):
        
           token = self.create_token()
           response = self.client.get(url_for('sysdocument.find_by_id',id=self.session.get("tests_id1_Sys_Document")), headers=token)
           
           self.assertEqual(response.status_code, 200,"Sys_Document_get_by_id 200")

#====================

    def test_Sys_Document_delete(self):
    
         token = self.create_token()

         response = self.client.delete(url_for('sysdocument.delete',id=self.session.get("tests_id2_Sys_Document")), headers=token)


         self.assertEqual(response.status_code, 204,"Sys_Document_delete 204")

#===========================================================
# Sys_Document_upload extends sys_document
#===========================================================

#====================
    
    def test_Sys_Document_001_create_PDF(self):
       
         uuidCreate = uuid.uuid4()
         token = self.create_token()
         req_post ={
            "title":"TST",
             "submission_date":"12/05/2022",

             "filename":"test1.pdf",
             "content_type":"application/pdf",

             "description":"S",
             "active":"S",
             "archive_date":"12/05/2022",
             
             "sys_user_id":"e59fa8cb-6791-4880-8ea4-112f5283f1bf",
             "sys_category_id":"b1d0f6d8-448e-465e-ace8-c6c4eb8137d8"
             }
    
         response = self.client.post(url_for('sysdocument.save'), json=req_post, headers=token)
         
         tests_id1_Sys_Document_pdf = str(json.loads(response.data.decode())['id'])
         self.session.set("tests_id1_Sys_Document_pdf",tests_id1_Sys_Document_pdf)
         self.assertEqual(response.status_code, 201,"Sys_Document_001_create 201")

#====================
    
    def test_Sys_Document_002_create_zip(self):
        
         uuidCreate = uuid.uuid4()
         token = self.create_token()
    
         req_post ={
            "title":"TST",
             "submission_date":"12/05/2022",

             "filename":"test2.zip",
             "content_type":"application/zip",

             "description":"S",
             "active":"S",
             "archive_date":"12/05/2022",
             
             "sys_user_id":"e59fa8cb-6791-4880-8ea4-112f5283f1bf",
             "sys_category_id":"b1d0f6d8-448e-465e-ace8-c6c4eb8137d8"
         }
    
         response = self.client.post(url_for('sysdocument.save'), json=req_post, headers=token)
    
         tests_id2_Sys_Document_zip = str( json.loads(response.data.decode())['id'])
         self.session.set("tests_id2_Sys_Document_zip",tests_id2_Sys_Document_zip)
         

         self.assertEqual(response.status_code, 201, "Sys_Document_002_create_zip 201")
   
#====================

    def test_Sys_Document_003_create_xlsx(self):
       
         uuidCreate = uuid.uuid4()
         token = self.create_token()
         req_post ={
            "title":"TST",
             "submission_date":"12/05/2022",

             "filename":"test3.xlsx",
             "content_type":"application/xlsx",

             "description":"S",
             "active":"S",
             "archive_date":"12/05/2022",
             
             "sys_user_id":"e59fa8cb-6791-4880-8ea4-112f5283f1bf",
             "sys_category_id":"b1d0f6d8-448e-465e-ace8-c6c4eb8137d8"
             }
    
         response = self.client.post(url_for('sysdocument.save'), json=req_post, headers=token)
         
         tests_id1_Sys_Document_xlsx = str(json.loads(response.data.decode())['id'])
         self.session.set("tests_id1_Sys_Document_xlsx",tests_id1_Sys_Document_xlsx)
         self.assertEqual(response.status_code, 201,"Sys_Document_001_create 201")

#====================

    def test_Sys_Document_004_create_txt(self):
       
         uuidCreate = uuid.uuid4()
         token = self.create_token()
         req_post ={
            "title":"TST",
             "submission_date":"12/05/2022",

             "filename":"test4.txt",
             "content_type":"application/txt",

             "description":"S",
             "active":"S",
             "archive_date":"12/05/2022",
             
             "sys_user_id":"e59fa8cb-6791-4880-8ea4-112f5283f1bf",
             "sys_category_id":"b1d0f6d8-448e-465e-ace8-c6c4eb8137d8"
             }
    
         response = self.client.post(url_for('sysdocument.save'), json=req_post, headers=token)
         
         tests_id1_Sys_Document_txt = str(json.loads(response.data.decode())['id'])
         self.session.set("tests_id1_Sys_Document_txt" ,tests_id1_Sys_Document_txt)
         self.assertEqual(response.status_code, 201,"Sys_Document_001_create_txt 201")

#===========================================================

    def test_Sys_Document_005_upload_pdf(self):
        dir_test = os.path.dirname(__file__) 
        path_test = os.path.join(dir_test, 'uploads'+os.sep+'test1.pdf')
        id = self.session.get('tests_id1_Sys_Document_pdf').decode()
       
        with open(path_test, "rb") as file:
            tostring = base64.b64encode(file.read())
            file.close()

            
        token = self.create_token()
        req_post ={
                "file_content_type":"application/pdf",
                "filename":"test1.pdf",
                "file_64":tostring.decode()            
             }

        response = self.client.post(url_for('sysdocument.post_file',id=id ), json=req_post, headers=token)
         
        self.assertEqual(response.status_code, 201)
        
#====================       

    def test_Sys_Document_006_upload_zip(self):
        dir_test = os.path.dirname(__file__) 
        path_test = os.path.join(dir_test, 'uploads'+os.sep+'test2.zip')
        id = self.session.get('tests_id2_Sys_Document_zip').decode()
        
        with open(path_test, "rb") as file:
            tostring = base64.b64encode(file.read())
            file.close()

            
        token = self.create_token()
        req_post ={
                "file_content_type":"application/zip",
                "filename":"test2.zip",
                "file_64":tostring.decode()            
             }

        response = self.client.post(url_for('sysdocument.post_file',id=id ), json=req_post, headers=token)
         
        self.assertEqual(response.status_code, 201)

#==================== 
   
    def test_Sys_Document_007_upload_xlsx(self):

        dir_test = os.path.dirname(__file__) 
        path_test = os.path.join(dir_test, 'uploads'+os.sep+'test3.xlsx')
        id = self.session.get('tests_id1_Sys_Document_xlsx').decode()
       
        with open(path_test, "rb") as file:
            tostring = base64.b64encode(file.read())
            file.close()

            
        token = self.create_token()
        req_post ={
                "file_content_type":"application/xlsx",
                "filename":"test3.xlsx",
                "file_64":tostring.decode()            
             }

        response = self.client.post(url_for('sysdocument.post_file',id=id ), json=req_post, headers=token)
         
        self.assertEqual(response.status_code, 201)
    
#==================== 

    def test_Sys_Document_008_upload_txt(self):

        dir_test = os.path.dirname(__file__) 
        path_test = os.path.join(dir_test, 'uploads'+os.sep+'test4.txt')
        id = self.session.get('tests_id1_Sys_Document_txt').decode()
    
        with open(path_test, "rb") as file:
            tostring = base64.b64encode(file.read())
            
         
        token = self.create_token()
        req_post ={
                "file_content_type":"application/txt",
                "filename":"test4.txt",
                "file_64":tostring.decode()          
             }

        response = self.client.post(url_for('sysdocument.post_file',id=id ), json=req_post, headers=token)
        
        self.assertEqual(response.status_code, 201)

# #===========================================================

#==================== 

    def test1_Sys_Document_009_download_pdf(self):
        id = self.session.get('tests_id1_Sys_Document_pdf').decode()

        dir_test = os.path.dirname(__file__) 
        path_test = os.path.join(dir_test, 'downloads'+os.sep+id+'-download.pdf')

        token = self.create_token()
        response = self.client.get(url_for('sysdocument.get_file',id=id ), headers=token)
        
        with open(path_test, 'wb+') as file:
                file.write(response.data)
                file.close()
        self.assertEqual(response.status_code, 200,"test_Sys_Document_001_download code 200")

        exist = os.path.exists(path_test)
        
        self.assertEqual(exist, True,"test_Sys_Document_001_download exist")

# #==================== 

    def test_Sys_Document_010_download_zip(self):
        id = self.session.get('tests_id2_Sys_Document_zip').decode()

        dir_test = os.path.dirname(__file__) 
        path_test = os.path.join(dir_test, 'downloads'+os.sep+id+'-download.zip')
        
        token = self.create_token()
        response = self.client.get(url_for('sysdocument.get_file',id=id ), headers=token)
       

        with open(path_test, 'wb') as file:
                file.write(response.data)
                file.close()
        self.assertEqual(response.status_code, 200,"test_Sys_Document_0010_download_zip code 200")

        exist = os.path.exists(path_test)
        self.assertEqual(exist, True,"test_Sys_Document_011_download_zip exist")

# #==================== 

    def test_Sys_Document_011_download_xlsx(self):
        id = self.session.get('tests_id1_Sys_Document_xlsx').decode()

        dir_test = os.path.dirname(__file__) 
        path_test = os.path.join(dir_test, 'downloads'+os.sep+id+'-download.xlsx')

        token = self.create_token()
        response = self.client.get(url_for('sysdocument.get_file',id=id ), headers=token)

        with open(path_test, 'wb') as file:
                file.write(response.data)
                file.close()
        self.assertEqual(response.status_code, 200,"test_Sys_Document_0010_download_xlsx code 200")

        exist = os.path.exists(path_test)
        self.assertEqual(exist, True,"test_Sys_Document_011_download_xlsx exist")

# #==================== 

    def test_Sys_Document_012_download_txt(self):
        id = self.session.get('tests_id1_Sys_Document_txt').decode()

        dir_test = os.path.dirname(__file__) 
        path_test = os.path.join(dir_test, 'downloads'+os.sep+id+'-download.txt')

        token = self.create_token()
        response = self.client.get(url_for('sysdocument.get_file',id=id ), headers=token)

        with open(path_test, 'wb') as file:
                file.write(response.data)
                file.close()
        self.assertEqual(response.status_code, 200,"test_Sys_Document_0010_download_txt code 200")

        exist = os.path.exists(path_test)
       
        self.assertEqual(exist, True,"test_Sys_Document_011_download_txt exist")
        
#==================== 
#===========================================================
# Sys_Group_Program
#===========================================================
    
    def test_Sys_Group_Program_001_create(self):
         
         uuidCreate = uuid.uuid4()
         token = self.create_token()
         req_post ={
                 "id": str(uuidCreate),
                   "sys_program_id":"1a7f1e36-e72c-4b96-abc0-9f3c56c777fe",
                    "sys_group_id":"9c69a855-b884-4d0b-963e-98253149b650"
            
             }
    
         response = self.client.post(url_for('sysgroupprogram.save'), json=req_post, headers=token)
         tests_id1_sysgroupprogram = json.loads(response.data.decode())['id']
         self.session.set("tests_id1_sysgroupprogram",tests_id1_sysgroupprogram)
         self.assertEqual(response.status_code, 201,"Sys_Group_Program_001_create 201")

#====================

    def test_Sys_Group_Program_002_create(self):
        
         uuidCreate = uuid.uuid4()
         token = self.create_token()
    
         req_post ={
                 "id": str(uuidCreate) ,
                 "sys_program_id":"1a7f1e36-e72c-4b96-abc0-9f3c56c777fe",
                 "sys_group_id":"9c69a855-b884-4d0b-963e-98253149b650"
             }
    
         response = self.client.post(url_for('sysgroupprogram.save'), json=req_post, headers=token)
         tests_id2_sysgroupprogram = json.loads(response.data.decode())['id']
         self.session.set("tests_id2_sysgroupprogram",tests_id2_sysgroupprogram)

         self.assertEqual(response.status_code, 201,"Sys_Group_Program_002_create 201")

#====================

    def test_Sys_Group_Program_get(self):
    
         token = self.create_token()
         response = self.client.get(
             url_for('sysgroupprogram.find_all'),
             headers=token
         )
         result = len(response.json)>0

         self.assertTrue(result, "Sys_Group_Program_get")

#====================

    def test_Sys_Group_Program_get_by_id(self):
           
           token = self.create_token()
           response = self.client.get(url_for('sysgroupprogram.find_by_id',id=self.session.get("tests_id1_sysgroupprogram")), headers=token)
    
           self.assertEqual(response.status_code, 200,"Sys_Group_Program_get_by_id 200")

#====================

    def test_Sys_Group_Program_delete(self):
         
         token = self.create_token()

         response = self.client.delete(url_for('sysgroupprogram.delete',id=self.session.get("tests_id2_sysgroupprogram")), headers=token)
         

         self.assertEqual(response.status_code, 204,"Sys_Group_Program_delete 204")

#===========================================================
# Sys_User_Group
#===========================================================
   
    def test_Sys_User_Group_001_create(self):
     
     uuidCreate = uuid.uuid4()
     token = self.create_token()
     req_post ={
             "id": str(uuidCreate),
             "sys_group_id": "5b0a97bf-38e8-443d-94be-181a01dc4929",
             "sys_user_id": "a4a5af12-46b3-42dd-9126-bc45d5306f2b"
         }
    
     response = self.client.post(url_for('sysusergroup.save'), json=req_post, headers=token)
     tests_id1_SysUserGroup = str(json.loads(response.data.decode())['id'])
     self.session.set("tests_id1_SysUserGroup",tests_id1_SysUserGroup)

     self.assertEqual(response.status_code, 201,"Sys_User_Group_001_create 201")

#====================

    def test_Sys_User_Group_002_create(self):
   
     uuidCreate = uuid.uuid4()
     token = self.create_token()
    
     req_post ={
             "id": str(uuidCreate) ,
             "sys_group_id": "5b0a97bf-38e8-443d-94be-181a01dc4929",
             "sys_user_id": "a4a5af12-46b3-42dd-9126-bc45d5306f2b"
     }
     response = self.client.post(url_for('sysusergroup.save'), json=req_post, headers=token)
     tests_id2_SysUserGroup = str(json.loads(response.data.decode())['id'])
     self.session.set("tests_id2_SysUserGroup",tests_id2_SysUserGroup)
    

     self.assertEqual(response.status_code, 201,"Sys_User_Group_002_create 201")

#====================

    def test_Sys_User_Group_get(self):
    
     token = self.create_token()
     response = self.client.get(
         url_for('sysusergroup.find_all'),
         headers=token
     )
     result = len(response.json)>0
    
     self.assertTrue(result)

#====================

    def test_Sys_User_Group_get_by_id(self):
       
       token = self.create_token()
       response = self.client.get(url_for('sysusergroup.find_by_id',id= self.session.get("tests_id1_SysUserGroup")), headers=token)
    
       self.assertEqual(response.status_code, 200,"Sys_User_Group_get_by_id 200")

#====================

    def test_Sys_User_Group_delete(self):
    
     token = self.create_token()

     response = self.client.delete(url_for('sysusergroup.delete',id=self.session.get("tests_id2_SysUserGroup")), headers=token)


     self.assertEqual(response.status_code, 204,"Sys_User_Group_delete 204")

#===========================================================
# Sys_Restriction
#===========================================================

    def test_Sys_Restrection_001_create(self):
        
         uuidCreate = uuid.uuid4()
         token = self.create_token()
         req_post ={
                 "id": str(uuidCreate),
                 "name":"TST"
             }
    
         response = self.client.post(url_for('sysrestriction.save'), json=req_post, headers=token)
         tests_id1_sysrestriction = str(json.loads(response.data.decode())['id'])
         self.session.set("tests_id1_sysrestriction",tests_id1_sysrestriction)

         self.assertEqual(response.status_code, 201,"test_Sys_Restrection_001_create 201")

#====================

    def test_Sys_Restrection_002_create(self):
   
         uuidCreate = uuid.uuid4()
         token = self.create_token()
    
         req_post ={
                 "id": str(uuidCreate) ,
                 "name":"TST"
         }
         response = self.client.post(url_for('sysrestriction.save'), json=req_post, headers=token)
         tests_id2_sysrestriction = str(json.loads(response.data.decode())['id'])
         self.session.set("tests_id2_sysrestriction",tests_id2_sysrestriction)

         self.assertEqual(response.status_code, 201, "test_Sys_Restrection_002_create 201")

#====================

    def test_Sys_Restriction_get(self):
    
         token = self.create_token()
         response = self.client.get(
             url_for('sysrestriction.find_all'),
             headers=token
         )
         result = len(response.json)>0
    
         self.assertTrue(result, "Sys_Restriction_get")

#====================

    def test_Sys_Restriction_get_by_id(self):
        
           token = self.create_token()
           response = self.client.get(url_for('sysrestriction.find_by_id',id=  self.session.get("tests_id1_sysrestriction")), headers=token)
    
           self.assertEqual(response.status_code, 200,"Sys_Restriction_get_by_id 200")

#====================

    def test_Sys_Restriction_delete(self):
    
         token = self.create_token()

         response = self.client.delete(url_for('sysrestriction.delete',id=self.session.get("tests_id2_sysrestriction")), headers=token)


         self.assertEqual(response.status_code, 204,"Sys_Restriction_delete 204")

#===========================================================
# Sys_Module
#===========================================================  

    def test_Sys_Module_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
                "id": str(uuidCreate),     
                "name":"Testess"+str(uuidCreate),
                "color": "tst",
                "icon": "tst",
                "sigla_module": "C",
                "sys_id": "cda6e838-fa47-4154-af8d-0f84be5f0a7a"

            }
        
        response = self.client.post(url_for('sysmodule.save'), json=req_post, headers=token)
        tests_id1_sys_module = str(json.loads(response.data.decode())['id'])
        self.session.set("tests_id1_sys_module",tests_id1_sys_module)
        self.assertEqual(response.status_code, 201, "Sys_Module_001_create 201")

#====================

    def test_Sys_Module_002_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        
        req_post ={
                "id": str(uuidCreate),     
                "name":"Testess"+str(uuidCreate),
                "color": "tst",
                "icon": "tst",
                "sigla_module": "C",
                "sys_id": "cda6e838-fa47-4154-af8d-0f84be5f0a7a"

            }
        response = self.client.post(url_for('sysmodule.save'), json=req_post, headers=token)
        tests_id2_sys_module = str(json.loads(response.data.decode())['id'])
        self.session.set("tests_id2_sys_module",tests_id2_sys_module)

        self.assertEqual(response.status_code, 201,"Sys_Module_002_create 201")

#====================

    def test_Sys_Module_get(self):
        
        token = self.create_token()
        response = self.client.get(
            url_for('sysmodule.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "Sys_Module_get 200")

#====================

    def test_Sys_Module_001_get_by_id(self):
    
      token = self.create_token()
      response = self.client.get(url_for('sysmodule.find_by_id',id= self.session.get("tests_id1_sys_module")), headers=token)
    
      self.assertEqual(response.status_code, 200,"Sys_Module_001_get_by_id 200")

#====================

    def test_Sys_Module_delete(self):
    
        token = self.create_token()

        response = self.client.delete(url_for('sysmodule.delete',id=self.session.get("tests_id2_sys_module")), headers=token)


        self.assertEqual(response.status_code, 204,"Sys_Module_delete 204")

#===========================================================
# Sys_Licence
#===========================================================  


    def test_Sys_Licence_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "doc":"tst",
            "end_uf": "tst",
            "end_bairro": "tst",
            "end_cidade": "tst",
            "end_logradouro": "tst",
            "end_numero": "tst",
            "end_pais": "sts",


            "log_date_ins": "12/05/2022",
            "nome_solicitante": "tst",
            "status": "AT",
            "status_data": "12/05/2022",
            "status_observacao": "tst",
            "sys_version": "tst",
            "tipo_doc": "tst",
            "chamado_id":"t",

            "sys_id": "16afb315-e210-42e4-9b15-ece23f5808c6",
            "sys_plan_id": "09cfa735-9357-495e-bfac-4d35cbb8c172",
            "sys_user_id":"d5ddf2dc-4b17-4c78-a8df-9f9e615b99a0"
                
            }
        
        response = self.client.post(url_for('syslicence.save'), json=req_post, headers=token)
        
        tests_id1_syslicence = str(json.loads(response.data.decode())['id'])
        self.session.set("tests_id1_syslicence",tests_id1_syslicence)
        self.assertEqual(response.status_code, 201, "Sys_Licence_001_create 201")

#====================

    def test_Sys_Licence_002_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        
        req_post ={
            "id": str(uuidCreate),   
            "doc":"tst",
            "end_uf": "tst",
            "end_bairro": "tst",
            "end_cidade": "tst",
            "end_logradouro": "tst",
            "end_numero": "tst",
            "end_pais": "sts",


            "log_date_ins": "12/05/2022",
            "nome_solicitante": "tst",
            "status": "AT",
            "status_data": "12/05/2022",
            "status_observacao": "tst",
            "sys_version": "tst",
            "tipo_doc": "tst",
            "chamado_id":"t",

            "sys_id": "16afb315-e210-42e4-9b15-ece23f5808c6",
            "sys_plan_id": "09cfa735-9357-495e-bfac-4d35cbb8c172",
            "sys_user_id":"d5ddf2dc-4b17-4c78-a8df-9f9e615b99a0"
                
            }
        response = self.client.post(url_for('syslicence.save'), json=req_post, headers=token)
        tests_id2_syslicence = str(json.loads(response.data.decode())['id'])
        self.session.set("tests_id2_syslicence",tests_id2_syslicence)

        self.assertEqual(response.status_code, 201,"Sys_Licence_001_create 201")

#====================

    def test_Sys_Licence_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('syslicence.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result,"Sys_Licence_get 200" )

#====================

    def test_Sys_Licenceget_by_id(self):
    
        token = self.create_token()
        response = self.client.get(url_for('syslicence.find_by_id',id= self.session.get("tests_id1_syslicence")), headers=token)
        
        self.assertEqual(response.status_code, 200,"Sys_Licenceget_by_id 200" )

#====================

    def test_Sys_Licence_delete(self):

        token = self.create_token()

        response = self.client.delete(url_for('syslicence.delete',id=self.session.get("tests_id2_syslicence")), headers=token)


        self.assertEqual(response.status_code, 204, "Sys_Licence_delete 204")

#===========================================================
# Sys_Pla
#===========================================================
    
    def test_Sys_Plan_001_create(self):
   
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "description": "Plano Free",
            "name": "FreXXe",
            "sys_id": "e8329d00-443f-4c03-8e73-c161f0d4f37d",
            "type_plan": "FR"
            }
        
        response = self.client.post(url_for('sysplan.save'), json=req_post, headers=token)
        tests_id1_sysplan = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sysplan",tests_id1_sysplan)
        self.assertEqual(response.status_code, 201, "Sys_Plan_001_create 201")

#====================

    def test_Sys_Plan_002_create(self):
   
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        
        req_post ={
            "id": str(uuidCreate),   
            "description": "Plano Free",
            "name": "FreXXe",
            "sys_id": "e8329d00-443f-4c03-8e73-c161f0d4f37d",
            "type_plan": "FR"
            }
        response = self.client.post(url_for('sysplan.save'), json=req_post, headers=token)
        tests_id2_sysplan = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sysplan",tests_id2_sysplan)

        self.assertEqual(response.status_code, 201, "Sys_Plan_002_create 201")

#====================

    def test_Sys_Plan_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('sysplan.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "Sys_Plan_get 200")

#====================

    def test_Sys_Plan_get_by_id(self):
        
        token = self.create_token()
        response = self.client.get(url_for('sysplan.find_by_id',id= self.session.get("tests_id1_sysplan")), headers=token)
        
        self.assertEqual(response.status_code, 200, "Sys_Plan_get_by_id 200")

#====================

    def test_Sys_Plan_delete(self):
       
        token = self.create_token()

        response = self.client.delete(url_for('sysplan.delete',id=self.session.get("tests_id2_sysplan")), headers=token)


        self.assertEqual(response.status_code, 204, "Sys_Plan_delete 204")

#===========================================================
# Sys_Plan_Restriction
#===========================================================
    
    def test_Sys_Plan_Restriction_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sys_plan_id": "d5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103",
            "sys_restriction_id": "c7924fb8-b0f5-49ae-9d17-311cf96f545e",
            "value_restriction": "1"
            }
        
        response = self.client.post(url_for('sysplanrestriction.save'), json=req_post, headers=token)
        tests_id1_sysplanrestriction = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sysplanrestriction",tests_id1_sysplanrestriction)
        self.assertEqual(response.status_code, 201, "Sys_Plan_Restriction_001_create 201")

#====================

    def test_Sys_Plan_Restriction_002_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        
        req_post ={
            "id": str(uuidCreate),   
            "sys_plan_id": "d5dbbee6-c2ed-4d3c-b1d2-b6c9ab561103",
            "sys_restriction_id": "c7924fb8-b0f5-49ae-9d17-311cf96f545e",
            "value_restriction": "1"
            }
        response = self.client.post(url_for('sysplanrestriction.save'), json=req_post, headers=token)
        tests_id2_sysplanrestriction = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sysplanrestriction",tests_id2_sysplanrestriction)

        

        self.assertEqual(response.status_code, 201, "Sys_Plan_Restriction_002_create 201")

#====================

    def test_Sys_Plan_Restriction_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('sysplanrestriction.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result,"Sys_Plan_Restriction_get 200")

#====================

    def test_Sys_Plan_Restriction_get_by_id(self):
      
      token = self.create_token()
      response = self.client.get(url_for('sysplanrestriction.find_by_id',id=self.session.get("tests_id1_sysplanrestriction")), headers=token)
    
      self.assertEqual(response.status_code, 200,"test_Sys_Plan_Restriction_get_by_id 200")

#====================

    def test_Sys_Plan_Restriction_delete(self):
        
        token = self.create_token()

        response = self.client.delete(url_for('sysplanrestriction.delete',id=self.session.get("tests_id1_sysplanrestriction")), headers=token)


        self.assertEqual(response.status_code, 204,"Sys_Plan_Restriction_delete 204")

#===========================================================
# Sys_Restriction_Licence
#===========================================================

    def test_Sys_Restriction_Licence_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sys_licence_id": "7aae3305-c2bb-43f1-a4e8-878f27288673",
            "sys_restriction_id": "31da7d22-1925-4f32-85cc-d578834aad3a",
            "value_restriction":"1"

            }
        
        response = self.client.post(url_for('sysrestrictionlicence.save'), json=req_post, headers=token)
        tests_id1_sysrestrictionlicence = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sysrestrictionlicence",tests_id1_sysrestrictionlicence)

        self.assertEqual(response.status_code, 201,"Sys_Restriction_Licence_001_create 201")

#====================

    def test_Sys_Restriction_Licence_002_create(self):
        
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        
        req_post ={
            "id": str(uuidCreate),   
            "sys_licence_id": "7aae3305-c2bb-43f1-a4e8-878f27288673",
            "sys_restriction_id": "31da7d22-1925-4f32-85cc-d578834aad3a",
            "value_restriction":"1"

            }
        response = self.client.post(url_for('sysrestrictionlicence.save'), json=req_post, headers=token)
        tests_id2_sysrestrictionlicence = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sysrestrictionlicence",tests_id2_sysrestrictionlicence)

        self.assertEqual(response.status_code, 201,"Sys_Restriction_Licence_002_create 201")

#====================

    def test_Sys_Restriction_Licence_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('sysrestrictionlicence.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "Sys_Restriction_Licence_get 200")

#====================

    def test_Sys_Restriction_Licence_get_by_id(self):
      
      token = self.create_token()
      response = self.client.get(url_for('sysrestrictionlicence.find_by_id',id=self.session.get("tests_id1_sysrestrictionlicence")), headers=token)
    
      self.assertEqual(response.status_code, 200,"Sys_Restriction_Licence_get_by_id 200")

#====================

    def test_Sys_Restriction_Licence_delete(self):
       
        token = self.create_token()

        response = self.client.delete(url_for('sysrestrictionlicence.delete',id=self.session.get("tests_id2_sysrestrictionlicence")), headers=token)


        self.assertEqual(response.status_code, 204, "Sys_Restriction_Licence_delete 204")

#===========================================================
# Sys_Program
#===========================================================

    def test_Sys_Program_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "admin": "N",
            "controller": str(uuidCreate),
            "icon": "fas fa-table",
            "menu": "S",
            "name": "Parmetros",
            "type_program": "T",
            "sys_module_id": "43994411-c2eb-442e-818b-f36af2c7ed4e"

            }
        
        response = self.client.post(url_for('sysprogram.save'), json=req_post, headers=token)
        tests_id1_sysprogram = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sysprogram",tests_id1_sysprogram)
        self.assertEqual(response.status_code, 201, "Sys_Program_001_create 201")

#====================

    def test_Sys_Program_002_create(self):
 
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        
        req_post ={
            "id": str(uuidCreate),   
            "admin": "N",
            "controller": str(uuidCreate),
            "icon": "fas fa-table",
            "menu": "S",
            "name": "Parmetros",
            "type_program": "T",
            "sys_module_id": "43994411-c2eb-442e-818b-f36af2c7ed4e"

            }
        response = self.client.post(url_for('sysprogram.save'), json=req_post, headers=token)
        tests_id2_sysprogram = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sysprogram",tests_id2_sysprogram)
        

        self.assertEqual(response.status_code, 201, "test_Sys_Program_002_create")

#====================

    def test_Sys_Program_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('sysprogram.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "Sys_Program_get 200")

#====================

    def test_Sys_Program_get_by_id(self):
      
        token = self.create_token()
        response = self.client.get(url_for('sysprogram.find_by_id',id=self.session.get("tests_id1_sysprogram")), headers=token)
        
        self.assertEqual(response.status_code, 200, "Sys_Program_get_by_id 200")

#====================

    def test_Sys_Program_delete(self):
    
        token = self.create_token()

        response = self.client.delete(url_for('sysprogram.delete',id=self.session.get("tests_id2_sysprogram")), headers=token)


        self.assertEqual(response.status_code, 204, "Sys_Program_delete 204")


#===========================================================
# sys_group_program_feature
#===========================================================

    def test_sys_group_program_feature_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sys_program_id": "301b1210-4119-4e7f-8b64-74b8cc442144", 
            "sys_group_id": "f739def9-1304-40e1-b5e6-97ad9aa118b7", 
            "identity_feature": "S"

            }
        
        response = self.client.post(url_for('sysgroupprogramfeature.save'), json=req_post, headers=token)
        tests_id1_sys_group_program_feature = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_group_program_feature",tests_id1_sys_group_program_feature)
        self.assertEqual(response.status_code, 201, "sys_group_program_feature_001_create 201" )

#====================

    def test_sys_group_program_feature_002_create(self):
 
            uuidCreate = uuid.uuid4()
            token = self.create_token()
            req_post ={
                "id": str(uuidCreate),
                "sys_program_id": "301b1210-4119-4e7f-8b64-74b8cc442144", 
                "sys_group_id": "f739def9-1304-40e1-b5e6-97ad9aa118b7", 
                "identity_feature": "S"

                }
            
            response = self.client.post(url_for('sysgroupprogramfeature.save'), json=req_post, headers=token)
            tests_id2_sys_group_program_feature = json.loads(response.data.decode())['id']

            self.session.set("tests_id2_sys_group_program_feature",tests_id2_sys_group_program_feature)
            self.assertEqual(response.status_code, 201, "sys_group_program_feature_002_create 201")

#====================

    def test_sys_group_program_feature__get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('sysgroupprogramfeature.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "sys_group_program_feature_get 200")

#====================

    def test_sys_group_program_feature_get_by_id(self):
      
        token = self.create_token()
        response = self.client.get(url_for('sysgroupprogramfeature.find_by_id',id=self.session.get("tests_id1_sys_group_program_feature")), headers=token)
        
        self.assertEqual(response.status_code, 200, "sys_group_program_feature_get_by_id 200")

#====================

    def test_sys_group_program_feature_003_delete(self):
    
        token = self.create_token()

        response = self.client.delete(url_for('sysgroupprogramfeature.delete',id=self.session.get("tests_id2_sys_group_program_feature")), headers=token)

        self.assertEqual(response.status_code, 204 ,"sys_group_program_feature_delete 204")

#===========================================================
#  sys_licence_device   
#===========================================================

    def test_sys_licence_device_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sigla_device": "S",
            "sys_licence_id":"8f59f80f-91d5-4f5c-9c97-90d09ee2c7f4"

            }
        
        response = self.client.post(url_for('syslicencedevice.save'), json=req_post, headers=token)
        tests_id1_sys_licence_device = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_licence_device",tests_id1_sys_licence_device)
        self.assertEqual(response.status_code, 201, "sys_licence_device_001_create 2001")

#====================

    def test_sys_licence_device_002_create(self):
 
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sigla_device": "S",
            "sys_licence_id":"8f59f80f-91d5-4f5c-9c97-90d09ee2c7f4"

            }
        
        response = self.client.post(url_for('syslicencedevice.save'), json=req_post, headers=token)
        tests_id2_sys_licence_device = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_licence_device",tests_id2_sys_licence_device)
        self.assertEqual(response.status_code, 201, " sys_licence_device_002_create 201 ")

#====================

    def test_sys_licence_device_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('syslicencedevice.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "sys_licence_device_get 200")

#====================

    def test_sys_licence_device_get_by_id(self):
      
        token = self.create_token()
        response = self.client.get(url_for('syslicencedevice.find_by_id',id=self.session.get("tests_id1_sys_licence_device")), headers=token)
        
        self.assertEqual(response.status_code, 200, "sys_licence_device_get_by_id 200")

#====================

    def test_sys_licence_device_delete(self):
    
        token = self.create_token()

        response = self.client.delete(url_for('syslicencedevice.delete',id=self.session.get("tests_id2_sys_licence_device")), headers=token)


        self.assertEqual(response.status_code, 204, "sys_licence_device_delete 204")

#===========================================================
#  sys_program_favorite   
#===========================================================

    def test_sys_program_favorite_001_crete(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sys_program_id": "dd27cc32-fedb-4572-b09d-896663bdab7a",
            "sys_user_id":"a4a5af12-46b3-42dd-9126-bc45d5306f2b"

            }
        
        response = self.client.post(url_for('sysprogramfavorite.save'), json=req_post, headers=token)
        tests_id1_sys_program_favorite = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_program_favorite",tests_id1_sys_program_favorite)
        self.assertEqual(response.status_code, 201, "sys_program_favorite_001_crete  201")

#====================

    def test_sys_program_favorite_002_crete(self):
 
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sys_program_id": "dd27cc32-fedb-4572-b09d-896663bdab7a",
            "sys_user_id":"a4a5af12-46b3-42dd-9126-bc45d5306f2b"

            }
        
        response = self.client.post(url_for('sysprogramfavorite.save'), json=req_post, headers=token)
        tests_id2_sys_program_favorite = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_program_favorite",tests_id2_sys_program_favorite)
        self.assertEqual(response.status_code, 201, "sys_program_favorite_002_crete 201")

#====================

    def test_sys_program_favorite_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('sysprogramfavorite.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "sys_program_favorite_get 200")

#====================

    def test_sys_program_favorite_get_by_id(self):
      
        token = self.create_token()
        response = self.client.get(url_for('sysprogramfavorite.find_by_id',id=self.session.get("tests_id1_sys_program_favorite")), headers=token)
        
        self.assertEqual(response.status_code, 200, "sys_program_favorite_get_by_id 200")

#====================

    def test_sys_program_favorite_delete(self):
    
        token = self.create_token()

        response = self.client.delete(url_for('sysprogramfavorite.delete',id=self.session.get("tests_id2_sys_program_favorite")), headers=token)


        self.assertEqual(response.status_code, 204, "test_sys_program_favorite_delete 204")

#===========================================================
#  sys_licence_device
#===========================================================

    def test_sys_licence_device_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sigla_device": "S",
            "sys_licence_id":"8f59f80f-91d5-4f5c-9c97-90d09ee2c7f4"

            }
        
        response = self.client.post(url_for('syslicencedevice.save'), json=req_post, headers=token)
        tests_id1_sys_licence_device = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_licence_device",tests_id1_sys_licence_device)
        self.assertEqual(response.status_code, 201, "sys_licence_001_create 201")

#====================

    def test_sys_licence_device_002_create(self):
 
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sigla_device": "S",
            "sys_licence_id":"8f59f80f-91d5-4f5c-9c97-90d09ee2c7f4"

            }
        
        response = self.client.post(url_for('syslicencedevice.save'), json=req_post, headers=token)
        tests_id2_sys_licence_device = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_licence_device",tests_id2_sys_licence_device)
        self.assertEqual(response.status_code, 201, "sys_licence_device_002_create 201")

#====================

    def test_sys_licence_device_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('syslicencedevice.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result," sys_licence_device_get 200")

#====================

    def test_sys_licence_device_get_by_id_sys(self):
      
        token = self.create_token()
        response = self.client.get(url_for('syslicencedevice.find_by_id',id=self.session.get("tests_id1_sys_licence_device")), headers=token)
        
        self.assertEqual(response.status_code, 200, "sys_licence_device_get_by_id_sys 200")

#====================

    def test_sys_licence_device_delete(self):
    
        token = self.create_token()

        response = self.client.delete(url_for('syslicencedevice.delete',id=self.session.get("tests_id2_sys_licence_device")), headers=token)


        self.assertEqual(response.status_code, 204, "sys_licence_device_delete 204")

#===========================================================
#  sys_program_feature      
#===========================================================

    def test_sys_program_feature_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sys_program_id": "503589b1-addd-4e0e-a335-3efc94715a22",
            "descricao":"tst",
            "identity": "tst"

            }
        
        response = self.client.post(url_for('sysprogramfeature.save'), json=req_post, headers=token)
        tests_id1_sys_program_feature = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_program_feature",tests_id1_sys_program_feature)
        self.assertEqual(response.status_code, 201, "sys_program_feature_001_create 201")

#====================

    def test_sys_program_feature_002_create(self):
 
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sys_program_id": "503589b1-addd-4e0e-a335-3efc94715a22",
            "descricao":"tst",
            "identity": "tst"

            }
        
        response = self.client.post(url_for('sysprogramfeature.save'), json=req_post, headers=token)
        tests_id2_sys_program_feature = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_program_feature",tests_id2_sys_program_feature)
        self.assertEqual(response.status_code, 201, "test_sys_program_feature_002_create 201")

#====================

    def test_sys_program_feature_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('sysprogramfeature.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "sys_program_feature_get 200")

#====================

    def test_sys_program_feature_get_by_id(self):
      
        token = self.create_token()
        response = self.client.get(url_for('sysprogramfeature.find_by_id',id=self.session.get("tests_id1_sys_program_feature")), headers=token)
        
        self.assertEqual(response.status_code, 200,"sys_program_feature_get_by_id 200")

#====================

    def test_sys_program_feature_delete(self):
    
        token = self.create_token()

        response = self.client.delete(url_for('sysprogramfeature.delete',id=self.session.get("tests_id2_sys_program_feature")), headers=token)


        self.assertEqual(response.status_code, 204, "test_sys_program_feature_delete 204")

#===========================================================
#  sys_user_program_feature         
#===========================================================
    def test_sys_user_program_feature_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sys_program_id": "2e940472-d3df-45cd-85e2-4c6d128c20df",
            "sys_user_id":"e25d0823-5e14-4968-93fe-a3b38915f350",
            "identity_feature": "TST"

            }
        
        response = self.client.post(url_for('sysuserprogramfeature.save'), json=req_post, headers=token)
        tests_id1_sys_user_program_feature = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_user_program_feature",tests_id1_sys_user_program_feature)
        self.assertEqual(response.status_code, 201, "sys_user_program_feature_001_create 201" )

#====================

    def test_sys_user_program_feature_002_create(self):
 
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "sys_program_id": "2e940472-d3df-45cd-85e2-4c6d128c20df",
            "sys_user_id":"e25d0823-5e14-4968-93fe-a3b38915f350",
            "identity_feature": "TST"

            }
        
        response = self.client.post(url_for('sysuserprogramfeature.save'), json=req_post, headers=token)
        tests_id2_sys_user_program_feature = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_user_program_feature",tests_id2_sys_user_program_feature)
        self.assertEqual(response.status_code, 201, "sys_user_program_feature_002 201")

#====================

    def test_sys_user_program_feature_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('sysuserprogramfeature.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "sys_user_program_feature_get 200")

#====================

    def test_sys_user_program_feature_get_by_id(self):
      
        token = self.create_token()
        response = self.client.get(url_for('sysuserprogramfeature.find_by_id',id=self.session.get("tests_id1_sys_user_program_feature")), headers=token)
        
        self.assertEqual(response.status_code, 200, "sys_user_program_feature_get_by_id 200")

#====================

    def test_sys_user_program_feature_delete(self):
    
        token = self.create_token()

        response = self.client.delete(url_for('sysuserprogramfeature.delete',id=self.session.get("tests_id2_sys_user_program_feature")), headers=token)


        self.assertEqual(response.status_code, 204,"sys_user_program_feature_delete 204")
    
#===========================================================
#  sys_change_log          
#===========================================================
    def test_sys_change_log_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "access_ip":"tst",
            "class_name":"tst",
            "columnname":"tst",

            "log_day":"ts",
            "log_month": "ts",
            "log_trace":"ts",
            "log_year":"ts",
            "logdate":"150420",
            "login":"tst",
            

            "newvalue":"tst",
            "oldvalue":"tst",
            "operation": "tst",
            "php_sapi":"tst",
            "pkvalue": "tst",
            "primarykey":"tst",
            "session_id":"tst",

            "tablename":"tst",
            "transaction_id":"tst"

            }
        
        response = self.client.post(url_for('syschangelog.save'), json=req_post, headers=token)
        tests_id1_sys_change_log = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_change_log",tests_id1_sys_change_log)
        self.assertEqual(response.status_code, 201, "sys_change_log_001_create 201")

#====================

    def test_sys_change_log_002_create(self):
 
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "access_ip":"tst",
            "class_name":"tst",
            "columnname":"tst",

            "log_day":"ts",
            "log_month": "ts",
            "log_trace":"ts",
            "log_year":"ts",
            "logdate":"150420",
            "login":"tst",
            

            "newvalue":"tst",
            "oldvalue":"tst",
            "operation": "tst",
            "php_sapi":"tst",
            "pkvalue": "tst",
            "primarykey":"tst",
            "session_id":"tst",

            "tablename":"tst",
            "transaction_id":"tst"

            }
        
        response = self.client.post(url_for('syschangelog.save'), json=req_post, headers=token)
        tests_id2_sys_change_log = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_change_log",tests_id2_sys_change_log)
        self.assertEqual(response.status_code, 201, "sys_change_log_002_create 201")

#====================

    def test_sys_change_log_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('syschangelog.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result , "sys_change_log_get 200")

#====================

    def test_sys_change_log_get_by_id(self):
      
        token = self.create_token()
        response = self.client.get(url_for('syschangelog.find_by_id',id=self.session.get("tests_id1_sys_change_log")), headers=token)
        
        self.assertEqual(response.status_code, 200, "sys_change_log_get_by_id 200")

#====================

    def test_sys_change_log_delete(self):

    
        token = self.create_token()

        response = self.client.delete(url_for('syschangelog.delete',id=self.session.get("tests_id2_sys_change_log")), headers=token)


        self.assertEqual(response.status_code, 204, "sys_change_log_delete 204")


#===========================================================
#  sys_email_log        
#===========================================================
    
    def test_sys_email_log_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "body":"ts",
            "body_type":"ts",
            "date_log":"050222",
            "date_send": "050222",
            "email_from":"ts",
            "email_to":"st",
            "error_message":"st",
            "login":"st",
            "subject": "st",
            "sys_unit_id": "94d93bd4-709a-4e13-84b1-dfdcacb1d14a",
            "type_in_out":"ts"

            }
        
        response = self.client.post(url_for('sysemaillog.save'), json=req_post, headers=token)
        tests_id1_sys_email_log = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_email_log",tests_id1_sys_email_log)
        self.assertEqual(response.status_code, 201," test_sys_email_log_001_create")

#====================

    def test_sys_email_log_002_create(self):
 
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "body":"ts",
            "body_type":"ts",
            "date_log":"050222",
            "date_send": "050222",
            "email_from":"ts",
            "email_to":"st",
            "error_message":"st",
            "login":"st",
            "subject": "st",
            "sys_unit_id": "94d93bd4-709a-4e13-84b1-dfdcacb1d14a",
            "type_in_out":"ts"

            }
        
        response = self.client.post(url_for('sysemaillog.save'), json=req_post, headers=token)
        tests_id2_sys_email_log = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_email_log",tests_id2_sys_email_log)
        self.assertEqual(response.status_code, 201,"test_sys_email_log_001_create" )

#====================

    def test_sys_email_log_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('sysemaillog.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "sys_email_log_get 200")

#====================

    def test_sys_email_log_get_by_id(self):
      
        token = self.create_token()
        response = self.client.get(url_for('sysemaillog.find_by_id',id=self.session.get("tests_id1_sys_email_log")), headers=token)
        
        self.assertEqual(response.status_code, 200, "sys_email_log_get_by_id 200")

#====================

    def test_sys_email_log_delete(self):

    
        token = self.create_token()

        response = self.client.delete(url_for('sysemaillog.delete',id=self.session.get("tests_id2_sys_email_log")), headers=token)


        self.assertEqual(response.status_code, 204, "sys_email_log_delete 204")
      
#===========================================================
#  sys_notification_log           
#===========================================================
    def test_sys_notification_log_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "action_body1": "ts",
            "action_body2": "st",
            "action_body3": "ts",
            "action_header1": "ts",
            "action_header2": "ts",
            "action_header3": "ts",
            "action_label1": "ts",
            "action_label2": "ts",
            "action_label3": "ts",
            "action_type1": "ts",
            "action_type2": "ts",
            "action_type3": "ts",
            "action_url1": "st",
            "action_url2": "ts",
            "action_url3": "st",
            "checked": "S",
            "dt_message": "ts",
            "email_to": "ts",
            "icon": "ts",
            "id": "ad4d038c-1ff3-4863-a2e6-fffd269f3c3f",
            "message": "",
            "subject": "ts",
            "sys_user_id": "4e1a831f-b877-4bf1-ad4d-e12079d709f6",
            "sys_user_to_id": "ts",
            "type_notification": "ts"

            }
        
        response = self.client.post(url_for('sysnotificationlog.save'), json=req_post, headers=token)
        tests_id1_sys_notification_log = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_notification_log",tests_id1_sys_notification_log)
        self.assertEqual(response.status_code, 201 ,"sys_notification_log_001_create 201")

#====================

    def test_sys_notification_log_002_create(self):
 
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "action_body1": "ts",
            "action_body2": "st",
            "action_body3": "ts",
            "action_header1": "ts",
            "action_header2": "ts",
            "action_header3": "ts",
            "action_label1": "ts",
            "action_label2": "ts",
            "action_label3": "ts",
            "action_type1": "ts",
            "action_type2": "ts",
            "action_type3": "ts",
            "action_url1": "st",
            "action_url2": "ts",
            "action_url3": "st",
            "checked": "S",
            "dt_message": "ts",
            "email_to": "ts",
            "icon": "ts",
            "id": "ad4d038c-1ff3-4863-a2e6-fffd269f3c3f",
            "message": "",
            "subject": "ts",
            "sys_user_id": "4e1a831f-b877-4bf1-ad4d-e12079d709f6",
            "sys_user_to_id": "ts",
            "type_notification": "ts"

            }
        
        response = self.client.post(url_for('sysnotificationlog.save'), json=req_post, headers=token)
        tests_id2_sys_notification_log = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_notification_log",tests_id2_sys_notification_log)
        self.assertEqual(response.status_code, 201, "sys_notification_log_001_create 201")
 
#====================
    
    def test_sys_notification_log_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('sysnotificationlog.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "sys_notification_log_get 200")

#====================

    def test_sys_notification_log_get_by_id(self):
      
        token = self.create_token()
        response = self.client.get(url_for('sysnotificationlog.find_by_id',id=self.session.get("tests_id1_sys_notification_log")), headers=token)
        
        self.assertEqual(response.status_code, 200, "sys_notification_log_get_by_id 200")

#====================

    def test_sys_notification_log_delete(self):

    
        token = self.create_token()

        response = self.client.delete(url_for('sysnotificationlog.delete',id=self.session.get("tests_id2_sys_notification_log")), headers=token)


        self.assertEqual(response.status_code, 204, "sys_notification_log_delete 204")
        
#===========================================================
#  sys_token            
#===========================================================
    def test_sys_token_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "dt_token":"15/04/2001",
            "dt_validade":"15/04/2001",
            "token":str(uuidCreate)

            }
        
        response = self.client.post(url_for('systoken.save'), json=req_post, headers=token)
        tests_id1_sys_token = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_token",tests_id1_sys_token)
        self.assertEqual(response.status_code, 201, "sys_token_001_create 201")

#====================

    def test_sys_token_002_create(self):
 
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "dt_token":"15/04/2001",
            "dt_validade":"15/04/2001",
            "token":str(uuidCreate)

            }
        
        response = self.client.post(url_for('systoken.save'), json=req_post, headers=token)
        tests_id2_sys_token = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_token",tests_id2_sys_token)
        self.assertEqual(response.status_code, 201, "sys_token_002_create 201")
 
#====================
    
    def test_sys_token_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('systoken.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "sys_token_get 200" )

#====================

    def test_sys_token_get_by_id(self):
      
        token = self.create_token()
        response = self.client.get(url_for('systoken.find_by_id',id=self.session.get("tests_id1_sys_token")), headers=token)
        
        self.assertEqual(response.status_code, 200,"sys_token_get_by_id 200")

#====================

    def test_sys_token_delete(self):

    
        token = self.create_token()

        response = self.client.delete(url_for('systoken.delete',id=self.session.get("tests_id2_sys_token")), headers=token)


        self.assertEqual(response.status_code, 204, "sys_token_delete 204")
        
#===========================================================
# sys_type_description         
#===========================================================
    def test_sys_type_description_001_create(self):
    
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "description_type":"trerers",
            "field_name": "tst",
            "table_name":"tst",
            "value_type": str(uuidCreate)

            }
        
        response = self.client.post(url_for('systypedescription.save'), json=req_post, headers=token)
        tests_id1_sys_type_description = json.loads(response.data.decode())['id']
        self.session.set("tests_id1_sys_type_description",tests_id1_sys_type_description)
        self.assertEqual(response.status_code, 201, "sys_type_description_001_create 201")

#====================

    def test_sys_type_description_002_create(self):
 
        uuidCreate = uuid.uuid4()
        token = self.create_token()
        req_post ={
            "id": str(uuidCreate),
            "description_type":"trerers",
            "field_name": "tst",
            "table_name":"tst",
            "value_type": str(uuidCreate)

            }
        
        response = self.client.post(url_for('systypedescription.save'), json=req_post, headers=token)
        tests_id2_sys_type_description = json.loads(response.data.decode())['id']
        self.session.set("tests_id2_sys_type_description",tests_id2_sys_type_description)
        self.assertEqual(response.status_code, 201, "sys_type_description_002_create 201")
 
#====================
    
    def test_sys_type_description_get(self):
    
        token = self.create_token()
        response = self.client.get(
            url_for('systypedescription.find_all'),
            headers=token
        )
        result = len(response.json)>0
        
        self.assertTrue(result, "sys_type_description_get 200")

#====================

    def test_sys_type_description_get_by_id(self):
      
        token = self.create_token()
        response = self.client.get(url_for('systypedescription.find_by_id',id=self.session.get("tests_id1_sys_type_description")), headers=token)
        
        self.assertEqual(response.status_code, 200, "sys_type_description_get_by_id 200")

#====================

    def test_sys_type_description_delete(self):

    
        token = self.create_token()

        response = self.client.delete(url_for('systypedescription.delete',id=self.session.get("tests_id2_sys_type_description")), headers=token)


        self.assertEqual(response.status_code, 204, "sys_type_description_delete 204")



