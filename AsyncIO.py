import time
import asyncio
import requests

async def function1():
    # await asyncio.sleep(1)
    URL = "https://cdn.pixabay.com/photo/2015/04/23/22/00/tree-736885_1280.jpg"
    response = requests.get(URL)
    open("img1.jpg","wb").write(response.content)

    print("func 1")
    return "Abc"

async def function2():
    # await asyncio.sleep(1)
    URL = "https://cdn.pixabay.com/photo/2015/04/19/08/32/marguerite-729510_640.jpg"
    response = requests.get(URL)
    open("img2.jpg","wb").write(response.content)
    
    print("func 2")

async def function3():
    # await asyncio.sleep(3)
    URL = "https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg"
    response = requests.get(URL)
    open("img3.jpg","wb").write(response.content)

    print("func 3")

async def main():
    # await function1()
    # await function2()
    # await function3()
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(L)
asyncio.run(main())