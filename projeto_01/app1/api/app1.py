from ninja import Router
from django.http import Http404, HttpRequest, HttpResponse

#import schemas.py
from app1.schemas import App1SchemaIn, App1SchemaOut

router = Router()

#curl -s http://localhost:8000/api/app1/ | python3 -m json.tool
@router.get("/")
def list_tasks(request):
    return {"results": [
        {"id": 1, "title": "test title"},
    ]}

#curl -X POST -s http://localhost:8000/api/app1/ -d '{"title": "Alien Life Detection Algorithm Enhancement", "description": "Im"}'
@router.post("/", response=App1SchemaOut)
def create_task(request: HttpRequest, task_in: App1SchemaIn):
    return App1SchemaOut(id=1)

