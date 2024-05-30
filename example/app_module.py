from nestipy.common import Module
from nestipy_config import ConfigModule, ConfigOption, ConfigService

from app_controller import AppController
from app_service import AppService
from product_document import Product
from nestipy_beanie import BeanieModule, BeanieOption


def beanie_config(config: ConfigService) -> BeanieOption:
    return BeanieOption(
        url=f"mongodb://{config.get('DB_USER')}:{config.get('DB_PASSWORD')}@{config.get('DB_HOST')}:{config.get('DB_PORT')}",
        documents=[Product],
        database=config.get("DB_NAME")
    )


@Module(
    imports=[
        ConfigModule.for_root(ConfigOption(), {'is_global': True}),
        BeanieModule.for_root_async(
            factory=beanie_config,
            inject=[ConfigService]
        ),
        # BeanieModule.for_root(BeanieOption(
        #     url="mongodb://user:pass@host:27017",
        #     database="nestipy",
        #     documents=[Product]
        # ))
    ],
    controllers=[AppController],
    providers=[AppService]
)
class AppModule:
    ...
