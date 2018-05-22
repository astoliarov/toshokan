build-docker-test:
	docker build -t toshokan-test  ./src

test-unit: build-docker-test
	docker run toshokan-test nose2 -v

test: test-unit

fmt:
	docker-compose -f docker-compose.fmt.yml build
	docker-compose -f docker-compose.fmt.yml run code black . -l 120
