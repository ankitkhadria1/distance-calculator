import json

from ..core.get_customers import GetUserDataByDistance

def test_filter_customers():

    starting_lat = "53.339428"
    starting_long = "-6.257664"
    max_distance = 100 #"In KM"
    filename = "test_customers.txt"

    obj = GetUserDataByDistance(starting_lat, starting_long, max_distance, filename)
    obj.break_largefile(10)

    assert len(obj.filenames) == 4

    obj.filter_customers()
    data = []
    with open("output/output.json") as f:
        data = json.load(f)

    assert len(data) == 16
        

