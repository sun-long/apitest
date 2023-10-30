from defines.belt.face_service_business import FaceSwaggerBusiness
from commonlib.sign_utils import encode_jwt_token
import threading
import time
def add_100w_person_to_db():
    host=f"https://ids.test.sensebelt.net"
    ak="2Mobf9c72Vo3aQVoWcaV54JkhCf"
    sk="Xp6EINE1YQIrqCEN0yzo7zMbH2odsVmA"
    # ak = "2JnWk8or7JuJqtBr3MthdJxCdfL"
    # sk = "XXIF0I3kUSSJR88NMgKsno4nAzPitUvS"
    
    token=encode_jwt_token(ak,sk)
    face1vn=FaceSwaggerBusiness(host,token=token)
    #创建库
    #入库
    name="100w_db"
    description="for testing performance"    
    resp=face1vn.FaceService_CreatePersonDBPostApi(name,description)
    
    # db_id=resp.json_get("id")    
    db_id="168782031247910594"
    image=face1vn.idsImageToBase64(f"face1vn/add_db_356K.jpg")
    images=[image]
    extra_info="test for performance "    
    for i in range(9286,1000000):
        person_id="a"+str(i)
            
    resp=face1vn.FaceService_AddPersonPostApi(db_id=db_id,person_id=person_id,images=images,extra_info=extra_info)


             


if __name__=='__main__':
    add_100w_person_to_db()