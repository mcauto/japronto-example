# Japronto-example
japronto-example project (inspired by [pybanca-back](https://github.com/arieljimenez/pybanca-back))

japronto is very fast python web framework. but It is not stable.(2018.10.21)

## Dependencies

```Pipfile
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]
marshmallow="*"
marshmallow-jsonapi="*"
pymysql="*"
enum34="*"
pyOpenSSL="*"
pytest="*"
pytest-cov="*"
circus="*" 
sqlalchemy = "*"
werkzeug = "*"
"fcb869c" = {file = "https://github.com/squeaky-pl/japronto/archive/master.zip"}

[dev-packages]

[requires]
python_version = "3.6"
```

If you install japronto by pip, you will face the following [issue](https://github.com/squeaky-pl/japronto/issues/104).

Then, this solution is useful.

```bash
$ pipenv install https://github.com/squeaky-pl/japronto/archive/master.zip
```



## How to run

```bash
$ docker-compose up -d
...
... # docker images build
Creating network "test-japronto-example_default" with the default driver
Creating japronto       ... done
Creating mysql_japronto ... done
$ docker exec -it japronto bash
$ pipenv install
$ pipenv shell
$ python migrations.py
$ python main.py
Accepting connections on http://0.0.0.0:8080
```

