from flask import request, Blueprint

unsigned_integer = Blueprint('unsigned_integer', __name__)


@unsigned_integer.get("/unsigned_integer/encode")
def encode():
    data = request.args.get("data", '0')
    size = request.args.get("size", '1')

    data = int(data)
    binary = bin(data)[2:]

    size = int(size)
    rem = size - len(binary)
    resized_binary = ('0' * rem) + binary

    return resized_binary


@unsigned_integer.get("/unsigned_integer/decode")
def decode():
    binary = request.args.get("binary", '0')

    data = int(binary, 2)
    data = str(data)

    return data