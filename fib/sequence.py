from flask_restful import Resource

class NegativeNumberError(Exception):
    pass

class FibSequenceResource(Resource):
    def get(self, number):
        number = int(number)

        if number < 0:
            raise NegativeNumberError

        sequence = []

        for n in self._sequence(number):
            sequence.append(n)

        return sequence

    def _sequence(self, number):
        a, b = 0, 1
        while True:
            if (a >= number): return
            yield a
            a, b = b, a + b
