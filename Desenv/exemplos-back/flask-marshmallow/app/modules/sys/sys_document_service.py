
from flask import  send_from_directory
import flask
from sqlalchemy import null


from app.env import STORAGE_UPLOAD_FOLDER
from app.exceptions.ApiException import ApiException
from app.utils.generic_service import generic_service

import base64
import os

 


class sys_document_service(generic_service):
 
    def uploadfile(self,sys_document_id,file_base64,filename,file_content_type,storage_type):
        
        document = self.find_by_id(sys_document_id)

        if filename != document.filename:
            raise ApiException('File name not equal file saved')

        if file_content_type != document.content_type:
            raise ApiException('Content Type not equal file saved')

        file_content=base64.b64decode(file_base64)
        file_name_id = str(sys_document_id)+"-"+filename
        file_path = 'app/'+STORAGE_UPLOAD_FOLDER +'/'+file_name_id

        if storage_type == 1:

            if not os.path.isdir('app/'+STORAGE_UPLOAD_FOLDER):
                os.mkdir('app/'+STORAGE_UPLOAD_FOLDER)

            #Deleta se existir antigo
            if document.filename is not None:
                file_name_id_old = str(sys_document_id)+"-"+document.filename
                file_path_old = 'app/'+STORAGE_UPLOAD_FOLDER +'/'+file_name_id_old
                if os.path.exists(file_path_old):
                    os.remove(file_path_old)
                          

            with open(file_path, 'wb') as file:
                file.write(file_content)
        
                
                self.save(document)
                
                file.close()

            return {"sys_document_id":sys_document_id, "upload":True}
    
        elif storage_type == 2:
            pass
            #Impplementar cloud DO
    
    def download(self,sys_document_id,storage_type):

        if storage_type == 1:
            document = self.find_by_id(sys_document_id)
            filename =  sys_document_id+'-'+ str(document.filename)
            
            if document.id != sys_document_id:
              raise ApiException('File id not equal exist')

            if document.id == sys_document_id: 
            
                return send_from_directory(directory=STORAGE_UPLOAD_FOLDER, path=filename)
            
    def download_open(self,filename):
        return send_from_directory(directory=STORAGE_UPLOAD_FOLDER, path=filename ,as_attachment=True)
    def active(self,obj):
        
        if obj.active == 'S':
          obj.archive_date
        elif obj.active == 'N':
          obj.archive_date = None

        return self.save(obj)