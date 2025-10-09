IMAGE_NAME=rpg_sim

build:
	docker build --target develop -t $(IMAGE_NAME) .

add:
	@read -p "Enter package to add: " pkg && \
	docker run --rm -v "$$(pwd)":/workdir $(IMAGE_NAME) uv add $$pkg && \
	$(MAKE) build

add-dev:
	@read -p "Enter dev package to add: " pkg && \
	docker run --rm -v "$$(pwd)":/workdir $(IMAGE_NAME) uv add --dev $$pkg && \
	$(MAKE) build

remove:
	@read -p "Enter package to remove: " pkg && \
	docker run --rm -v "$$(pwd)":/workdir $(IMAGE_NAME) uv remove $$pkg && \
	$(MAKE) build

remove-dev:
	@read -p "Enter dev package to remove: " pkg && \
	docker run --rm -v "$$(pwd)":/workdir $(IMAGE_NAME) uv remove --dev $$pkg && \
	$(MAKE) build

format:
	docker run --rm -v "$$(pwd)":/workdir $(IMAGE_NAME) ruff format /workdir