import asyncio  
async def main():  
    print ("Waiting 5 seconds. ")  
    for i in range(5):  
        await asyncio.sleep(1)  
        print ("Hello")  
    print ("Finished waiting.")  
asyncio.run(main())  