SHELL := /bin/bash

GIT_TAG = $(shell git describe --tags)
APP="GridGenerator"


ui:
	pyuic5 ui/UIMainWindowForm.ui -o UIMainWindowForm.py

	pyrcc5 resources.qrc -o resources_rc.py
.PHONY: ui

build:
	rm -rf ./build ./dist
	pyinstaller main.py -n ${APP} --windowed
	mkdir -p dist/${APP}/icons
	cp -r icons/vibrator-48.png dist/${APP}/icons
	#cp -r icons/ dist/OffsetCheck
	cd dist; \
	tar zcvf ../dist-out/${APP}-"${GIT_TAG}".linux.tgz ${APP}/; \
	cd ..
	@echo "TAG: ${GIT_TAG}"
.PHONY: build

build-osx:
	@echo "TAG: ${GIT_TAG}"
	@echo "Not implemented yet"
.PHONY: build-osx