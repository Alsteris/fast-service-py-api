async def Greeting():
    data = "Hello World"
    return data 


async def GreetingForAll(data):
    if data == "hello":
        data = "Hello World for All"
    else:
        data = "another word"

    return data 

async def login (request):
    return request