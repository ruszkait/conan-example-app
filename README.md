# example application workflow with conan

## development

install dependencies to build folder (e.g. `build`)

```
conan install . --build=missing -if=build
```

configure project in build folder (e.g. `build`)

```
cmake -S . -B build
```

build project in build folder (e.g. `build`)

```
cmake --build build --config Release -j
```

## deployment

create a packaged version with specified user and channel (e.g. `dena/testing`)

```
conan create . dena/testing
```

upload previously created package to a conan server of choice (e.g. `dena-local`)

```
conan upload dena_app/0.1@dena/testing --all -r=dena-local
```

## usage

install the package from server (build if missing) into the conan cache

```
conan install dena_app/0.1@dena/testing --build=missing -s build_type=Debug
```