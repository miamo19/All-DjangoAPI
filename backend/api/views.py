from django.http import JsonResponse
import json

#Create your views here.
def api_home(request, *args, **kwargs):
    body = request.body  #byte string of JSON data
    print(type(body))
    print(request.GET)   # url query params
    data = {}
    try:
        data = json.loads(body)  #take astring of JSON data ---> turn it to Python dictionary
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)  #converti to a dictinary but it's already a dictionary
    print(data['params'])

    data['headers'] = request.headers   #request.META -->   (this cannot automaticaly convert to JSON)
    print(data['headers'])

    json.dumps(dict(data['headers']))
    data['content_type'] = request.content_type
    return JsonResponse({"message": "Hi there, This is your django API crash course", "name":"Hyacinth", "Age": 18})
