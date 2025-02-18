version = $(shell cargo-get package.version)
cwd = $(shell pwd)

all: build build_arm64

build:
	cargo build

build_arm64:
	cross build --target aarch64-unknown-linux-musl --release --bin test