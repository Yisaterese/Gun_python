class Person:
  def __int__(self,problem_type = []):
          self._problem_type = []

  def addProblems(self,prob) -> None:
    self._problem_type.append(prob)

  def recounted_problems(self) -> []:
    return self._problem_type

  def solved_problems(self,prob1) -> None:
      for index in self._problem_type:
          if self._problem_type[index] == prob1:
            self._problem_type.remove(prob1)
