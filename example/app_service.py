from nestipy.common import Injectable
from dataclasses import asdict

from product_document import Product, ProductDto


@Injectable()
class AppService:

    @classmethod
    async def get(cls):
        data = []
        result = await Product.find_all().to_list()
        for r in result:
            data.append(r.to_json())
        return data

    @classmethod
    async def post(cls, data: ProductDto):
        return await Product(**asdict(data)).save()

    @classmethod
    async def put(cls, id_: int, data: ProductDto):
        return Product.find_one(Product.id == id_).update(**asdict(data))

    @classmethod
    async def delete(cls, id_: int):
        return Product.find_one(Product.id == id_).delete()
