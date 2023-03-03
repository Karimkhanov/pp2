def camel_to_snake(camel_str):
    snake_str = ''
    for i, char in enumerate(camel_str):
        if i > 0 and char.isupper():
            snake_str += '_'
        snake_str += char.lower()
    return snake_str


camel_str = "CamelCaseString"
snake_str = camel_to_snake(camel_str)
print(snake_str)
