import uvicorn
from nestipy.openapi import DocumentBuilder, SwaggerModule

from app_module import AppModule
from nestipy.core import NestipyFactory

app = NestipyFactory.create(AppModule)

document = DocumentBuilder().set_title("Beanie Mongo").set_description("API Mongo async").build()
SwaggerModule.setup('api', app, document)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8000, reload=True)
