#DOCKER_IMAGE=continuumio/anaconda3
DOCKER_IMAGE=python:latest
FILENAME_MAIN=./src/main.py
FILENAME_TEST=./src/test_nqueens.py

run:
	@docker run --rm -v $(PWD):/home/work/ -w /home/work/ $(DOCKER_IMAGE) python $(FILENAME_MAIN)
test:
	@docker run --rm -v $(PWD):/home/work/ -w /home/work/ $(DOCKER_IMAGE) python $(FILENAME_TEST)


