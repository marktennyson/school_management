import uvicorn

from school_management.asgi import application

if __name__ == '__main__':
    uvicorn.run(application, port=8001)