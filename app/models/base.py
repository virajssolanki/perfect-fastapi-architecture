from tortoise import fields, models


class BaseModel(models.Model):
    id = fields.IntField(pk=True)
    created_at = fields.DatetimeField(auto_now_add=True, null=True)
    updated_at = fields.DatetimeField(auto_now=True, null=True)
    is_deleted = fields.BooleanField(null=True, default=False)

    async def soft_delete(self):
        self.is_deleted = False
        await self.save(update_fields=["is_deleted"])