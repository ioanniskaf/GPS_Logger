from django.http import HttpResponse
from django.template import loader
from pandas import read_csv
from json import loads

def gps_info(request,interviewer,respodent):
    data = read_csv('location/data/data.csv')
    data = data.loc[
        (data['interviewer'] == int(interviewer)) & (data['respodent'] == int(respodent))
    ]
    data = data.to_json(orient='records')
    template = loader.get_template("location/index.html")
    context = {'data': loads(data)[0] }

    return HttpResponse(template.render(context, request))