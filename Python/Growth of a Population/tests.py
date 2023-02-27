import codewars_test as test
from solution import nb_year

@test.describe("nb_year")
def tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
        test.assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
        test.assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94)
        