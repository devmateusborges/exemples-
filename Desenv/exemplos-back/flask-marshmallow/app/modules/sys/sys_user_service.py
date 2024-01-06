from app.utils.generic_service import generic_service


class SysUser_service(generic_service):
    
    def save(self,obj):
        obj.gen_hash()
        return super().save(obj)        