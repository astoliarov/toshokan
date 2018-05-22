build-docker-test:
	docker build -t toshokan-test  ./src

test-unit: build-docker-test
	docker run toshokan-test nose2 -v

test: test-unit
