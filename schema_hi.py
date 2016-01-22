from schema import Schema

print Schema(int).validate(123)

#print Schema(int).validate('123')