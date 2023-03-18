def selection_of_parameters(json_response):
    toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    sizes = toponym['boundedBy']['Envelope']
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

    a, c = list(map(float, sizes['upperCorner'].split()))
    b, d = list(map(float, sizes['lowerCorner'].split()))

    map_params = {
        "ll": ",".join([toponym_longitude, toponym_lattitude]),
        "spn": ",".join([str(a - b), str(c - d)]),
        "l": "map"}
    return map_params
