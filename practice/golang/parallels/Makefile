# Check that given variables are set and all have non-empty values,
# die with an error otherwise.
#
# Params:
#   1. Variable name(s) to test.
#   2. (optional) Error message to print.
check_defined = \
    $(strip $(foreach 1,$1, \
        $(call __check_defined,$1,$(strip $(value 2)))))
__check_defined = \
    $(if $(value $1),, \
      $(error Undefined $1$(if $2, ($2))))

git_commit := $(shell git rev-parse --short HEAD)
git_tag := $(or $(shell git tag --points-at HEAD), 0)

# NOTE: need define _Tag/_Commit/_Profile variable in main package
LD_FLAGS=-ldflags "-X main._Tag=$(git_tag) -X main._Commit=$(git_commit) -X main._Profile=$(Profile)"

PWD = $(shell pwd)
# NOTE: build will be executed in this docker image
build_image = ubuntu-ci:1.20
# NOTE: modify build command if needed
build_command = "make build Profile=$(Profile)"
.PHONY: build_docker build test lint

test:
	export PROJECT_ROOT=${PWD} && go test -v -coverprofile=cover.out.tmp -coverpkg=./...  ./...
	cat cover.out.tmp | grep -v "mock" | grep -v "docs.go" > cover.out
	go tool cover -func cover.out > coverage.txt

coverage:
	export PROJECT_ROOT=${PWD} && /go/bin/gotestsum --junitfile report.xml --format testname -- -race -gcflags=-l -coverpkg=./... -coverprofile=cover.out.tmp ./...
	cat cover.out.tmp | grep -v "mock" | grep -v "docs.go" > cover.out
	go tool cover -func cover.out > coverage.txt

lint:
	golangci-lint --timeout 5m run --out-format checkstyle ./... >  lint_report.xml

generate:
	go generate ./...

swagger:
	rm -rf docs/swagger
	swag init -d ./api/http -g ../../cmd/server/main.go -o docs/swagger/ --parseDependency

clean:
	rm -rf ${PWD}/logs/*
	rm -rf ${PWD}/cmd/server/logs/*
	rm -rf ${PWD}/dist

build_docker:
	$(call check_defined, Profile)
	@echo "profile $(Profile)"
	@echo "tag: $(git_tag), commit id: $(git_commit)"

	mkdir -p dist

	docker run -v $$HOME/gopath:/root/go --rm -v $(PWD):/home/deploy $(build_image) /bin/bash -c ${build_command}

build:
	$(call check_defined, Profile)
	@echo "profile $(Profile)"

	git config --global url."https://".insteadOf "https://"
	go env -w GOPROXY="https://goproxy.cn,direct"
	GOOS=linux go build ${LD_FLAGS} -mod=readonly -o dist/ ./cmd/...
	GOOS=linux GOARCH=arm64 go build
