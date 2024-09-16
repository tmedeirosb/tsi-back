from ninja import Router
from django.http import Http404, HttpRequest, HttpResponse

#import schemas.py
from app1.schemas import App1SchemaIn, App1SchemaOut, AgendaSchemaIn, AgendaSchemaOut

router = Router()

#curl -s http://localhost:8000/api/app1/teste_get | python3 -m json.tool
@router.get("/teste_get")
def list_tasks(request):
    return {"results": [
        {"id": 1, "title": "test title"},
    ]}

#curl -s http://localhost:8000/api/app1/ | python3 -m json.tool
@router.get('/', response=list[AgendaSchemaOut])
def list_tasks(request):
    return [AgendaSchemaOut(nome="Maria", telefone="987654321")]

#curl -X POST -s http://localhost:8000/api/app1/teste_post -d '{"title": "Alien Life Detection Algorithm Enhancement", "description": "Im"}'
@router.post("/teste_post", response=App1SchemaOut)
def create_task(request: HttpRequest, task_in: App1SchemaIn):
    return App1SchemaOut(id=1)



