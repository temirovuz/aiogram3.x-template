## Aiogramning 3.x versiasi uchun moslashtirilgan template.

### Loyihani clone qilasiz.

### Uv ni ornatib olamiz bu linux uchun

    curl -LsSf https://astral.sh/uv/install.sh | sh && chmod +x /root/.local/bin/uv


> 1.  Clone qilingan folderdaga kirasiz.
> 2.  .env  **file ichida** TOKEN, ADMIN\_ID, DB\_HOST, DB\_PORT, DB\_USER,DB\_PASSWORD, DB\_NAME

    uv sync 

**bu avtomatik venv yaratadi va kerakli barcha kutubxonalarni ham o'rnatadi.**

    uv run main.py  

**orqali botni ishga tushurasiz**

### Malumotlar bazasini migrate qilish

```plaintext
uv run aerich init -t config.TORTOISE_ORM
uv run aerich init-db
uv run aerich migrate
uv run aerich upgrade
```
