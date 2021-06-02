from ..core.calculate_distance import CalculateDistance

def test_calc_distance():

    starting_lat = "53.339428"
    starting_long = "-6.257664"

    ending_lat_1 = "52.986375"
    ending_long_1 = "-6.043701"

    ending_lat_2 = "51.92893"
    ending_long_2 = "-10.27699"

    cal_distance_obj = CalculateDistance(starting_lat, starting_long)
    distance_1 = cal_distance_obj.caluate_distance(ending_long_1, ending_lat_1)
    distance_2 = cal_distance_obj.caluate_distance(ending_long_2, ending_lat_2)

    assert round(distance_1, 2) == 41.77
    assert round(distance_2, 2) == 313.26


