# Mysql Database
```shell
docker-compose -f docker-compose-mysql.yml up -d
```

# Alembic commands
```shell
alembic init migrations
alembic list_templates
alembic -n first current
alembic -n second current
alembic -n third current
alembic -n first revision --autogenerate -m "First test created"
alembic -n second revision --autogenerate -m "Second test created"
alembic -n third revision --autogenerate -m "Third test created"
```