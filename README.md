# example application workflow with conan

## development

install dependencies to build folder (e.g. `build`)

```
conan install . -if=build
```

configure and build the project in build folder (e.g. `build`)

```
conan build . -bf=build
```

## deployment

create a packaged version with specified user and channel (e.g. `dena/stable`)

```
conan create . dena/stable
```

upload previously created package to a conan server of choice (e.g. `dena-local`)

```
conan upload dena_app/1.0@dena/stable --all -r=dena-local
```

## usage

install the package from server (build if missing) into the conan cache

```
conan install dena_app/1.0@dena/stable --build=missing -s build_type=Debug
```