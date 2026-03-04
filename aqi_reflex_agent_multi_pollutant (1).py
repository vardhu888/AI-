def read_environment(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split("=")
            data[key.strip()] = float(value.strip())
    return data

def sub_index_pm25(value):
    if value <= 50: return 50
    if value <= 100: return 100
    if value <= 200: return 200
    if value <= 300: return 300
    if value <= 400: return 400
    return 500

def sub_index_pm10(value):
    if value <= 50: return 50
    if value <= 100: return 100
    if value <= 250: return 200
    if value <= 350: return 300
    if value <= 430: return 400
    return 500

def sub_index_co(value):
    if value <= 1: return 50
    if value <= 2: return 100
    if value <= 10: return 200
    if value <= 17: return 300
    if value <= 34: return 400
    return 500

def sub_index_no2(value):
    if value <= 40: return 50
    if value <= 80: return 100
    if value <= 180: return 200
    if value <= 280: return 300
    if value <= 400: return 400
    return 500

def sub_index_so2(value):
    if value <= 40: return 50
    if value <= 80: return 100
    if value <= 380: return 200
    if value <= 800: return 300
    if value <= 1600: return 400
    return 500

def sub_index_o3(value):
    if value <= 50: return 50
    if value <= 100: return 100
    if value <= 168: return 200
    if value <= 208: return 300
    if value <= 748: return 400
    return 500

def categorize_aqi(aqi):
    if aqi <= 50: return "Good", 100
    if aqi <= 100: return "Satisfactory", 80
    if aqi <= 200: return "Moderate", 60
    if aqi <= 300: return "Poor", 40
    if aqi <= 400: return "Very Poor", 20
    return "Severe", 5

def simple_reflex_agent(file_path, total_cars):
    env = read_environment(file_path)

    indices = []

    if "PM2.5" in env: indices.append(sub_index_pm25(env["PM2.5"]))
    if "PM10" in env: indices.append(sub_index_pm10(env["PM10"]))
    if "CO" in env: indices.append(sub_index_co(env["CO"]))
    if "NO2" in env: indices.append(sub_index_no2(env["NO2"]))
    if "SO2" in env: indices.append(sub_index_so2(env["SO2"]))
    if "O3" in env: indices.append(sub_index_o3(env["O3"]))

    overall_aqi = max(indices) if indices else 0

    category, percent_allowed = categorize_aqi(overall_aqi)
    allowed_cars = int((percent_allowed / 100) * total_cars)

    print("Overall AQI:", overall_aqi)
    print("AQI Category:", category)
    print("Cars Allowed on Road:", allowed_cars)

if __name__ == "__main__":
    simple_reflex_agent("environment.txt", 10000)
