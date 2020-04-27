import requests

def waterPlant():
    plantNo = {'plantNo' : 1}
    response = requests.post('http://localhost:5001/water_plant',data = plantNo)
    print(response.content)


if __name__ == '__main__':
    print('try')
    waterPlant()
    print('after')
