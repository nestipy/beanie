from typing import Annotated

from nestipy.common import Controller, Get, Post, Put, Delete
from nestipy.ioc import Inject, Body, Param
from nestipy.openapi import ApiBody, ApiOkResponse

from app_service import AppService
from product_document import ProductDto


@ApiOkResponse()
@Controller()
class AppController:
    service: Annotated[AppService, Inject()]

    @Get()
    async def get(self) -> list[dict]:
        return await self.service.get()

    @ApiBody(ProductDto)
    @Post()
    async def post(self, data: Annotated[ProductDto, Body()]) -> dict:
        return await self.service.post(data=data)

    @ApiBody(ProductDto)
    @Put('/{id}')
    async def put(self, app_id: Annotated[int, Param('id')], data: Annotated[ProductDto, Body()]) -> str:
        return await self.service.put(id_=app_id, data=data)

    @Delete('/{id}')
    async def delete(self, app_id: Annotated[int, Param('id')]) -> None:
        await self.service.delete(id_=app_id)
