# Lecture

강의 수강생들을 위한 웹 사이트 애플리케이션

## Requirements

- Python >= 3.6
- Django >= 2.0
- `.secrets` directory

### Create `.secrets` directory

```
<Project container>
	.requirements/
	.secrets/
		base.json
	django/
	manage.py
```

### Create `.secrets/base.json` file

```json
{
  "SECRET_KEY": "<Django secret key>"
}
```

## Installation (Using pyenv)

```
# Move to project container directory
cd <Project container>

# Create and apply virtualenv with Python 3.6.3
pyenv virtualenv 3.6.3 lecture
pyenv local lecture

# Install pip packages
pip install .requirements/dev_local.py
```


## Note

### Python executable "python" is v3.4.3, which is not supported by gyp

`.theme`폴더의 Bootstrap테마 모듈(`node_modules`)을 설치하기 위해 `npm install`하던 과정에서 오류 발생

[https://github.com/nodejs/node-gyp/issues/746](https://github.com/nodejs/node-gyp/issues/746)

```
npm install --python=python2.7
```

### Sass preprocessor

`Django Compressor`와 `django-libsass`를 사용

- [Django Compressor](https://django-compressor.readthedocs.io/en/latest/)
- [django-libsass](https://github.com/torchbox/django-libsass)

### Bootstrap테마가 참조하는 bower_components

`static`폴더 내의 `bower.json`파일을 이용, `bower install`명령어로 `bower_components`에 모듈들을 설치한다.

```
cd <Project container>
cd django/static
npm install
```

### HTML 이메일 메시지 전송

`EmailMultiAlternatives`클래스를 사용한다

```python
msg = EmailMultiAlternatives(subject, text_content, to=[to], from_email=from_email)
msg.attach_alternative(html_content, 'text/html')
msg.send()
```

### Markdown에디터 추가

[https://github.com/agusmakmun/django-markdown-editor](https://github.com/agusmakmun/django-markdown-editor)