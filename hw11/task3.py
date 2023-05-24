class Worker:
    def __init__(self, name, job, salary, education, work_experience):
        self.name = name
        self.job = job
        self.salary = salary
        self.education = education
        self.work_experience = work_experience

    def info(self):
        print(
            f'Name: {self.name}, Position: {self.job}, Salary: {self.salary}, Education: {self.education}, Work experience: {self.work_experience}')


class Project_Manager(Worker):
    def __init__(self, name, salary, education, work_experience):
        super().__init__(name, 'Project Manager', salary, education, work_experience)


class HR(Worker):
    def __init__(self, name, salary, education, work_experience):
        super().__init__(name, 'Human Resources', salary, education, work_experience)


class Developer(Worker):
    def __init__(self, name, salary, specialization, programming_language, education, work_experience):
        super().__init__(name, 'Developer', salary, education, work_experience)
        self.specialization = specialization
        self.programming_language = programming_language


class ML(Worker):
    def __init__(self, name, salary, programming_language, education, work_experience):
        super().__init__(name, 'ML-developer', salary, education, work_experience)
        self.programming_language = programming_language


class QA(Worker):
    def __init__(self, name, salary, education, work_experience):
        super().__init__(name, 'Quality assurance', salary, education, work_experience)


class Analyst(Worker):
    def __init__(self, name, salary, education, work_experience):
        super().__init__(name, 'Analyst', salary, education, work_experience)


class Economist(Worker):
    def __init__(self, name, salary, education, work_experience):
        super().__init__(name, 'Economist', salary, education, work_experience)


pm1 = Project_Manager('Alexandra Viktorova', 55000, 'in process of getting higher education', '0.5 years')
hr1 = HR('Alina Fedoseeva', 137500, 'secondary vocational education', ' 1 year')
developer1 = Developer('Ilya Ponomarenko', 350000, 'mobile apps', 'kotlin', 'higher education', '1 year')
developer2 = Developer('Maksim Trofimov', 375000, 'backend development', 'JS', 'higher education', '1.5 years')
ml1 = ML('Ekaterina Libets', 330000, 'python', 'higher education', '3.5 years')
qa1 = QA('Anastasiya Trifonova', 230000, 'higher education', '4 years')
analyst1 = Analyst('Anna Ponomarenko', 240000, 'higher education', '5 years')
economist1 = Economist('Alisa Zyryanova', 300000, 'higher education', '7 years')

pm1.info()
hr1.info()
developer1.info()
developer2.info()
ml1.info()
qa1.info()
analyst1.info()
economist1.info()
