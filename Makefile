.PHONY: build test run

STATES ?= CE DF 
IMAGE = buscacep

build:
	docker build -t $(IMAGE) .

test:
	docker run --rm -v `pwd`/test-reports:/root/test-reports $(IMAGE) \
	python -m pytest --junitxml=test-reports/junit.xml --basetemp=out \
	rm -r ./out

run: 
	docker run --rm -v `pwd`/out:/root/out $(IMAGE) \
	python buscaCep.py $(STATES)