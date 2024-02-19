from Person import Person
from Problem import Problem


def testPersonCanAddProblems():
    problem = Problem().SPIRITUAL
    problem.addProblems("wirdDreams")
    assert  problem.recounted_problems() == 1