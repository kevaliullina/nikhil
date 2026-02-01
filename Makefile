install:
	uv sync

VD-games:
	vd-main

build:
	uv build

package-install:  # установка пакета в систему
	uv tool install ./dist/nikhil-0.1.0-py3-none-any.whl


