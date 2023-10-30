import os
project_path = os.path.dirname(os.path.dirname(__file__))
pm_path = os.path.join(project_path, "data/postman")
swagger_path = os.path.join(project_path, "data/swagger")
pb_path = os.path.join(project_path, "data/pb")
grpc_req_path = os.path.join(project_path, 'data/grpc_req')
pm_req_path = os.path.join(project_path, 'data/pm_req')
contract_path = os.path.join(project_path, 'data/contract')
result_path = os.path.join(project_path, 'result')
resource_path = os.path.join(project_path, 'resource')
temp_path = os.path.join(project_path, 'temp')
temp_template_path = os.path.join(temp_path, 'templates')
template_path = os.path.join(project_path, 'templates')
code_gen_path = os.path.join(template_path, 'code_gen')
image_path = os.path.join(resource_path, "images")
goimage_path = os.path.join(image_path, "go_image")
ids_image_path = os.path.join(image_path, "ids_image")
console_image_path = os.path.join(image_path, "console_image")
ctid_image_path = os.path.join(image_path, "ctid_image")
nova_path = os.path.join(resource_path, "nova")
ids_face1vn_search_person_image_path= os.path.join(ids_image_path, "face1vn/search_person")
json_headers = {'Content-Type': 'application/json;charset=UTF-8', "Accept": "*/*", "apiVersion": "1.0"}

form_headers = {'Content-Type': 'application/x-www-form-urlencoded',
				"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"}
