#!/bin/bash

function main(){

    version="$1"

    if [[ -z "$version" ]]; then

	echo "Invalid argument version."
	exit 0

    fi

    if [[ ! -d tmp ]]; then

	mkdir tmp

    fi

    cd tmp

    git clone https://github.com/grpc-ecosystem/grpc-gateway -b "$version"

    protoc -I ./grpc-gateway/ --python_out=../ ./grpc-gateway/protoc-gen-swagger/options/annotations.proto ./grpc-gateway/protoc-gen-swagger/options/openapiv2.proto

}

main "$@"
