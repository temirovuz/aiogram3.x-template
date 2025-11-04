from gettext import Catalog
from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    user_id = fields.CharField(max_length=100)
    phone_number = fields.CharField(max_length=13)
    password = fields.CharField(max_length=15, null=True)
    is_blocked = fields.BooleanField(default=False, index=True)
    is_admin = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=False)

    class Meta:
        table = "users"
        table_description = "Foydalanuvchi ma'lumotlari"

    def __str__(self):
        return f"{self.phone_number}"


class Category(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    parent = fields.ForeignKeyField(
        "models.Category",
        related_name="subcategories",
        null=True,
        on_delete=fields.CASCADE,
    )

    class Meta:
        table = "categories"
        table_description = "Bo'limlar"

    def __str__(self):
        return f"{self.name}"


class Data(Model):
    id = fields.IntField(pk=True)
    category = fields.ForeignKeyField(
        "models.Category", related_name="data", index=True
    )
    message_id = fields.CharField(max_length=50)

    class Meta:
        table = "data"
        table_description = "Ma'lumotlar"

    def __str__(self):
        return f"{self.category.name} - {self.message_id}"
